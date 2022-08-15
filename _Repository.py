import sqlite3
import atexit
import sys
from _Hat import _Hat
from _Hats import _Hats
from _Orders import _Orders
from _Supplier import _Supplier
from _Suppliers import _Suppliers




class _Repository:
    def __init__(self):
        self._conn=sqlite3.connect(sys.argv[4])
        self.hats = _Hats(self._conn)
        self.suppliers = _Suppliers(self._conn)
        self.order = _Orders(self._conn)

    def _close(self):
         self._conn.commit()
         self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE hats(id INTEGER PRIMARY KEY,
        topping STRING NOT NULL, 
        supplier INTEGER REFERENCES Supplier(id),
        quantity INTEGER NOT NULL
        );
        
         CREATE TABLE suppliers(id INTEGER PRIMARY KEY,
         name STRING NOT NULL);
         
         CREATE TABLE orders(id INTEGER PRIMARY KEY,
         location STRING NOT NULL,
         hat INTEGER REFERENCES hats(id)
         );  
        """)

    def configDatabase(self, config_path):
        file = open(config_path, 'r')
        temp = file.read().splitlines()
        arguments = temp[0].split(',')
        Index = 1
        hatsList = temp[Index:int(arguments[0]) + Index]
        Index += int(arguments[0])
        suppliersList = temp[Index:int(arguments[1]) + Index]
        Index += int(arguments[1])

        for x in hatsList:
            temp = x.split(',')
            self.hats.insert(_Hat(temp[0], temp[1], temp[2], temp[3]))

        for x in suppliersList:
            temp = x.split(',')
            self.suppliers.insert(_Supplier(temp[0], temp[1]))

    def takeCareOfOrders(self, order_path , output_path):
        id = 1
        file = open(order_path, 'r')
        input = file.read().splitlines()
        for x in input:
            temp = x.split(',')
            temp2 = self.hats.handle_order(temp[1])
            hat_id = temp2[0]
            sup_name = self.hats.getName(temp2[1])
            self._conn.execute("INSERT INTO orders(id,location,hat) VALUES(?,?,?)",[id, temp[0], hat_id] )
            id+=1
            list = [temp[1], sup_name, temp[0]]
            listToStr = ','.join([str(elem) for elem in list])
            file = open(output_path, "a")
            file.write(listToStr + "\n")




# the repository singleton
repo = _Repository()
atexit.register(repo._close)

