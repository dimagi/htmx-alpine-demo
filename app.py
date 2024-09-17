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


@app.route("/edit/<int:item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    item_to_edit = get_item(item_id)
    return render_template("edit_item.html", item=item_to_edit)


def get_item(item_id):
    return next((item for item in items if item["id"] == item_id), None)


if __name__ == "__main__":
    app.run(debug=True)
