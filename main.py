data = {}

while True:

    print("\n1. Add product")
    print("2. View product")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # ADD PRODUCT
    if choice == "1":

        name = input("Enter product name: ")
        category = input("Enter category: ")
        price = input("Enter price: ")
        quantity = input("Enter quantity: ")

        data[name] = {
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity
        }

        print("Product added successfully")


    # VIEW PRODUCT
    elif choice == "2":

        if not data:
            print("No products available")

        else:
            for name, product in data.items():
                print("\nProduct:", name)
                print("Category:", product["category"])
                print("Price:", product["price"])
                print("Quantity:", product["quantity"])


    # SEARCH PRODUCT
    elif choice == "3":

        search_name = input("Enter product name to search: ")

        if search_name in data:
            print("\nProduct found")
            print("Name:", data[search_name]["name"])
            print("Category:", data[search_name]["category"])
            print("Price:", data[search_name]["price"])
            print("Quantity:", data[search_name]["quantity"])

        else:
            print("Product not found")


    # UPDATE PRODUCT
    elif choice == "4":

        update_name = input("Enter product name to update: ")

        if update_name not in data:
            print("Product not found")

        else:
            category = input("Enter new category: ")
            price = input("Enter new price: ")
            quantity = input("Enter new quantity: ")

            data[update_name]["category"] = category
            data[update_name]["price"] = price
            data[update_name]["quantity"] = quantity

            print("Product updated successfully")


    # DELETE PRODUCT
    elif choice == "5":

        delete_name = input("Enter product name to delete: ")

        if delete_name not in data:
            print("Product not found")

        else:
            del data[delete_name]
            print("Product deleted successfully")


    # EXIT
    elif choice == "6":

        print("Program ended")
        break

    else:
        print("Enter a valid option")