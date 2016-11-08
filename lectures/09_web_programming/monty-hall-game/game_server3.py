# File: game_server.py
from flask import Flask
from flask import render_template
from flask import request
import random
import uuid

app = Flask(__name__)

@app.route("/")
def root():
        return """<h1>Welcome to the <b>magic door</b> game!</h1>
<a href="/select/">Launch game</a>
"""

@app.route("/select/")
def new():
    return render_template('select.html')

@app.route('/reselect', methods=['POST']) 
def reselect():           

    # request.form contains all form parameters, like the selected door
    selected = int(request.form["door"])

    return render_template("reselect1.html", selected=selected)


if __name__ == "__main__":
    app.run(debug=True)
