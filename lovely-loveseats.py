class Furniture:
    '''An inventory item with a name, description, and price.'''
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return self.name + '.' + '\n' + self.description

class ShoppingCart:
    '''A container to track and add up a customer's purchases.'''
    sales_tax = 0.088
    
    def __init__(self, customer_id=""):
        self.customer_id = customer_id
        self.contents = []
        self.total = 0
        self.taxes = 0

    def add_item(self, item):
        self.contents.append(item)
        self.total += item.price
        self.taxes += item.price * self.sales_tax

    def __str__(self):
        result = ""
        for item in self.contents:
            result += str(item) + '\n\n'
        return result

    def print_receipt(self):
        print(self.customer_id, "Items:\n")
        print(self, end="")
        print(self.customer_id, "Total:")
        print(f"${self.total + self.taxes:.2f}")

    
if __name__ == '__main__':
    lovely_loveseat = Furniture("Lovely Loveseat",
    "Tufted polyester blend on wood. 32 inches high x 40 inches wide \
x 30 inches deep. Red or white.", 254.00)
    stylish_settee = Furniture("Stylish Settee",
    "Faux leather on birch. 29.50 inches high x 54.75 inches wide \
x 28 inches deep. Black.", 180.50)
    luxurious_lamp = Furniture("Luxurious Lamp",
    "Glass and iron. 36 inches tall. Brown with cream shade.", 52.15)
    inventory = {"Lovely Loveseat" : lovely_loveseat,
                 "Stylish Settee" : stylish_settee,
                 "Luxurious Lamp" : luxurious_lamp,
                 }
    customer_one = ShoppingCart("Customer One")
    customer_one.add_item(inventory["Lovely Loveseat"])
    customer_one.add_item(inventory["Luxurious Lamp"])
    customer_one.print_receipt()
    
