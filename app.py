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
    template = "edit_item.html"

    if request.method == "POST":
        template = "item.html"
        update_item(item_id, request)

    item_to_edit = get_item(item_id)
    return render_template(template, item=item_to_edit)


@app.route("/alpine")
def alpine_index():
    return render_template("alpine/index.html", items=items)


@app.route("/alpine/update", methods=["POST"])
def alpline_update_item():
    item_id = int(request.form["id"])
    
    update_item(item_id, request)
    
    return jsonify(success=True)


def get_item(item_id):
    return next((item for item in items if item["id"] == item_id), None)


def update_item(item_id, request):
    new_name = request.form.get("name")
    item_to_edit = get_item(item_id)
    if new_name and item_to_edit:
        item_to_edit["name"] = new_name


if __name__ == "__main__":
    app.run(debug=True)

