class Customer:
    def __init__(self, id, address, username, password, orders):
        self.id = id
        self.address = address
        self.username = username
        self.password = password
        self.orders[] = orders
    
    def placeOrder(self, order):
        self.orders.append(order)
