class _Suppliers:
    def __init__(self ,conn):
        self.conn = conn

    def insert(self, supplier):
        curs = self.conn.cursor()
        curs.execute("""
           INSERT INTO suppliers(id,name) VALUES(?,?)""",
                     [supplier.id, supplier.name])