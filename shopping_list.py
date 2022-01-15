# Create a new empty list 
shopping_list = []
# Create function that declares a parameter named item
def add_to_list(item):
# add the item to the list
    shopping_list.append(item)
    # notify the user the item was added and current number of items
    print("Added! List had {} items.".format(len(shopping_list)))


# user should be able to ask for help to understand program
def show_help():
    print("What should we pickup at the store? ")
    print("""
    Enter 'DONE' to stop adding items to the shopping list.
    Enter 'HELP' for help.
    """)

show_help()
# promp user to add a grocery item to lis or view the list
while True:
    new_item = input("> ")

# user should be able to state when they are done adding items to the list
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
# Call add_to_list with new_item
    add_to_list(new_item)