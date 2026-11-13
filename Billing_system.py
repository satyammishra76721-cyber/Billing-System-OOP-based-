
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_price(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []
        self.tax_rate = 18

    def add_product(self, product):
        self.products.append(product)

    def display_bill(self):
        print("\n========== FINAL BILL ==========")
        print(f"{'Name':<15}{'Price':<10}{'Quantity':<10}{'Total':<10}")
        print("-------------------------------------------")

        subtotal = 0

        for product in self.products:
            total = product.calculate_price()
            subtotal += total

            print(f"{product.name:<15}{product.price:<10}{product.quantity:<10}{total:<10}")

        tax = subtotal * self.tax_rate / 100
        grand_total = subtotal + tax

        print("-------------------------------------------")
        print(f"Subtotal: Rs. {subtotal:.2f}")
        print(f"Tax (18%): Rs. {tax:.2f}")
        print(f"Grand Total: Rs. {grand_total:.2f}")
        print("===========================================")


# Main Program
bill = Bill()

n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nProduct {i + 1}")

    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    product = Product(name, price, quantity)
    bill.add_product(product)

bill.display_bill()
