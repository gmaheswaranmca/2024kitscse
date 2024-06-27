from db import vendorTablesCreate,Vendor,createVendor,readAllVendors

vendorTablesCreate()

vendor = Vendor(name='ebox', ratings=3,
    place='comibatore', phone_number='3334422111')
createVendor(vendor)

vendor = Vendor(name='bytexl', ratings=4,
    place='hyderabad', phone_number='98989831122')
createVendor(vendor)

vendors = readAllVendors()
for vendor in vendors:
    print(vendor)


