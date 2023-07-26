from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import datetime as dt
from PIL import Image

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return render_template("index.html")


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host="0.0.0.0", port=80)