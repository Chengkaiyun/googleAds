def initialize():
    global countryInfo, country, fileName
    global df, new_df
    global sku, designName, productLine, device, caseColor, bumperColor, handle, dashDevice

    global url_dict, backplate

    handle = []
    dashDevice =[]

    url_dict = {
        'TW': 'https://cdn.shopify.com/s/files/1/0740/2335/files/',
        'IO': 'https://cdn.shopify.com/s/files/1/0274/8717/files/',
        'FR': 'https://cdn.shopify.com/s/files/1/1286/1203/files/'
    }

    backplate = {
        'TW': '',
        'IO': ' Backplate',
        'FR': ' Verso'
    }