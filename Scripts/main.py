import functions
def main():
    """
    -------------------------------------------------------
    Menu system to choose between functions.
    -------------------------------------------------------
    """
    choice = 0
    while choice != 6:
        print("\nMenu:")
        print("1. Retrieve a specific customer record")
        print("2. Find the customer with the highest balance")
        print("3. Append max number to file")
        print("4. Copy file contents")
        print("5. Copy first N lines from one file to another")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            with open("data/customers.txt", "r") as file:
                n = int(input("Enter record number: "))
                print(functions.customer_record(file, n))
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            pass
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

main()