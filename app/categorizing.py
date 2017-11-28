import json

from app import app
from flask import request, abort
from c4algo import convert

@app.route('/', methods=['POST'])
def hey():
    data = request.get_json()
    path = data['filepath']
    result = convert.distinguish(path)
    print(request.get_json())
    return json.dumps(result)
