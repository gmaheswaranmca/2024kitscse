from flask import Flask, request, jsonify 
from db import Vendor, vendorTablesCreate, createVendor, readAllVendors, updateVendor, deleteVendor, readVendorById
app = Flask(__name__)

vendorTablesCreate()

@app.route("/vendors",methods=["POST"])
def vendor_create():
    vendor = Vendor()
    body = request.get_json()
    vendor.name = body['name']
    vendor.ratings = body['ratings']
    vendor.place = body['place']
    vendor.phone_number = body['phone_number']
    id = createVendor(vendor)
    vendor = readVendorById(id)
    dict_vendor = {
        'id':vendor.id,
        'name':vendor.name,
        'ratings':vendor.ratings,
        'place':vendor.place,
        'phone_number':vendor.phone_number
    }
    return jsonify(dict_vendor)
    
@app.route("/vendors",methods=["GET"])
def vendor_readall():
    vendors = readAllVendors()
    dict_vendors = []
    for vendor in vendors: 
        dict_vendors.append({
            'id':vendor.id,
            'name':vendor.name,
            'ratings':vendor.ratings,
            'place':vendor.place,
            'phone_number':vendor.phone_number
        })
    return jsonify(vendors)

'''
@app.route("/vendors/edit/<id>",methods=["GET","POST"])
def vendor_edit(id):
    print('debugging 1001 id=',id)
    if request.method == "POST":
        vendor = Vendor()
        vendor.id = request.form['id']
        vendor.name = request.form['name']
        vendor.ratings = request.form['ratings']
        vendor.place = request.form['place']
        vendor.phone_number = request.form['phone_number']
        updateVendor(vendor)
        return redirect('/')
    else:
        vendor = readVendorById(id)
        return render_template('vendors-edit.html',vendor=vendor)

@app.route("/vendors/delete/<int:id>",methods=["GET"])
def vendor_delete(id):
    deleteVendor(id)
    return redirect('/')
'''



app.run(debug=True)
