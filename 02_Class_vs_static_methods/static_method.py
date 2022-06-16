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
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('../object oriented programming in python/Class_vs_static_methods/items.csv','r') as f:            #here, we are reading the csv file
            reader = csv.DictReader(f)              #here, we are representing the csv file as a dictonary
            items = list(reader)                    #here, we are getting the list of dictonaries

        # for item in items:
        #     print(item)                             #this will print each the item in the csv file as a dictonary. It doesnot create instances

    #SO NOW TO CREATE INSTANCES: 
        for item in items:
            Item(
                name=item.get('name'),
                price= float(item.get('price')),
                quantity= int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        '''
        Here we will count out the float that are point zero
        i.e., 5.0, 10.0
        '''
        if isinstance(num, float):              #counts out the float that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    def __repr__(self):                                     #this is a magic attribute that allows the programmer to specify the representation of instances in the console
        return f"item('{self.name}',{self.price}, {self.quantity})" 

print(Item.is_integer(89.0)) 