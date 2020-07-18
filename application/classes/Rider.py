class Rider:
    def __init__(self, id, suburb):
        self.id = id
        self.suburb = suburb
        self.orders = []

    def acceptOrder(self, order):
        self.orders.append(order)
        order.addRider(this)
    
    def addOrder(self, order):
        self.order.append(order)

    def completeOrder(self, order):
        self.orders.remove(order)
        order.completeOrder()