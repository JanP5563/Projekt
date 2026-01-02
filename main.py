from flask import Flask
from flask import render_template
from flask import request

# Nie wiem czy potrzebujemy SQLAlchemy, najwyżej potem usuniesz stąd i z requirements

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("main.html")

if __name__ == "__main__":
        app.run(
        "127.0.0.1",
        5001,
        debug=True
    )




