from flask import Flask, render_template, request
from puzzle import *
import random

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    n = random.randrange(10000)
    return render_template("index.html", n = n)
    
#test with /1643 -- 781349562   395276418   246815379   469182753   123567894   857493621   918654237   534721986   672938145

@app.route("/game/<n>", methods=['GET', 'POST'])
def game(n):
    game = Puzzle(int(n))
    templateGame = Puzzle(int(n))
    data = dict(request.form)
    #update grid with new input, check if grid is full.
    game.grid, isFull = updateGrid(game, data)



    if isFull:
        if game.isLegal():
            return render_template("complete.html", n=n)
    
    return render_template("game.html", grid=game.grid, templateGrid = templateGame.grid)

    

def updateGrid(game, data):
    isFull = True
    for index, value in data.items():
        if not value == "":
            j,i = int(index[0]), int(index[2])
            game.grid[j][i] = value
        else:
            isFull = False

    return (game.grid, isFull)



if __name__ == "__main__":
    app.run(debug=True)
