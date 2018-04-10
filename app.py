
import os
import signal
from flask import Flask, url_for
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = "<html><body><h1 align='center'>"
    page += generator.generate_buzz()
    page += "</h1><p align='center'>"
    page += "Version: 1.0"
    page += "</p></body></html>"
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
