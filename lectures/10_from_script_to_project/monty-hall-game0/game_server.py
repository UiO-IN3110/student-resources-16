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
    game_id = str(uuid.uuid4())
    winning = random.randint(1, 3)
    game_states[game_id] = {"winning": winning}

    return render_template('select.html', game_id=game_id)

@app.route('/reselect', methods=['POST'])
def reselect():

    # request.form contains all form parameters, like the selected door
    selected = int(request.form["door"])

    # request.args contains the URL parameters, like the game_id
    game_id = request.args.get("game_id")

    # Record some statistics
    game_states[game_id]["first_choice"] = selected

    winning = game_states[game_id]["winning"]

    # Open a random door (but not the winning nor the user-chosen door)
    opened = set([1, 2, 3])
    opened.discard(winning)
    opened.discard(selected)
    opened = random.choice(list(opened))

    return render_template("reselect.html", game_id=game_id, selected=selected, opened=opened)

@app.route('/final', methods=['POST'])
def final():

    # request.form contains all form parameters, like the selected door
    selected = int(request.form["door"])

    # request.args contains the URL parameters, like the game_id
    game_id = request.args.get("game_id")
    winning = game_states[game_id]["winning"]

    has_won = selected == winning

    # Record some statistics
    game_states[game_id]["changed_choice"] = selected != game_states[game_id]["first_choice"]
    game_states[game_id]["won"] = has_won

    return render_template("final.html", has_won=has_won, winning=winning)

@app.route('/statistics')
def statistics():
    changed_and_won = [e["won"] for e in game_states.values() if "changed_choice" in e and e["changed_choice"]]
    notchanged_and_won = [e["won"] for e in game_states.values() if "changed_choice" in e and not e["changed_choice"]]

    s1 = "Changed and won: {} out of {}".format(sum(changed_and_won), len(changed_and_won))
    s2 = "Not changed and won: {} out of {}".format(sum(notchanged_and_won), len(notchanged_and_won))
    return "<h1>Statistics</h1>{}</br>{}".format(s1, s2)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
