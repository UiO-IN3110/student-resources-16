# File: game_server.py
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def root():
        return """<h1>Welcome to the <b>magic door</b> game!</h1>
<a href="/select/">Launch game</a>
"""

@app.route("/select/")
def new():
    return render_template('select2.html')

if __name__ == "__main__":
    app.run(debug=True)
