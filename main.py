from flask import Flask, request, jsonify
from src.models import product  # call model file
from flask_cors import CORS  # avoid cors errors if called from frontend

app = Flask(__name__)
CORS(app)

product = product.Product()


# product routes
@app.route('/products', methods=['GET'])
def get_all_products():
    return jsonify(product.find({})), 200


@app.route('/products/<string:product_id>', methods=['GET'])
def get_products_by_id(product_id):
    return product.find_by_id(product_id), 200


@app.route('/products', methods=['POST'])
def create_products_by_id():
    if request.method == "POST":
       product_id = request.json['product_id']
       name = request.json['name']
       created_by = request.json['created_by']
       updated_by = request.json['updated_by']
       response = product.create({'product_id': product_id, 'name': name, 'created_by': created_by, 'updated_by': updated_by})
       return response, 201


@app.route('/products/<string:product_id>/', methods=['PUT'])
def update_products_by_id(product_id):
    if request.method == "PUT":
        product_id = request.json['product_id']
        name = request.json['name']
        response = product.update(product_id, {'product_id': product_id, 'name': name})
        return response, 201


@app.route('/products/<string:product_id>/', methods=['DELETE'])
def delete_tasks(product_id):
    if request.method == "DELETE":
        product.delete(product_id)
        return "Record Deleted"


if __name__ == '__main__':
    app.run(debug=True)
