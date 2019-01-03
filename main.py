# Title Screen.

print("| ======================================================================================================= |")
print("|  ____ _____ __  __ ____  _____  ____   _     _     _  __  _  ____    _____  ____   ____   _     __  __  |")
print("| / (__`| () )\ \/ /(_ (_`|_   _|/ () \ | |__ | |__ | ||  \| || ===|   | () )| ===| / () \ | |__ |  \/  | |")
print("| \____)|_|\_\ |__|.__)__)  |_| /__/\__\|____||____||_||_|\__||____|   |_|\_\|____|/__/\__\|____||_|\/|_| |")
print("| ======================================================================================================= |")
print("                                                                                                       ")
print("                               Use the space bar to progress in the game.                                    ")
print("                                                                                                       ")

next_line = ""

# Opening text.
welcome = input("Welcome to the Crystalline Realm! ")
while True:
    if welcome == " ":
        break
    else:
        welcome = input("Welcome to the Crystalline Realm! ")

# INTRODUCTION:

# Naming:
name = input("Hello Mystic! You have stumbled upon the Crystalline Realm! May I ask, what is your name? ")

while True:
    yes_no_name = input(f'Ah, your name is {name}, did I get that right? [y/n] ')
    if yes_no_name == "y" or "Y" or "yes" or "YES":
        break
    if yes_no_name == "n" or "N" or "no" or "NO":
        name = input("What is your name?")

# Dialogue
player_element_before = input(
    "In this realm, every mystic has a birthstone or crystal, their crystals are infused with elemental magic, their stone determines what abilities they are able to wield and bend. It seems like you don't have one... ")
while True:
    if player_element_before == " ":
        break
    else:
        player_element_before = input(
            "In this realm, every mystic has a birthstone or crystal, their crystals are infused with elemental magic,their stone determines what abilities they are able to wield and bend. It seems like you don't have one... ")
player_element_before2 = input(
    "...luckily for you, I brought some stones with me, pick one, choose wisely... ")
while True:
    if player_element_before2 == " ":
        break
    else:
        player_element_before2 = input(
            "...luckily for you, I brought some stones with me, pick one, choose wisely... ")

# Crystal Selection
while True:
    player_crystal = input("  Jade ~ Rose-quartz ~ Sapphire ~ Celestite ~ Garnet ~ Tanzanite ~ Diamond ~ Opal ")

    # Wind and Earth abilities
    if player_crystal == "Jade" or "jade":
        yes_no_jade = input(
            "Jade: a light green stone engraved with carvings of dragons, swirls, and spirals. Choose this crystal? [y/n] ")
        if yes_no_jade == "Y" or "y" or "yes" or "YES":
            pass
        if yes_no_jade == "N" or "n" or "no" or "NO":
            yes_no_jade = ""

        # Fairytale/Charm abilities
    if player_crystal.upper == "ROSE-QUARTZ" or "ROSE QUARTZ":
        yes_no_rosequartz = input(
            "Rose-quartz: a light pink opaque crystal, it somehow looks... cute. Choose this crystal? [y/n] ")
        if yes_no_rosequartz == "Y" or "y" or "yes" or "Yes" or "YES":
            pass
        if yes_no_rosequartz == "N" or "n" or "no" or "No" or "NO":
            yes_no_rosequartz == ""
            player_element = input("  Jade ~ Rose-quartz ~ Sapphire ~ Celestite ~ Garnet ~ Tanzanite ~ Diamond ~ Opal ")

    # Storm abilities (electric and water)
    # Cosmic abilities
    # Tamer (Summon animals) and morphing abilities
    # Dark/Necromancy/Demonic abilities
    # Light/Metal abilities
    # Fire and Ice abilities
