#task 2: Include a function to remove items from the list.

shopping_list = ['milk', 'bananas', 'bread', 'eggs']
def remove_list():

    item = input("remove item from the list:")
    shopping_list.remove(item)

remove_list()
print(shopping_list)

