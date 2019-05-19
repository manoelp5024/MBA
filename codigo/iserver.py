from flask import Flask, abort, request 
import json

app = Flask(__name__)


@app.route('/temphumid/send', methods=['POST']) 
def send():
    print(request.json)
    return "Ok... Python!"

app.run(host='0.0.0.0', port=8080, debug=True)