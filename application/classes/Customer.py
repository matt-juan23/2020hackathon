from classes.Order import *

class Customer:
    def __init__(self, id, address, username, password):
        self.id = id
        self.address = address
        self.username = username
        self.password = password
        self.orders = []
    
    def placeOrder(self, item, amount):
        order = Order(self, "date", item.shop)
        order.addItem(item)
        item.shop.addOrder(order)
        self.orders.append(order)
