import datetime
from classes.utility import *

class Order:
    def __init__(self, customer, date, shop):
        self.customer = customer
        self.date = date
        self.totalPrice = 0
        self.status = PENDING
        self.items = []
        self.shop = shop
        self.rider = None
        self.id = shop.getOrderId()

    def addRider(self, rider):
        self.rider = rider

    def addItem(self, item):
        self.items.append(item)
        self.totalPrice += item.price
        self.shop.addOrder(self)

    def sendOrder(self):
        self.status = INTRANSIT


    def completeOrder(self):
        self.status = COMPLETE
        self.shop.fulfilOrder(this)