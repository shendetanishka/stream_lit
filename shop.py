from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Sample data for clothing and furniture items
items = {
    'clothing': [
        {'id': 1, 'name': 'T-Shirt', 'image': 'static/images/tshirt.png'},
        {'id': 2, 'name': 'Jeans', 'image': 'static/images/jeans.png'},
    ],
    'furniture': [
        {'id': 1, 'name': 'Chair', 'image': 'static/images/chair.png'},
        {'id': 2, 'name': 'Table', 'image': 'static/images/table.png'},
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)
