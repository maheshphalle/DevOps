
### This is practical #####

####################

from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [
    {
        'id': 100,
        'title': 'Mobile',
        'description': 'This is Cell phones category',
        'done': False
    },
    {
        'id': 200,
        'title': 'Television',
        'description': 'This is a Smart TV category',
        'done': False
    }
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({'products': products})

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product is None:
        abort(404)
    return jsonify({'product': product})

if __name__ == '__main__':
    app.run(debug=True)
