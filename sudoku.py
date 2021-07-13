from flask import Flask, render_template, request
from puzzle import *

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        game = Puzzle()
        return render_template("index.html", grid = game.grid)
    if request.method == 'POST':
        data = request.form
        #update grid with new input
        print(data)
        return render_template("index.html", grid=game.grid)

if __name__ == "__main__":
    app.run(debug=True)
