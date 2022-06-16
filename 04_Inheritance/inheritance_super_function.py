import csv

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
        return f"{self.__class__.__name__}('{self.name}',{self.price}, {self.quantity})"

class Phone(Item):                      #created a new class called 'Phone' inherited from the class 'Item'
    def __init__(self,name:str,price:int,quantity:int, broken_phones=0):
        #call to super function to have access to all attributes/methods
        super().__init__(name, price, quantity)

        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to 0"

        #assign to self object
        self.broken_phones = broken_phones

       

phone1 = Phone("jscPhonev10", 500, 5,1)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev10", 700, 5,1)

print("-----------------------------------------------------------------")
print(Item.all)
print(Phone.all)