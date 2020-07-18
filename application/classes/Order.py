import datetime
import data

class Order:
    def __init__(self, customer, id, date):
        self.customer = customer
        self.id = id
        self.date = date
        self.totalPrice = 0
        self.status = "pending"
        self.items = []

    def addItem(self, item):
        self.items.append(item)
        self.totalPrice += item.price

    def sendOrder(self):
        self.status = "in-transit"


    def completeOrder(self):
        self.status = "complete"
