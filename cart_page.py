from datetime import datetime
import time
import json

cart_games = []


def checkout():
    total_price = render_cart("checkout")
    print("-" * 30)
    print(f"(Step 2) Total:     ${total_price}\n")
    pay = input("(Step 3) PAY(y/n): ")
    if pay == "y":
        verify = input("Are you sure?(y/n): ")
        if verify == "y":
            print("Thank you for paying!")
            print(f"Confirmation: Payment of ${total_price} on {datetime.now()}")
            time.sleep(2)
            print("\nReturning to Cart..")

            # Get saved games from JSON
            with open("games_list_saved.json", 'r') as in_file:
                saved_games = json.load(in_file)

                saved_games.clear()

            # Add saved games to JSON
            with open("games_list_saved.json", 'w') as out_file:
                json.dump(saved_games, out_file, indent=4)

            cart("fill")
    else:
        print("Returning to Cart...")
        cart("fill")


def render_cart(status):
    empty = 0
    count = 1
    total = 0
    if status == "checkout":
        # Empty cart
        for game in cart_games:
            print(f"    ({count}) {game['title']} -- {game['price']}")
            count += 1
            total += float(game["price"])

        cart_games.clear()

    elif status == "render":
        # Render cart
        for game in cart_games:
            empty += 1
            print(f"    ({count}) {game['title']} -- {game['price']}")
            count += 1
            total += float(game["price"])

    elif status == "fill":
        # Fill cart
        with open("games_list_saved.json", 'r') as file:
            saved_games = json.load(file)

        for game in saved_games:
            empty += 1
            cart_games.append(game)
            print(f"    ({count}) {game['title']} -- {game['price']}")
            count += 1
            total += float(game["price"])
    if empty == 0:
        print("\nCart is empty.\n")
    return total


def remove_from_cart():
    while True:
        title = input("Which game?: ")
        for game in cart_games:
            if title == game["title"]:
                cart_games.remove(game)
        another = input("Another?(y/n): ")
        if another == "y":
            continue
        elif another == "n":
            break
        else:
            print("Invalid input, try again.")


def menu(status):
    print("*" * 52 + "\n" + " " * 17 + "GAMEQUEST APP" + "\n" + "*" * 52)
    print("-" * 36 + "CHECKOUT CART---")
    print("-" * 52)
    print("\n(Step 1) Complete Your Cart:")
    render_cart(status)
    print("Edit/Checkout/Exit?:" + "\n(a)Edit\n(b)Checkout\n(c)Refresh")
    print("~" * 52 + "\n(i) BROWSE " + "(ii) SAVED " + "(iii) CART " + "(q) EXIT")


def user_input():
    while True:
        res = input("*" * 50 + "\n" + "Finalize Cart: ")
        if res == "a":
            remove_from_cart()
            cart("render")
        elif res == "b":
            checkout()
        elif res == "c":
            cart("fill")
        elif res == "q":
            print("\nSuccessfully Exit.")
            exit(0)
        else:
            print("Error: Invalid input, try again.\n")


def cart(status):
    while True:
        menu(status)
        user_input()


if __name__ == "__main__":
    cart("fill")
