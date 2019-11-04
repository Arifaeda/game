
print("| ======================================================================================================= |")
print("|  ____ _____ __  __ ____  _____  ____   _     _     _  __  _  ____    _____  ____   ____   _     __  __  |")
print("| / (__`| () )\ \/ /(_ (_`|_   _|/ () \ | |__ | |__ | ||  \| || ===|   | () )| ===| / () \ | |__ |  \/  | |")
print("| \____)|_|\_\ |__|.__)__)  |_| /__/\__\|____||____||_||_|\__||____|   |_|\_\|____|/__/\__\|____||_|\/|_| |")
print("| ======================================================================================================= |")
print("                                                                                                       ")
print("                                 Press enter to progress through the game.                                    ")
print("                                                                                                       ")

while True:
    yes_no_name = input(f'???: So, your name is {name}, is that correct? [y/n]\n')
    if yes_no_name == "y":
        break
    elif yes_no_name == "n":
        name = input("What is your name?\n"
                     "==========ENTER NAME BELOW==========\n")
    else:


    # Wind and Earth abilities
    if player_crystal == "Jade":
        yes_no_jade = input(
            "Jade: a light green stone engraved with carvings of dragons, swirls, \n"
            "and spirals. Choose this crystal? [y/n] ")
        if yes_no_jade == "y":
            pass
        else:
            pass

    # Fairytale/Charm abilities
    if player_crystal == "Rose-Quartz":
        yes_no_rosequartz = input(
            "Rose-Quartz: a light pink opaque crystal, it somehow looks... cute. Choose this crystal? [y/n] ")
        if yes_no_rosequartz == "y":
            pass
        else:
            pass

    # Storm abilities (electric and water)
    # Cosmic abilities
    # Tamer (Summon animals) and morphing abilities
    # Dark/Necromancy/Demonic abilities
    # Light/Metal abilities
    # Fire and Ice abilities
