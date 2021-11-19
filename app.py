from flask import Flask, jsonify, render_template
from utils import run_bot
import json
import os

app = Flask(__name__)

base_url = "https://vindictus.nexon.net"
ext = "/news/updates"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def main():
    try:
        run_bot(base_url, ext)
        return jsonify("Success")
    except:
        return jsonify("Failure")



if __name__ == "__main__":
    app.run(debug=False)