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
    
    def addItem(self, item):
        self.items.append(item)
    
    def fulfilOrder(self, order):
        i=self.findOrder(order)
        self.orders[i].setFulfilled

    def findOrder(self, order):
        for i, x in enumerate(self.orders):
            if x == order:
                return i

    def removeItem(self, item):
        self.items.remove(item)

 

    


    

