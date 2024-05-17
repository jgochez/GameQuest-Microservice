from datetime import datetime
import time
import json

cart_games = []


def checkout():
    total_price = render_cart("checkout")
    print("-" * 30)
    print(f"(Step 2) Total:     ${round(total_price, 2)}\n")
    pay = input("(Step 3) PAY(y/n): ")
    if pay == "y":
        verify = input("Are you sure?(y/n): ")
        if verify == "y":
            print("Thank you for paying!")
            print(f"Confirmation: Payment of ${round(total_price, 2)} on {datetime.now()}")
            time.sleep(2)
            print("\nReturning to Cart..")

            empty_cart()
            return "fill"
    else:
        print("Returning to Cart...")
        return "render"


def empty_cart():
    # Get saved games from JSON
    with open("games_list_saved.json", 'r') as in_file:
        saved_games = json.load(in_file)

        saved_games.clear()

    # Add saved games to JSON
    with open("games_list_saved.json", 'w') as out_file:
        json.dump(saved_games, out_file, indent=4)

    cart_games.clear()


def render_cart(status):
    empty = True
    count = 1
    total = 0
    if status == "checkout":
        # Empty cart
        for game in cart_games:
            empty = False
            print(f"    ({count}) {game['title']} -- {game['price']}")
            count += 1
            total += float(game["price"])

    elif status == "render":
        # Render cart
        for game in cart_games:
            empty = False
            print(f"    ({count}) {game['title']} -- {game['price']}")
            count += 1
            total += float(game["price"])

    elif status == "fill":
        # Fill cart
        with open("games_list_saved.json", 'r') as file:
            saved_games = json.load(file)

        for s_game in saved_games:
            empty = False
            for c_game in cart_games:
                if s_game["title"] == c_game["title"]:
                    cart_games.remove(s_game)
            cart_games.append(s_game)
            print(f"    ({count}) {s_game['title']} -- {s_game['price']}")
            count += 1
            total += float(s_game["price"])

    if empty:
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
            return
        else:
            print("Invalid input, try again.")


def menu(status):
    print("*" * 52 + "\n" + " " * 17 + "GAMEQUEST APP" + "\n" + "*" * 52)
    print("-" * 36 + "CHECKOUT CART---")
    print("-" * 52)
    print("\n(Step 1) Complete Your Cart:")
    render_cart(status)
    print("-" * 52)
    print("(a)Edit\n(b)Checkout\n(c)Refresh")
    print("~" * 52 + "\n(i) BROWSE " + "(ii) SAVED " + "(iii) CHECKOUT " + "(q) EXIT")


def user_input():
    while True:
        res = input("*" * 50 + "\n" + "Finalize Cart: ")
        if res == "a":
            remove_from_cart()
            cart("render")
        elif res == "b":
            status = checkout()
            cart(status)
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
