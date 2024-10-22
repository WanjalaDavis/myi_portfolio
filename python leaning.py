# Initialize counters for each item
gum_sold = 0
chocolate_sold = 0
popcorn_sold = 0
juice_sold = 0

# Start the vending machine loop
while True:
    # Display menu options
    print("\nVending Machine Options:")
    print("[1] Get gum")
    print("[2] Get chocolate")
    print("[3] Get popcorn")
    print("[4] Get juice")
    print("[5] Display total sold so far")
    print("[6] Quit")

    # Ask the user to select an option
    choice = input("Select an option (1-6): ")

    # Perform actions based on user choice
    if choice == "1":
        print("Here is your gum.")
        gum_sold += 1  # Increment gum counter

    elif choice == "2":
        print("Here is your chocolate.")
        chocolate_sold += 1  # Increment chocolate counter

    elif choice == "3":
        print("Here is your popcorn.")
        popcorn_sold += 1  # Increment popcorn counter

    elif choice == "4":
        print("Here is your juice.")
        juice_sold += 1  # Increment juice counter

    elif choice == "5":
        # Display the total number of each item sold
        print(f"\nTotal Sold So Far:")
        print(f"{gum_sold} items of gum sold")
        print(f"{chocolate_sold} items of chocolate sold")
        print(f"{popcorn_sold} items of popcorn sold")
        print(f"{juice_sold} items of juice sold")

    elif choice == "6":
        print("Thank you! The program will now terminate.")
        break  # Exit the loop and terminate the program

    else:
        # Invalid option
        print("Error, options 1-6 only!")
