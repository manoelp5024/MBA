from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World! &lt;strong&gt;I am learning Flask&lt;/strong&gt;", 200

app.run()
