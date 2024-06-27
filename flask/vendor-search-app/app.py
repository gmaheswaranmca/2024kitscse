from flask import Flask, request, render_template, redirect 
from db import Vendor, vendorTablesCreate, createVendor, readAllVendors
app = Flask(__name__)

vendorTablesCreate()

@app.route("/vendors/create",methods=["GET","POST"])
def vendor_create():
    if request.method == "POST":
        vendor = Vendor()
        vendor.name = request.form['name']
        vendor.ratings = request.form['ratings']
        vendor.place = request.form['place']
        vendor.phone_number = request.form['phone_number']
        createVendor(vendor)
        return redirect('/')
    else:
        return render_template('vendors-create.html')

@app.route("/",methods=["GET"])
def vendor_list():
    vendors = readAllVendors()
    return render_template('vendors-list.html', vendors=vendors)

app.run(debug=True)

'''
name: [             ]               
ratings:[               ]
place: [                ]
phone number:  [            ]
<Create Vendor>
'''