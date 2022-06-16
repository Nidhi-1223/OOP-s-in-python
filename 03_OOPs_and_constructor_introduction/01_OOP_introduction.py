class  Item:        #initializing the class
    def calculate_total_price(self,price,quantity):
        return price*quantity
        

item1 = Item()      #creating an instance (item1) of class (Item)

item1.name = "Phone"    #creating attributes for that instance
item1.price = 100
item1.quantity = 50

item1.total_price = item1.calculate_total_price(item1.price, item1.quantity)        #calling the method
print(item1.total_price)

'''
alternate method for line 12 and 13
print(item1.calculate_total_price(item1.price, item1.quantity))
'''

item2 = Item()      #creating an instance (item1) of class (Item)2
item2.name = "Phone"    #creating attributes for that instance
item2.price = 1000
item2.quantity = 30

item2.total_price = item2.calculate_total_price(item2.price, item2.quantity)        #calling the method
print(item2.total_price)


# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))

# random_string = "ojfwidjf"
# print(random_string.upper())        #.upper() is a method that will print the uppercase of the letter