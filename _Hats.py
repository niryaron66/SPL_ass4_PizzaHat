class _Hats:
    def __init__(self ,conn):
        self.conn = conn

    def insert(self, hat):
        curs=self.conn.cursor()
        curs.execute("""
        INSERT INTO hats(id,topping,supplier,quantity) VALUES(?,?,?,?)""",
        [hat.id,hat.topping,hat.supplier,hat.quantity])

    def handle_order(self, topping):
        curs = self.conn.cursor()
        curs.execute("SELECT min(supplier),quantity,id FROM hats WHERE topping=?", [topping])
        tmp = curs.fetchone()
        sup_id =tmp[0]
        quan = tmp[1]
        hat_id = tmp[2]
        if (quan > 1):
            curs.execute("UPDATE hats SET quantity =? WHERE topping =? AND supplier =?", (quan - 1, topping, sup_id))
        else:
            curs.execute("DELETE FROM hats WHERE topping =? AND supplier =? ", [topping, sup_id])
        return hat_id,sup_id

    def getName(self,sup_id):
        curs = self.conn.cursor()
        curs.execute("""
                        SELECT name FROM suppliers WHERE id=?""", [sup_id])
        return curs.fetchone()[0]