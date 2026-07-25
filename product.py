class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def __str__(self):
        return f"{self.name} - Price$ : {self.price} - Stock : {self.stock}"
    
    def single_discount(self):
        self.price = int(self.price * 0.9)

    def is_available(self):
        if self.stock > 0 :
            return "Available"
        else:
            return "Unavailable"
        
    def total_value(self):
        return self.price * self.stock
    
    def reduce_stock(self):
        if self.stock > 0:
            self.stock -= 1
            return True
        return False

