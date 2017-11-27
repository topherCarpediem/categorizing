import json

from app import app
from flask import request, abort


@app.route('/', methods=['POST'])
def hey():

    print(request.form)
    return json.dumps(request.get_json())
