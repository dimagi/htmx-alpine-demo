from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"},
]


@app.route("/")
def index():
    return render_template("index.html", items=items)


if __name__ == "__main__":
    app.run(debug=True)
