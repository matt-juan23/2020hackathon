from utility import *

class Shop:
    def __init__(self, id, name, contact, address):
        self.id=id
        self.name=name
        self.contact=contact
        self.address=address
        self.orders = []
        self.items = []

    def addOrder(self, order):
        self.orders.append(order)

    def getLists(self):
        dash = {}
        dash["pending"] = self.getPending()
        dash["in-transit"] = self.getInTransit()
        dash["completed"] = self.getCompleted()

        return dash

    def getPending(self):
        pending = []
        for x in self.orders:
            if x.status == PENDING:
                pending.append(x)
        return pending

    def getInTransit(self):
        intransit = []
        for x in self.orders:
            if x.status == INTRANSIT:
                intransit.append(x)
        return intransit

    def getCompleted(self):
        completed = []
        for x in self.orders:
            if x.status == COMPLETED:
                completed.append(x)
        return completed
    
    def addItem(self, item):
        self.items.append(item)
    
    def fulfilOrder(self, order):
        self.orders.remove(order)

    def findOrder(self, order):
        for i, x in enumerate(self.orders):
            if x == order:
                return i

    def removeItem(self, item):
        self.items.remove(item)

 

    


    

