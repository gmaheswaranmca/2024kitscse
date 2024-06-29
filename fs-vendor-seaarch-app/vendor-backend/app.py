from flask import Flask, request, jsonify 
from db import Vendor, vendorTablesCreate, createVendor, readAllVendors, updateVendor, deleteVendor, readVendorById
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

@app.route("/vendors",methods=["POST"])
@cross_origin()
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
@cross_origin()
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
    return jsonify(dict_vendors)

@app.route("/vendors/<id>",methods=["GET"])
@cross_origin()
def vendors_read_byid(id):
    vendor = readVendorById(id)
    if vendor != None:
        dict_vendor = {
            'id':vendor.id,
            'name':vendor.name,
            'ratings':vendor.ratings,
            'place':vendor.place,
            'phone_number':vendor.phone_number
        }
        return jsonify(dict_vendor)
    else:
        return jsonify({'error':'Vendor Not Found'})
    
@app.route("/vendors/<id>",methods=["PUT"])
@cross_origin()
def vendors_update(id):
    vendor = Vendor()    
    body = request.get_json()
    vendor.id = id
    vendor.name = body['name']
    vendor.ratings = body['ratings']
    vendor.place = body['place']
    vendor.phone_number = body['phone_number']
    updateVendor(vendor)
    vendor = readVendorById(id)
    dict_vendor = {
        'id':vendor.id,
        'name':vendor.name,
        'ratings':vendor.ratings,
        'place':vendor.place,
        'phone_number':vendor.phone_number
    }
    return jsonify(dict_vendor)


@app.route("/vendors/<id>",methods=["DELETE"])
@cross_origin()
def vendors_delete(id):
    deleteVendor(id)
    return jsonify({'message':'vendor deleted successfully.'})

app.run(debug=True)
