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
    id = cur.lastrowid  #
    con.commit()
    con.close()
    return id           #

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

def updateVendor(vendor):
    sql = """UPDATE vendor
    set name=?,ratings=?,
    place=?, phone_number=?
    WHERE (id=?)"""
    params = (vendor.name, vendor.ratings,
              vendor.place, vendor.phone_number,
              vendor.id, )
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    con.close()
def deleteVendor(id):
    sql = """DELETE from vendor
    WHERE (id=?)"""
    params = (id, )
    con = connect()
    cur = con.cursor()
    cur.execute(sql,params)
    con.commit()
    con.close()
    
def readVendorById(id):
    sql = """SELECT id,name,ratings,
    place, phone_number FROM vendor
    WHERE (id=?)"""
    params = (id,)
    con = connect()
    cur = con.cursor()
    response = cur.execute(sql,params)
    result = response.fetchone() #row=[id,name,...]
    con.close()

    if result != None:
        vendor = Vendor(id=result[0],name=result[1],
                    ratings=result[2],place=result[3],
                    phone_number=result[4])
    else:
        vendor = None 
    return vendor

