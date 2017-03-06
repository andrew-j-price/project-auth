from flask import Flask, render_template, request
from rps import RPS
rps = RPS()

app = Flask(__name__)


@app.route('/', strict_slashes=False, methods=["GET", "POST"])
def index():
    # If POST request, play the game
    if request.method == "POST":
        player_choice = request.form["my_selection"]
        computer_choice = rps.computer_choose()
        winner = rps.play(player_choice, computer_choice)
        match_output = rps.result_of(player_choice, computer_choice, winner)
        totals_output = rps.results_total()
        return render_template("index.html",
                               match_output=match_output,
                               totals_output=totals_output)
    # If GET request, reset the counters and start fresh
    rps.__init__()
    return render_template("index.html")
