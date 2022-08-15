class _Orders:
    def __init__(self ,conn):
        self.conn = conn

    def insert(self, order):
        curs = self.conn.cursor()
        curs.execute("""
           INSERT INTO orders(id,location,hat) VALUES(?,?,?)""",
                     [order.id, order.location, order.hat])
