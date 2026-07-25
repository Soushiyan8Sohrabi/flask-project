from flask import Flask, jsonify, request
from product import Product
from cart import Cart

app = Flask(__name__)
my_cart = Cart()

products = [
    Product("keyboard", 2000, 10),
    Product("mouse", 1000, 5),
]

@app.route("/products")
def get_products():
    result = []
    for p in products:
        result.append({
            "name": p.name,
            "price": p.price,
            "stock": p.stock
        })

    return jsonify({
        "message": "Here are your products!",
        "products": result
    })

@app.route("/about")
def about():
    return jsonify({
        "message": "Welcome to our online store! We offer wide variety of products with extremely low prices."
    })

@app.route("/cart/add", methods=["POST"])
def add_product():
    data = request.get_json()
    product_name = data.get("name")
    quantity = data.get("quantity", 1)

    for p in products:
        if p.name == product_name:
            my_cart.add_product(p, quantity)

            return jsonify({
                "message": f"{p.name} added to cart successfully!"
            }), 200

    return jsonify({
        "error": "Product not found!"
    }), 404

@app.route("/cart")
def get_cart():
    result = []

    for item in my_cart.get_items():
        result.append({
            "name": item["product"].name,
            "price": item["product"].price,
            "quantity": item["quantity"]
        })

    return jsonify({
        "message": "Your cart items.",
        "cart": result
    })


if __name__ == "__main__":
    app.run(debug=True)
