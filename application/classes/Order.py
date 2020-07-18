import datetime
import utility

class Order:
    def __init__(self, customer, id, date, data):
        self.customer = customer
        self.id = id
        self.date = date
        self.totalPrice = 0
        self.status = PENDING
        self.items = []
        self.data = data
        self.rider = None

    def addRider(self, rider):
        self.rider = rider

    def addItem(self, item):
        self.items.append(item)
        self.totalPrice += item.price

    def sendOrder(self):
        self.status = INTRANSIT
        data.pending.remove(self)
        data.inTransit.append(self)


    def completeOrder(self):
        self.status = COMPLETE
        data.inTransit.remove(self)
        data.completed.append(self)
