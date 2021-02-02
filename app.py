from flask import Flask, render_template
from random import choice

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("hra.html")


@app.route("/kamen")
def kamen():
    ja = "kámen"
    vysledek = choice(["kámen", "nůžky", "papír"])
    if vysledek == "kámen":
        skore = "Remíza"
    if vysledek == "nůžky":
        skore = "Prohrál jste."
    if vysledek == "papír":
        skore = "Vyhrál jste."
    return render_template("hra.html", vysledek=vysledek, ja=ja, skore=skore)


@app.route("/nuzky")
def nuzky():
    ja = "nůžky"
    vysledek = choice(["kámen", "nůžky", "papír"])
    if vysledek == "kámen":
        skore = "Prohrál jste."
    if vysledek == "nůžky":
        skore = "Remíza."
    if vysledek == "papír":
        skore = "Vyhrál jste."
    return render_template("hra.html", vysledek=vysledek, ja=ja, skore=skore)


@app.route("/papir")
def papir():
    ja = "papír"
    vysledek = choice(["kámen", "nůžky", "papír"])
    if vysledek == "papír":
        skore = "Remíza."
    if vysledek == "nůžky":
        skore = "Vyhrál jste."
    if vysledek == "kámen":
        skore = "Prohrál jste."
    return render_template("hra.html", vysledek=vysledek, ja=ja, skore=skore)


if __name__ == "__main__":
    app.run()
