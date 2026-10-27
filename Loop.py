def show_menu():
    print("\nWelcome to Taco Palace! Please view the menu below and make a selection")
    print("\nTaco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")


def get_item_price(choice):
    # Function to retrieve the price based on choice
    if choice == 1:
        return 2.50
    elif choice == 2:
        return 4.50
    elif choice == 3:
        return 3.75
    elif choice == 4:
        return 1.25
    else:
        return 0.0


def main():
    # Variables and list
    my_orders = []
    total_price = 0.0

    # Main loop that keeps running until user quits
    while True:
        show_menu()

        # Get user input as an integer
        choice = int(input("User entered: "))

        if choice == 1:
            print("You selected a Taco")
            my_orders.append("Taco")
            total_price += get_item_price(1)

        elif choice == 2:
            print("You selected a Burrito")
            my_orders.append("Burrito")
            total_price += get_item_price(2)

        elif choice == 3:
            print("You selected Nachos")
            my_orders.append("Nachos")
            total_price += get_item_price(3)

        elif choice == 4:
            print("You selected a Drink")
            my_orders.append("Drink")
            total_price += get_item_price(4)

        elif choice == 5:
            # Quit option breaks the loop
            break
        else:
            print("Invalid choice, please enter a number from 1 to 5.")

    # Print final results after loop ends
    print("\nYou ordered:", my_orders)
    print("Your total is $" + str(round(total_price, 2)))

main()