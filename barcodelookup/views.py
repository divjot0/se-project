from django.shortcuts import render
from django.http import HttpResponse

import json
import requests
# Create your views here.

ISBN_API_URL = "https://openlibrary.org/api/books?bibkeys=ISBN:{}&format=json&jscmd=data"

def is_isbn(barcode):
    if str(barcode).startswith("978"):
        return True
    return False

def lookup_product(request, barcode):
    # example test
    # TODO: change function to scrap or do api calls for barcode lookup
    # TODO: 1. Look into openstore database
    # TODO: 2. If not, then look up in https://barcodelookup.com etc
    # books api: https://openlibrary.org/api/books?bibkeys=ISBN:9789352135219&format=json&jscmd=data
    
    # check if barcode is isbn
    if is_isbn(barcode):
        api_url = ISBN_API_URL.format(barcode)
        resp = requests.get(api_url)
        return HttpResponse(resp)
    else:
        return HttpResponse(json.dumps({"barcode": barcode, 
            "name": "Lotus notebook No.4",
            "description": "It is a test\nTODO: add api or scrapper for products",
        }))