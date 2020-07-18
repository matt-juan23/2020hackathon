from classes.Order import *

class Customer:
    def __init__(self, id, address, username, password):
        self.id = id
        self.address = address
        self.username = username
        self.password = password
        self.orders = []
    
    def placeOrder(self, item, amount):
        if amount > item.stock:
            print("Unable to get stock")
            return
        shop = item.shop
        order = Order(self, "date", shop)
        for _ in range(amount):
            order.addItem(item)
        item.removeStock(amount)
        #item.shop.addOrder(order)
        self.orders.append(order)
