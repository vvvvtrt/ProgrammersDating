from flask import Flask, jsonify, request
import json
import random

app = Flask(__name__)


def Read():
    try:
        with open("data/InquiryData.json", "r") as ReadFile:
            data = json.load(ReadFile)
            return data
    except:
        return None

def Write(arr, mess):

    data = {
        "code": arr,
        "me": mess
    }
    try:
        with open("data/InquiryData.json", "w") as WriteFile:
            json.dump(data, WriteFile)
        return True
    except:
        return False

@app.route('/')
def main():
    with open("main.html", "rb") as fin:
        return fin.read()


@app.route('/search')
def search():
    with open("search.html", "rb") as fin:
        g = Read()
        i = random.randint(0, len(g["me"]) - 1)
        s = fin.read()[2:]
        s = s[:841] + g["me"][i].encode('utf-8') + s[841:]
        s = s[:542] + g["code"][i].encode('utf-8') + s[542:]
        return s


@app.route('/create')
def create():
    with open("create.html", "rb") as fin:
        return fin.read()


@app.route('/handle_data', methods=('GET', 'POST'))
def handle_data():
    if len(str(request.form['me'])) == 0 and len(str(request.form['programm'])) == 0:
        with open("errorcreate.html", "rb") as fin:
            return fin.read()
    else:
        g = Read()
        Write(g["code"] + [request.form['programm']], g["me"] + [request.form['me']])
        with open("successfullycreate.html", "rb") as fin:
            return fin.read()


@app.route("/image/fon12.png")
def background():
    with open("image/fon12.png", "rb") as fin:
        return fin.read()


@app.route("/image/fon2.png")
def background2():
    with open("image/fon2.png", "rb") as fin:
        return fin.read()

@app.route("/image/fon3.png")
def background3():
    with open("image/fon3.png", "rb") as fin:
        return fin.read()

@app.route("/image/fon4.png")
def background4():
    i = random.randint(0, 1)
    if i:
        with open("image/fon4.png", "rb") as fin:
            return fin.read()
    else:
        with open("image/fon42.png", "rb") as fin:
            return fin.read()

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
