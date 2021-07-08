from flask import Flask, render_template
from puzzle import *

app = Flask(__name__)

@app.route("/")
def index():
    game = Puzzle()
    game.genNewPuzzle()
    return render_template("index.html", grid = game.grid)

if __name__ == "__main__":
    app.run(debug=True)
