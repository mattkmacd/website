from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/americanpie")
def americanpie():
    return render_template("americanpie.html")


@app.route("/data")
def data():
    return render_template("data.html")


@app.route("/moneybb")
def moneybb():
    return render_template("moneybb.html")


@app.route("/happyhours")
def happyhours():
    return render_template("happyhours.html")


@app.route("/seniordesign")
def seniordesign():
    return render_template("seniordesign.html")
