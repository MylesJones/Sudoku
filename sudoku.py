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
    data = dict(request.form)
    game.updateGrid(data)  # update grid with new input, check if grid is full.
    game.isOver() #think maybe I should include isOver call into updateGrid method to abstract more.
    
    
    return render_template("game.html", game = game)

    

if __name__ == "__main__":
    app.run(debug=True)

