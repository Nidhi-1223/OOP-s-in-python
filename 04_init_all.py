# Here we will create a list that has all the instances that were created throughout the execution of the program

class  Item:        

    pay_rate = 0.8          #this is a class attribute
    all = []                #initializing a list
    def __init__(self,name:str,price:int,quantity:int,non_mandatory_parameter=0):

        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"

        #assign to self object
        self.name = name
        self.price = price 
        self.quantity = quantity
        
        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price*self.quantity  

    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    def __repr__(self):                                     #this is a magic attribute that allows the programmer to specify the representation of instances in the console
        return f"item('{self.name}',{self.price}, {self.quantity})"

item1 = Item("Phone", 100, 5)      
item2 = Item("Laptop", 1000, 3)    
item3 = Item("Cable", 10, 5)  
item4 = Item("Mouse", 50, 5)      
item5 = Item("Keyboard", 75, 5)    

print(Item.all)

print("\n\n##########################################################\n\n")

for instance in Item.all:
    print(instance.name)