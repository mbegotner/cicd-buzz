
import os
import signal
from flask import Flask
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = "<html><head>"
    page += "<link rel='stylesheet' href={{ url_for('static' filename='static/styles/app.css') }}/>"
    page += "</head><body><div class='container'><div class='animate one'><span>"
    page += generator.generate_buzz()
    page += "</span></div></div><div class ='container'>"
    page += "Version: 2.0"
    page += "</div></body></html>"
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
