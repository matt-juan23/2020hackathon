from classes.Customer import *
from classes.Item import *
from classes.Data import *
from classes.Order import *
from classes.Rider import *
from classes.Shop import *

c = Customer(1, "a", "a", "a")

s = Shop(1, "b", "b", "b")

i = Item(1, 4, "pole", 10, s)
i2 = Item(2, 4, "thign", 12, s)

s.addItem(i)
s.addItem(i2)

c.placeOrder(i, 1)

print(s.orders)
print(s.items)

