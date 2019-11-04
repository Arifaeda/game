print("| ======================================================================================================= |")
print("|  ____ _____ __  __ ____  _____  ____   _     _     _  __  _  ____    _____  ____   ____   _     __  __  |")
print("| / (__`| () )\ \/ /(_ (_`|_   _|/ () \ | |__ | |__ | ||  \| || ===|   | () )| ===| / () \ | |__ |  \/  | |")
print("| \____)|_|\_\ |__|.__)__)  |_| /__/\__\|____||____||_||_|\__||____|   |_|\_\|____|/__/\__\|____||_|\/|_| |")
print("| ======================================================================================================= |")
print("                                                                                                       ")
print("                                 Press enter to progress through the game.                                    ")
print("                                                                                                       ")

opening = input("*** Regaining consciousness, your entire being is immersed in a brilliant show\n"
                "of lights and gentle colors. Your vision is overwhelmed, but a faint voice catches\n"
                "your attention. You listen closely, as you close your eyes tightly... ***")

# INTRO DIALOGUE =======================================================================================================
lighttext1 = input("???: I hope this worked...")
lighttext2 = input("???: Is anyone there?")
lighttext3 = input("???: Hello? Can you hear me?")
lighttext4 = input("???: Can you see me?\n")

thought1 = input(
    "*** You slowly try to open your eyes once more, but even squinting, the mysterious \n"
    "light blinds you still. ***\n")

lighttext5 = input("???: Huh, I guess not...")
lighttext6 = input("???: Anyhow, there is no time to lose.")
lighttext7 = input(
    "???: This realm is sinking into grave darkness, they are in need of a great hero to \n"
    "prevent such a fate...")
lighttext8 = input("???: The imbalance of light and dark is spinning out of control, \n"
                       "you are this realm's last hope.")

# NAMING ===============================================================================================================
name = input("???: Hero, what is your name?\n"
             "==========ENTER NAME BELOW==========\n")
while True:
    yes_no_name = input(f'???: So, your name is {name}, is that correct? [y/n]\n')
    if yes_no_name == "y":
        break
    elif yes_no_name == "n":
        name = input("What is your name?\n"
                     "==========ENTER NAME BELOW==========\n")
    else:
        yes_no_name = input(f'???: So, your name is {name}, is that correct? [y/n]')

lighttext9 = input(
    "???: So, in this realm, every mystic has a crystal assigned to them at birth, their crystals are infused with \n"
    "elemental magic, their stone determines what abilities they are able to wield and bend. It seems like you \n"
    "don't have one yet...")
lighttext10 = input("???: ...I have brought before you many mystical crystals "
                        "from all over the Crystalline Realm...")
lighttext11 = input("???: ...just choose the one that calls out to you most...")
lighttext12 = input("???: ...please choose wisely...\n")

# CRYSTAL SELECTION ====================================================================================================
# TO BE IMPLEMENTED BY DIRECTION OF CREATOR
while True:
    player_crystal = input("================== CRYSTAL CHOICES: ==================\n"
                           "                  Jade ~ Rose-quartz\n"
                           "                 Sapphire ~ Celestite\n"
                           "                   Garnet ~ Tanzanite\n"
                           "                    Diamond ~ Opal\n"
                           "======================================================\n")

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
