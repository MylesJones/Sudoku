from flask import Flask, render_template, request
from puzzle import *
import random

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    n = random.randrange(10000)
    return render_template("index.html", n = n)
    


@app.route("/game/<n>", methods=['GET', 'POST'])
def game(n):
    game = Puzzle(int(n))
    data = request.form
    #update grid with new input
    print(data)
    return render_template("game.html", grid=game.grid)




if __name__ == "__main__":
    app.run(debug=True)
