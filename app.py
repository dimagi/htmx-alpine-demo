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
    if request.method == "POST":
        template = "item.html"
        item = update_item(item_id, request)
    else:
        template = "edit_item.html"
        item = get_item(item_id)

    return render_template(template, item=item)


@app.route("/new", methods=["POST"])
def new_item():
    item = {"id": len(items) + 1, "name": "New Item"}
    items.insert(0, item)
    return render_template("item.html", item=item)


def get_item(item_id):
    return next((item for item in items if item["id"] == item_id), None)


def update_item(item_id, request):
    new_name = request.form.get("name")
    item_to_edit = get_item(item_id)
    if new_name and item_to_edit:
        item_to_edit["name"] = new_name
    return item_to_edit


if __name__ == "__main__":
    app.run(debug=True)
