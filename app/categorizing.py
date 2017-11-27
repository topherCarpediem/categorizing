import json

from app import app
from flask import request, abort


@app.route('/', methods=['POST'])
def hey():
    if not request.json:
        abort(400)
    print(request.get_json())
    return json.dumps(request.get_json())
