class  Item:        #initializing the class
    def __init__(self,name:str,price:int,quantity:int,non_mandatory_parameter=0):

        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"

        # print(f"I AM CREATED!: {name}")
        self.name = name
        self.price = price 
        self.quantity = quantity
        self.non_mandatory_paramter = non_mandatory_parameter


    def calculate_total_price(self):
        return self.price*self.quantity
        

item1 = Item("Phone", 100, 50)      #creating an instance (item1) of class (Item)

item2 = Item("Laptop", 1000, 30)      #creating an instance (item1) of class (Item)
item2.has_numpad = False                #creating an attribute that is only valid for a single instance i.e. a laptop
# print(item1.name)
# print(item2.name)

# print(item1.price)
# print(item2.price)

# print(item1.quantity)
# print(item2.quantity)

# print(item1.non_mandatory_paramter)
# print(item2.non_mandatory_paramter)


# print(type(item2.has_numpad))

print(item1.calculate_total_price())
print(item2.calculate_total_price())