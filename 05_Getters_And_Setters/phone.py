import csv
from item import Item

class Phone(Item):                      #created a new class called 'Phone' inherited from the class 'Item'
    def __init__(self,name:str,price:int,quantity:int, broken_phones=0):
        #call to super function to have access to all attributes/methods
        super().__init__(name, price, quantity)

        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to 0"

        #assign to self object
        self.broken_phones = broken_phones