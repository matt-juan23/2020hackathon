class Item:

    def __init__(self, id, price, description, stock):
        self.id = id
        self.price = price
        self.description = description
        self.stock = stock
    
    def removeStock(amount):
        self.stock = self.stock - amount

    def addStock(amount):
        self.stock = self.stock + amount
        