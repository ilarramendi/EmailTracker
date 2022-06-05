from flask import Flask, send_file, request, abort
import json
from datetime import datetime
from sys import argv
from random import randint
from base64 import b64encode

app = Flask(__name__)

BASE_PATH = 'https://test.com/asd/'

@app.route('/<path>')
def main(path):
    js = {}
    with open('storage.json') as f:
        js = json.load(f)
            
    if path in js:
        if request.headers['X-Real-Ip'] in js[path]['requests']:
            js[path]['requests'][request.headers['X-Real-Ip']].append(datetime.now().strftime('%m/%d/%Y, %H:%M:%S'))
        else: js[path]['requests'][request.headers['X-Real-Ip']] = [datetime.now().strftime('%m/%d/%Y, %H:%M:%S')]
        
        with open('storage.json', 'w') as f:
            json.dump(js, f, sort_keys=True, indent=3)
        return send_file('image.jpg')
    
    return abort(404)

if argv[1] == 'start':
    app.run(host="0.0.0.0")

elif argv[1] == 'new':
    if len(argv) > 2:
        with open('storage.json') as f:
            js = json.load(f)
        path = str(randint(0, 9999999999)).zfill(10) + '.jpg'
        while path in js: path = str(randint(0, 999999999)).zfill(10) + '.jpg'
        js[path] = {'requests': {}, 'name': argv[2]}
        with open('storage.json', 'w') as f:
                json.dump(js, f, sort_keys=True, indent=3)
        print(BASE_PATH + path)
    else: print('missing name')