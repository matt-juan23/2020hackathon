class Customer:
    def __init__(self, id, address, username, password):
        self.id = id
        self.address = address
        self.username = username
        self.password = password
        self.orders[] = []
    
    def placeOrder(self, order):
        self.orders.append(order)
