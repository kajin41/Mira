from flask import Flask, render_template, request, redirect


app = Flask(__name__)


nav_items = ['app', 'join', 'about', 'partners', 'contact']


@app.route('/')
def index():
    return render_template("home3.html", title="Mira Saves", nav_items=nav_items)


if __name__ == '__main__':
    app.run()
