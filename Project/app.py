from collections import namedtuple

from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)

urls = []


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", urls=urls)


@app.route("/add_url", methods=["POST"])
def add_url():
    urls = request.form["url"]

    urls.append(Url(url))
    return redirect(url_for("home"))

