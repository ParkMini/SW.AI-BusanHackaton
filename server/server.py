from flask import Flask, render_template, request
import os
import datetime as dt
from PIL import Image

app = Flask(__name__)

def write(content):
    f = open('./server/static/data.txt', 'w')
    f.write(f'{content}')
    f.close()

@app.route("/", methods=["GET"])
def main():
    return render_template("index.html")

@app.route("/noDetection", methods=["GET"])
def noDetection():
    write("Nothing. ")
    return "ok"

@app.route("/humanDetection/CSeungJoo", methods=["GET"])
def CSeungJoo():
    write("1 Friend(CSeungJoo), ")
    return "ok"

@app.route("/humanDetection/gunggme", methods=["GET"])
def gunggme():
    write("1 Friend(gunggme), ")
    return "ok"

@app.route("/crashDetection", methods=["GET"])
def crashDetection(): # 소리 재생만
    write("Use Yolo Model")
    return "ok"

@app.route("/busNumDetection/1008", methods=["GET"])
def busNumDetection1008():
    write("1 bus(1008), ")
    return "ok"

@app.route("/busNumDetection/518", methods=["GET"])
def busNumDetection518():
    write("1 bus(518), ")
    return "ok"

@app.route("/busNumDetection/3003", methods=["GET"])
def busNumDetection3003():
    write("1 bus(3003), ")
    return "ok"

@app.route("/busNumDetection/74", methods=["GET"])
def busNumDetection74():
    write("1 bus(74), ")
    return "ok"

@app.route("/busNumDetection/4101", methods=["GET"])
def busNumDetection4101():
    write("1 bus(4101), ")
    return "ok"

@app.route("/dotDetection", methods=["GET"])
def dotDetection():
    write("1 dot(안녕하세요), ")
    return "ok"

@app.route("/manyHumanDetection", methods=["GET"])
def manyHumanDetection(): # 소리 재생만
    write("Use Yolo Model")
    return "ok"

@app.route("/useDayDetection", methods=["GET"])
def useDayDetection(): # 소리 재생만
    write("1 SoBiGiHan(2023. 04. 28까지 11:18 321204), ")
    return "ok"


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host="0.0.0.0", port=80)