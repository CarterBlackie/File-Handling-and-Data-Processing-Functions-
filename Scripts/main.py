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
            with open("data/customers.txt", "r") as file:
                print(functions.customer_best(file))
        elif choice == "3":
            with open("data/numbers.txt", "r+") as file:
                print("Appended max number:", functions.append_max_num(file))
        elif choice == "4":
            with open("data/source.txt", "r") as src, open("data/destination.txt", "w") as dest:
                functions.file_copy(src, dest)
                print("File copied successfully.")
        elif choice == "5":
            with open("data/source.txt", "r") as src, open("data/destination.txt", "a") as dest:
                n = int(input("Enter number of lines to copy: "))
                functions.file_copy_n(src, dest, n)
                print(f"Copied {n} lines successfully.")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

main()

print("Hello")