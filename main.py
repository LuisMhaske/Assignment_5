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
  - Balance - To add or deduct current account balance
  - Sale - To make a sale of product
  - Purchase - To purchase a new product
  - Account - Shows the current balance
  - List - Shows the total inventory
  - Warehouse - search for a specific product to check availability.
  - Review - History
  - End - to exit.
"""
balance = 0
shelve = {}
history = []
while True:
    print(COMMAND_LIST)
    # try:
    action = input("Select an option from above list of commands: ")
    # except EOFError:
    #     print("Reached the end")
    action = action.casefold()
    history.append(f"Task performed {action}")

    if action == "end":
        print("Ending the instance")
        break

    elif action == "balance":
        add_sub_list = """Select an option
        - Add
        - Subtract
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
                history.append(f"Added {addition} amount  to the current balance")
                break
            elif option == "subtract":
                sub = int(input("How much amount do you want to deduct?:"))
                balance -= sub
                history.append(f"Remove {sub} amount to the current balance")
                break
            else:
                print(f"{option} is incorrect, please enter a correct input")

    elif action == "sale":
        product_name = input("Please enter the name of the product: ")
        product_quantity = int(input("Please enter the quantity:  "))
        if product_name not in shelve or shelve[product_name]["quantity"] < 1:
            print(f"Transaction Error!! Product {product_name} is out of stock in our warehouse.")
            continue

        shelve[product_name]["quantity"] -= product_quantity
        balance += shelve[product_name]["price"] * product_quantity
        print(f"{product_quantity} {product_name} have been sold.")
        history.append(f"Sold Product detail: Name: {product_name} | Quantity: {product_quantity} ")

    elif action == "purchase":
        product_name = input("Please enter the name of the product to purchase: ")
        product_price = float(input("Please enter the current price per piece: "))
        product_quantity = int(input("Please enter the quantity:  "))
        total_price = product_price * product_quantity
        print(total_price)
        if product_name not in shelve:
            shelve[product_name] = {"price": 0.0, "quantity": 0}

        if balance >= total_price:
            shelve[product_name]["quantity"] += product_quantity
            shelve[product_name]["price"] = product_price
            balance -= total_price
            print(f"{product_name} has been added to the shelve.")
            history.append(f"Product added to shelve: Name: {product_name} | Price: {product_price} | "
                           f"Quantity: {product_quantity} ")
        else:
            print("Unable to purchase, please check account balance")

    elif action == "account":
        print(f"Current Account Balance is: {balance}")

    elif action == "list":
        print("Product name | Pricing | Quantity")
        for product, product_stats in shelve.items():
            print(f"{product:12.12s} | {product_stats['price']:7} | {product_stats['quantity']:7}")

    elif action == "warehouse":
        product_name = input("Please enter the name of product to check availability: ")
        if product_name in shelve and shelve[product_name]["quantity"] > 0:
            print(f"{product_name} is available in the warehouse ")
        else:
            print(f"{product_name} is out of stock ")
        history.append(f"Searched for {product_name}.")

    elif action == "review":
        print("Review recorded operations:")
        from_idx = input("Enter 'from' index (or press Enter for the beginning): ")
        to_idx = input("Enter 'to' index (or press Enter for the end): ")
        try:
            from_idx = int(from_idx) \
                if from_idx \
                else 0
            to_idx = int(to_idx) \
                if to_idx \
                else len(history)
        except ValueError:
            print("Invalid indices. Please enter valid numbers.")
            continue
        # Check if the indices are out of range
        if from_idx < 0 or from_idx >= len(history) or to_idx < 0 or to_idx > len(history) or from_idx > to_idx:
            print("Invalid indices. Please enter valid indices within the range.")
            continue
        # Display recorded operations within the specified range
        for idx in range(from_idx, to_idx):
            print(f"{idx + 1}: {history[idx]}")

    else:
        print(f"{action} is incorrect, please enter a correct input")
        continue
