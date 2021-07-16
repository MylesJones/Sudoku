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
    templateGame = Puzzle(int(n))
    data = dict(request.form)
    #update grid with new input
    game.grid, isOver = updateGrid(game, data)

    if isOver:
        if game.isLegal():
            return render_template("complete.html", n=n)
    return render_template("game.html", grid=game.grid, templateGrid = templateGame.grid)

def updateGrid(game, data):
    isOver = True
    for index, value in data.items():
        if not value == "":
            j,i = int(index[0]), int(index[2])
            game.grid[j][i] = value
        else:
            isOver = False

    return (game.grid, isOver)



if __name__ == "__main__":
    app.run(debug=True)
