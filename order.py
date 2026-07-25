import uuid
import datetime
import json

class Order:
    def __init__(self, customer_name, cart, discount_code="", discount_percent=0):
        self.customer_name = customer_name
        self.items = cart.get_items()      
        self.total_price = cart.get_total()
        self.order_id = str(uuid.uuid4())
        self.timestamp = str(datetime.datetime.now())
        
        self.discount_code = discount_code
        self.discount_percent = discount_percent
        
        self.final_price = self.total_price - (self.total_price * self.discount_percent / 100)
    
    def show_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Date: {self.timestamp}")
        print(f"Customer: {self.customer_name}")
        
        for item in self.items:
            print(f"""{item['product'].name} | Price : {item['product'].price} | Quantity : {item['quantity']}""")
        
        if self.discount_percent > 0:
            print(f"Discount Code: {self.discount_code}")
            print(f"Discount: {self.discount_percent}%")


        print(f"Total Price: {int(self.total_price)}")
        print(f"Final Price: {int(self.final_price)}")


def save_order_to_json(order):
    file_name = "orders.json"

    order_data = {
        "Order_ID": order.order_id,
        "timestamp": order.timestamp,
        "customer_name": order.customer_name,
        "items": [],
        "total_price": order.total_price,
        "discount_code": order.discount_code,
        "discount_percent": order.discount_percent,
        "final_price": int(order.total_price - (order.total_price * order.discount_percent / 100))
    }
    
    for item in order.items:
        order_data["items"].append({
            "name": item["product"].name,
            "price": item["product"].price,
            "quantity": item["quantity"]
        })

    try:
        with open(file_name, "r") as file:
            orders = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        orders = []

    orders.append(order_data)

    with open(file_name, "w") as file:
        json.dump(orders, file, indent=4)
    