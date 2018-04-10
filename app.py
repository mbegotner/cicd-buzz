
import os
import signal
from flask import Flask, url_for
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = "<html><head><link rel='stylesheet' href='{{ url_for('static',filename='styles/main.css') }}'></head><body><div class='container'><div class='animate one'><span>"
    page += generator.generate_buzz()
    page += "</span></div></div>"
    page += "<div class='container'>Version: 1.0</div>"
    page += "</body></html>"
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
