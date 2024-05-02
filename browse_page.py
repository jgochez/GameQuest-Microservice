import time
import json

# ssh -i ~/.ssh/id_rsa -T git@github.com

render_games = []


def add_to_saved():
    while True:
        res = input("Save the game/s?(y/n): ")
        if res == "y":
            # Get saved games from JSON
            with open("games_list_saved.json", 'r') as in_file:
                saved_games = json.load(in_file)

            for game in render_games:
                saved_games.append(game)

            for game in render_games:
                render_games.remove(game)

            # Add saved games to JSON
            with open("games_list_saved.json", 'w') as out_file:
                json.dump(saved_games, out_file, indent=4)

            break

        elif res == "n":
            print("Returning to Browse Page..")
            for game in render_games:
                render_games.remove(game)
            time.sleep(2)

            break
        else:
            print("Invalid input, try again.")


def normal_filter():
    # Display message and prompt
    print("Filter Options..")
    print("Press <enter> to skip..")
    time.sleep(2)

    print("*" * 15)
    render_all = input("Render all?(y/n): ")
    print("*" * 15)

    # Get games from JSON
    with open("games_list_catalog.json", 'r') as file:
        game_list = json.load(file)

    # Render entire list of games
    if render_all == "y":
        start_y = time.time()

        count = 1
        for game in game_list:
            render_games.append(game)
            print(f"({count}) {game['title']} -- {game['price']}")
            count += 1

        end_y = time.time()
        print(f"\nRendered in {round(end_y - start_y, 4)} seconds.")

    # Render games based of filter
    elif render_all == "n":
        print("*" * 15)
        console = input("Console: ")
        developer = input("Developer: ")
        game_series = input("Game Series: ")
        release_year = input("Release Year: ")
        print("*" * 15)

        start_n = time.time()

        for game in game_list:
            if console == game["console"] and game not in render_games:
                render_games.append(game)
            if developer == game["developer"] and game not in render_games:
                render_games.append(game)
            if game_series == game["game series"] and game not in render_games:
                render_games.append(game)
            if release_year == game["release year"] and game not in render_games:
                render_games.append(game)

        count = 1
        for game in render_games:
            print(f"({count}) {game['title']} -- {game['price']}")
            count += 1

        end_n = time.time()
        print(f"\nRendered in {round(end_n - start_n, 4)} seconds.")


def menu():
    print("*" * 52 + "\n" + " " * 17 + "GAMEQUEST APP" + "\n" + "*" * 52)
    print("-" * 35 + "BROWSE CATALOG---")
    print("-" * 52)
    print("(a) Normal Filter (Default)")
    print(" |RECOMMENDED: Search with only one field required.|\n")
    print("(b) Uber Filter (Comprehensive)")
    print(" |WARNING: For comprehensive filtering use the     |\n"
          " |Uber Search filter, packed with over 100 filter  |\n"
          " |options, so be mindful of your time!             |\n")
    print("(c) Quick Search (Faster)")
    print(" |NEW!!!: Quick Search uses browsing history for   |\n"
          " |its algorithm and may be less accurate due to it.|")
    print("~" * 52)
    print("(i) BROWSE " + "(ii) SAVED " + "(iii) CART " + "(q) EXIT")


def user_input():
    while True:
        res = input("*" * 50 + "\n" + "Choose Filter: ")
        if res == "a":
            normal_filter()
            break
        elif res == "b":
            pass
        elif res == "c":
            pass
        elif res == "q":
            print("\nSuccessfully Exit.")
            exit(0)
        else:
            print("Error: Invalid input, try again.\n")


def browse():
    while True:
        menu()
        user_input()
        add_to_saved()


if __name__ == "__main__":
    browse()
