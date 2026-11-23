print("Welcome to the Fantasy Item Shop!")

player_name = input("What is your name? ")
player_gold = 100
inventory = []

print(f"\nHello {player_name}! You have {player_gold} gold.")

shop_items = ["Sword", "Shield", "Potion", "Bow"]

print("\nItems available in the shop:")

for item in shop_items:
    print(item)

while True:
    print("\n=== Fantasy Item Shop ===")
    print("1. Buy Sword (50 gold)")
    print("2. Buy Shield (40 gold)")
    print("3. Buy Potion (20 gold)")
    print("4. Buy Bow (60 gold)")
    print("5. View Inventory")
    print("6. Exit Shop")

    choice = input("\nWhat would you like to do? ")

    match choice:
        case "1":
            if player_gold >= 50:
                player_gold -= 50
                inventory.append("Sword")
                print("\nYou bought a Sword!")
                print(f"Remaining gold: {player_gold}")
            else:
                print("\nYou don't have enough gold!")

        case "2":
            if player_gold >= 40:
                player_gold -= 40
                inventory.append("Shield")
                print("\nYou bought a Shield!")
                print(f"Remaining gold: {player_gold}")
            else:
                print("\nYou don't have enough gold!")

        case "3":
            if player_gold >= 20:
                player_gold -= 20
                inventory.append("Potion")
                print("\nYou bought a Potion!")
                print(f"Remaining gold: {player_gold}")
            else:
                print("\nYou don't have enough gold!")

        case "4":
            if player_gold >= 60:
                player_gold -= 60
                inventory.append("Bow")
                print("\nYou bought a Bow!")
                print(f"Remaining gold: {player_gold}")
            else:
                print("\nYou don't have enough gold!")

        case "5":
            if len(inventory) == 0:
                print("\nYour inventory is empty!")
            else:
                print("\nYour inventory:")

                for item in inventory:
                    print(f"- {item}")

        case "6":
            print(f"\nThanks for visiting, {player_name}!")
            print(f"You have {player_gold} gold left.")
            break

        case _:
            print("\nInvalid option! Please choose 1-6.")
