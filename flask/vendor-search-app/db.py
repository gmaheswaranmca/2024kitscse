import sqlite3

def connect():
    con = sqlite3.connect('vendor_search_db.db')
    return con 
def vendorTablesCreate():
    sql = """CREATE TABLE IF NOT EXISTS vendor(
        id integer primary key AUTOINCREMENT,
        name varchar(255) not null,
        ratings integer not null default 1,
        place varchar(255) not null,
        phone_number varchar(20) not null
    )"""
    con = connect()
    con.execute(sql)
    con.close()
    print("Database is connected and in sync.")

class Vendor:
    def __init__(self, id=None,
        name='',
        ratings=1,
        place='',
        phone_number=''):
        self.id = id 
        self.name = name 
        self.ratings = ratings 
        self.place = place 
        self.phone_number = phone_number
    #def __str__(self):
    #    return f'[{self.id},{self.name},{self.ratings},{self.place},{self.phone_number}]'

def createVendor(vendor):
    sql = """INSERT INTO vendor(name,ratings,
    place, phone_number)
    VALUES(?,?,?,?)"""
    params = (vendor.name, vendor.ratings,
              vendor.place, vendor.phone_number,)
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    con.close()

def readAllVendors():
    sql = """SELECT id,name,ratings,
    place, phone_number FROM vendor"""
    params = tuple()
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchall() #[rows], each row=[id,name,...]
    con.close()

    vendors = []
    for row in result:
        vendors.append(Vendor(id=row[0],name=row[1],
                ratings=row[2],place=row[3],
                phone_number=row[4]))
    return vendors 




















