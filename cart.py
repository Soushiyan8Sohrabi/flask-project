class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity=1):
        for item in self.items:
            if item["product"] == product:
                item["quantity"] += 1
                return

        item = {"product": product, "quantity": quantity}
        self.items.append(item)

    def remove_product(self, product):
        if product in self.items:
            self.items.remove(product)
        else:
            print(f"{product.name} is not on the list")

    def get_total(self):
        total = 0
        for item in self.items:
            total += item["product"].price * item["quantity"]
        return total
    
    def apply_discount(self, percent):
        total_price = self.get_total()
        final_price = int(total_price * (1 - percent / 100))
        return final_price
    
    def clear_cart(self):
        self.items.clear()

    def get_items(self):
        return self.items.copy()
        
    
    def show_cart(self):
        for item in self.items:
            print(f"{item['product'].name} | Price: {item['product'].price} | Quantity: {item['quantity']}")


