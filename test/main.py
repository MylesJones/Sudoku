from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)


# @app.route('/')
# def index():
#     return f'Method used: {request.method}'


# @app.route('/bacon', methods = ['GET', 'POST'])
# def bacon():
#     if request.method == 'POST':
#         return "You are using POST"
#     else:
#         return "You are probably using GET"


# @app.route('/tuna')
# def tuna():
#     return '<h2>Tuna is bad</h2>' #It is bad practice to put html in the return of the method.

# @app.route('/profile/<user>')
# def profile(user):
#     return f"<h1>Hello {user}</h1>"

# @app.route('/post/<int:postID>')
# def post(postID):
#     return f"<h1>PostID is {postID}</h1>"





if __name__ == "__main__":
    app.run(debug=True)
