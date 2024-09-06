#Task 3: Add a function that prints out the entire list in a formatted way.


shopping_list = ['milk', 'bananas', 'bread', 'eggs']
def add_list():

    item = input("add item to the list:")
    shopping_list.append(item)

add_list()
print(f'\n{shopping_list}', )

