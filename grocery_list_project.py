# GROCERY LIST
budget = int(input("Enter your total budget: "))

list_items = ["Chicken", "Milk", "Cheese", "Rice", "Yogurt", "Butter", "Chocolate", "Vegetables", "Mint", "Coriander Leaves", "Bread"]

print("Final checking of items")             
print(f"this is the list items: {list_items}")

choice = input("Does this list look good? (yes/no): ")

if choice == "yes":
    print("Great job buddy")
else:
    additional_items = input("Enter the name of your additional items: ")
    list_items.append(additional_items)
    
    additional_items_price = int(input("Enter the price of your additional items: "))
    new_budget = budget + additional_items_price
    
    print(f"Your new budget is: {new_budget}")
    print("Are you fine with the new budget?")
    print("Say yes if you are or else please remove the additional items")

print("Happy Shopping")