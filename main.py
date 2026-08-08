from past_frontend.product import Product
from past_frontend.cart import Cart
from past_frontend.order import Order, save_order_to_json

p1 = Product("Iphone 16", 1000, 0)
p2 = Product("S24 FE", 500, 5)
p3 = Product("Macbook", 2000, 13)

products = [p1, p2, p3]
my_cart = Cart()

orders = []


discount_codes = {
    "OFF10": 10,
    "OFF20": 20
}

while True:
    try:
        print("=== Our Online Shop ===")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. View Shopping Cart")
        print("4. Order Placement")
        print("5. Recent Orders")
        print("6. Exit")

        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            for i, product in enumerate(products, start=1):
                print(f"{i}. {product}")

        elif choice == 2:
            for i, product in enumerate(products, start=1):
                print(f"{i}. {product}")

            choose_p = int(input("Enter product number: "))

            if 1 <= choose_p <= len(products):
                product = products[choose_p - 1]

                if product.reduce_stock():
                    my_cart.add_product(product)
                    print("Product added to cart.")
                else:
                    print(product.is_available())
            else:
                print("Invalid product number.")

        elif choice == 3:
            if not my_cart.items:
                print("Shopping cart is empty.")
            else:
                print("=== Shopping Cart ===")
                my_cart.show_cart()
                print(f"Total: {my_cart.get_total()} USD")

        elif choice == 4:
            if not my_cart.items:
                print("Your shopping cart is empty!")
            else:
                while True:
                    name = input("Please, enter your name: ").strip()

                    if name:
                        break

                    print("Customer name cannot be empty.")
                
                discount = input("Do you have a discount code? (Press Enter if not): ").upper()

                if discount in discount_codes:
                    discount_percent = discount_codes[discount]
                else:
                    discount_percent = 0
                    print("No discount code applied.")

                new_order = Order(name, my_cart, discount, discount_percent)
                orders.append(new_order)
                save_order_to_json(new_order)
                

                print("Your order has been placed successfully.")
                print("=== Last Order ===")

                new_order.show_order()
                
                my_cart.clear_cart()
        
        elif choice == 5:
            print("=== Orders History ===")
            
            if not orders:
                print("No orders found.")
            else:
                for i, order in enumerate(orders, start=1):
                    print(f"Order {i}")
                    order.show_order()
        
        elif choice == 6:
            print("Goodbye! 👋")
            break

        else:
            print("Invalid option.")

    except ValueError:
        print("Please enter a valid number.")