import json

from app import app
from flask import request, abort, Response
from c4algo import convert

@app.route('/', methods=['POST'])
def hey():
    data = request.get_json()
    path = "C:/xampp/htdocs/kms/admin/" + data['filepath']
    result = convert.distinguish(path)
    
    return result
