shopping_list = []

def add_item():
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"'{item}' has been addedto the shopping list.")

def remove_item():
    item = input("Enter the item name to remove")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from shopping list.")
    else:
        print(f"'{item}' is not found in the shopping list.")

def view_list():
    if shopping_list:
        print("\nCurrent Shopping List:")
        for item in shopping_list:
            print(f" - {item}")
    else:
        print("\nThe Shopping List is empty.")

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("\Enter your choice(1 - 4): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice  == "3":
            view_list()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()