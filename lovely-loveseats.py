class Furniture:
    '''An inventory item with a name, description, and price.'''
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return self.name + '.' + '\n' + self.description
    
if __name__ == '__main__':
    lovely_loveseat = Furniture("Lovely Loveseat",
    "Tufted polyester blend on wood. 32 inches high x 40 inches wide \
x 30 inches deep. Red or white.", 254.00)
    print(lovely_loveseat)
    stylish_settee = Furniture("Stylish Settee",
    "Faux leather on birch. 29.50 inches high x 54.75 inches wide \
x 28 inches deep. Black.", 180.50)
    print(stylish_settee)
    luxurious_lamp = Furniture("Luxurious Lamp",
    "Glass and iron. 36 inches tall. Brown with cream shade.", 52.15)
    print(luxurious_lamp)
