# File: game_server.py
from flask import Flask
from flask import render_template
from flask import request
import random
import uuid

app = Flask(__name__)

game_states = {}  # Maps game id to winner door

@app.route("/")
def root():
        return """<h1>Welcome to the <b>magic door</b> game!</h1>
<a href="/select/">Launch game</a>
"""

@app.route("/select/")
def new():
    game_id = str(uuid.uuid4())  # Creates a unique identifer for this game
    winning = random.randint(1, 3)  # Define a winning door
    game_states[game_id] = winning

    return render_template('select.html', game_id=game_id)

@app.route('/reselect', methods=['POST']) 
def reselect():           

    # request.form contains all form parameters, like the selected door
    selected = int(request.form["door"])
    
    # request.args contains the URL parameters, like the game_id
    game_id = request.args.get("game_id")
    winning = game_states[game_id]

    # Open a random door (but not the winning nor the user-chosen door)
    opened = set([1, 2, 3])
    opened.discard(winning)
    opened.discard(selected)
    opened = random.choice(list(opened))

    return render_template("reselect.html", game_id=game_id, selected=selected, opened=opened)

if __name__ == "__main__":
    app.run(debug=True)
