from flask import Flask, jsonify, request
from product import Product
from cart import Cart
from order import Order



app = Flask(__name__)
my_cart = Cart()

order_history = []

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

@app.route("/order/create", methods=["POST"])
def order_create():
    data = request.get_json()

    customer_name = data.get("customer_name")

    if not customer_name:
        return jsonify({
            "error": "Customer name is required!"
        })

    if not my_cart.get_items():
        return jsonify({
            "error": "Your cart is empty!"
        }), 400

    total_price = 0

    for i in my_cart.get_items():
        total_price += i["product"].price * i["quantity"]

    new_order = Order(customer_name, my_cart)

    order_history.append(new_order)

    my_cart.clear_cart()

    return jsonify({
        "message": "Order created successfully!",
        "order": {
            "customer_name": customer_name,
            "total_price": new_order.total_price,
            "final_price": new_order.final_price
        }
    })

@app.route("/orders")
def get_orders():
    result = []

    for order in order_history:
        items = []

        for item in order.items:
            items.append({
                "name": item["product"].name,
                "price": item["product"].price,
                "quantity": item["quantity"]
            })

        result.append({
            "order_id": order.order_id,
            "customer_name": order.customer_name,
            "timestamp": order.timestamp,
            "items": items,
            "total_price": order.total_price,
            "discount_code": order.discount_code,
            "discount_percent": order.discount_percent,
            "final_price": order.final_price
        })

    return jsonify({
        "messsage": "Orders History",
        "orders": result
    })

    

if __name__ == "__main__":
    app.run(debug=True)
