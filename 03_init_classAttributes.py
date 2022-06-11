class  Item:        #initializing the class

    pay_rate = 0.8          #this is a class attribute
    def __init__(self,name:str,price:int,quantity:int,non_mandatory_parameter=0):

        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"

        self.name = name
        self.price = price 
        self.quantity = quantity
        self.non_mandatory_paramter = non_mandatory_parameter


    def calculate_total_price(self):
        return self.price*self.quantity  

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        

item1 = Item("Phone", 100, 50)      #creating an instance (item1) of class (Item)
item1.apply_discount()
print(item1.price)


item2 = Item("Laptop", 1000, 30)      #creating an instance (item1) of class (Item)
item2.pay_rate = 0.7                    #modifying the class attribute for a specific instance
item2.apply_discount()
print(item2.price)

print("######################################################")

print(Item.pay_rate)
print(item1.pay_rate)                   #here the program checked all the attributes of instance "item1" at the instance level. It didnot find any attribute named "pay_rate" that's why it moved on to the class level
print(item2.pay_rate)

print("########################################################")

print(Item.__dict__)        #__dict__ is a magic attribute that gives all the attributes of that particular class or instance in the form of a dictonary
print(item1.__dict__)       #you wont see pay_rate as __dict__ will only list the attributes at the instance level
print(item2.__dict__)