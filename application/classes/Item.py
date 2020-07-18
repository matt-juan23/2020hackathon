class Item:

    def __init__(self, id, price, name, description, stock, shop):
        self.id = id
        self.price = price
        self.name = name
        self.description = description
        self.stock = stock
        self.shop = shop
    
    def removeStock(self, amount):
        self.stock = self.stock - amount

    def addStock(self, amount):
        self.stock = self.stock + amount
    
