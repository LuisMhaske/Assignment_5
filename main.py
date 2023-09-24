"""
Task to create a program to manage accounting system for a warehouse.

Command and actions:
Balance -> Add or Subtract balance.
Sale -> should be able to sale a product i.e. if there is multiple product only one item should be sold
        and balance (+=) and quantity updated.
Purchase-> should add the item to the self and balance (-=) and quantity update(if item is already)
account -> display current balance.
list -> display total inventory
warehouse -> Search for product and display its status.
Review ->
end ->

"""
COMMAND_LIST = """List of commands
  - Balance
  - Sale
  - Purchase
  - Account
  - List
  - Warehouse
  - Review
  - End
"""
balance = 0
shelve = {}
while True:
    print(COMMAND_LIST)
    action = input("Select an option from above: ")
    action = action.casefold()

    if action == "end":
        print("Ending the instance")
        break

    elif action == "balance":
        add_sub_list = """Select an option
        - add
        - subtract
        - Type 'Stop' to return to main menu."""
        print(add_sub_list)
        option = input(": ")
        option = option.casefold()
        while True:
            if option == "stop":
                print("Returning to main menu.")
                break
            elif option == "add":
                addition = int(input("How much amount do you want to add?:"))
                balance += addition
                break
            elif option == "subtract":
                sub = int(input("How much amount do you want to deduct?:"))
                balance -= sub
                break
            else:
                print(f"{option} is incorrect, please enter a correct input")

    elif action == "sale":
        print("sale")

    elif action == "purchase":
        product_name = input("Please enter the name of the product purchased: ")
        product_price = int(input("Please enter the price of the product: "))

        if product_name not in shelve:
            shelve[product_name] = {"price": 0, "quantity": 0}

        shelve[product_name]["quantity"] += 1
        shelve[product_name]["price"] = product_price

        balance -= shelve[product_name]["price"]

    elif action == "account":
        print(f"Current Balance is: {balance}")

    elif action == "list":
        print("list")

    elif action == "warehouse":
        print("warehouse")

    elif action == "review":
        print("review")

    else:
        print(f"{action} is incorrect, please enter a correct input")
