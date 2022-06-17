from cgi import print_arguments
from operator import itemgetter
from item import Item
from phone import Phone

# Item.instantiate_from_csv()
# print(Item.all)

item1 = Item("MyItem", 750,6)
item1.name = "OtherItem"                #gonna throw an error when name is a read only property, we used the setter method so the users can still modify the read only properties

print(item1.name)

# print(item1.read_only_name)

# # item1.read_only_name = "i wanna overwrite this property"