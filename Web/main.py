from flask import Flask, render_template, redirect, url_for
from database import get_orders

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for("orders"))


@app.route("/orders")
def orders():
    data = get_orders()
    return render_template("index.html", orders=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
