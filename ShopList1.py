#Objective: The aim of this assignment is to create a program that helps users make a shopping list.

#Task 1: Write a function that lets the user add items to a list.

shopping_list = []
def add_list():

    item = input("add item to the list:")
    shopping_list.append(item)

add_list()
print(shopping_list)

