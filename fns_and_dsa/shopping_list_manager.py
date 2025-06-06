shopping_list = []

def display_items():
    for item in shopping_list:
        print(item)

def add_to_list(product):
    shopping_list.append(product)
    display_items()

status = input("Do you want to add, remove, or display? ")

if status == "add":
    product = input("Enter the name of the product: ")
    add_to_list(product)

elif status == "remove":
    product = input("Enter the name of the product to remove: ")
    if product in shopping_list:
        shopping_list.remove(product)
    else:
        print("Product not found.")
    display_items()

elif status == "display":
    display_items()

else:
    print("Unknown request")
