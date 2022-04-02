# imports
import json, random, requests
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

jinx = open('data.json')
jinx.data = json.load(jinx)
img = random.choices(jinx.data, k=1)
rnd = img[0]['url']
@app.route("/")
def home():
    return render_template('index.html', rnd=rnd)

@app.route("/imgs/", methods=["GET"])
def fetch_imgs():
    if request.method == "GET":
        if len(jinx.data) > 0:
            return jsonify(jinx.data)
        else:
            return('API is empty')

@app.route("/imgs/<int:id>/", methods=["GET"])
def fetch_specific_img(id: str):
    for url in jinx.data:
        if url['id'] == id:
            return jsonify(url)
        pass

@app.route("/imgs/random/", methods=["GET"])
def fetch_random_img():
    if request.method == "GET":
        img = random.choices(jinx.data, k=1)
        return jsonify(img)

if __name__ == '__main__':
    app.run(debug = True)