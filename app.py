
import os
import signal
from flask import Flask, render_template, send_from_directory
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
    page = "<html><head>"
    page += "<link rel='stylesheet' href='static/styles/app.css') />"
    page += "</head><body><div class='container'><div class='animate one'><span>"
    page += generator.generate_buzz()
    page += "</span></div></div><div class ='container'>"
    page += "Version: 1.0"
    page += "</div></body></html>"
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
