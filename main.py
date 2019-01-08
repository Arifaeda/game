# Title Screen.

print("| ======================================================================================================= |")
print("|  ____ _____ __  __ ____  _____  ____   _     _     _  __  _  ____    _____  ____   ____   _     __  __  |")
print("| / (__`| () )\ \/ /(_ (_`|_   _|/ () \ | |__ | |__ | ||  \| || ===|   | () )| ===| / () \ | |__ |  \/  | |")
print("| \____)|_|\_\ |__|.__)__)  |_| /__/\__\|____||____||_||_|\__||____|   |_|\_\|____|/__/\__\|____||_|\/|_| |")
print("| ======================================================================================================= |")
print("                                                                                                       ")
print("                               Use the space bar to progress in the game.                                    ")
print("                                                                                                       ")







# Opening text.
welcome = input("Welcome to the Crystalline Realm! ")
while True:
    if welcome == " ":
        break
    else:
        welcome = input("Welcome to the Crystalline Realm! ")
    

# INTRODUCTION:

# Introduction dialogue


lightdialogue1 = input("???: I hope this worked...")
while True:
  if lightdialogue1 == " ":
    break
  else:
    lightdialogue1 = input("???: I hope this worked...")


lightdialogue2 = input("???: Is anyone there?")
while True:
  if lightdialogue2 == " ":
    break
  else:
    lightdialogue2 = input("???: Is anyone there?")


lightdialogue3 = input("???: Hello? Can you hear me?")
while True:
  if lightdialogue3 == " ":
    break
  else:
    lightdialogue3 = input("???: Hello? Can you hear me?")


lightdialogue4 = input("???: Can you see me?")
while True:
  if lightdialogue4 == " ":
    break
  else:
    lightdialogue4 = input("???: Can you see me?")


thought1= input("*you slowly try to open your eyes, but even squinting, the mysterious bright white light is blinding")
while True:
  if thought1 == " ":
    break
  else:
    thought1 = input("*you slowly try to open your eyes, but even squinting, the mysterious bright white light is blinding")


lightdialogue5= input("???: Huh, I guess not...")
while True:
  if lightdialogue5 == " ":
    break
  else:
    lightdialogue5 = input("???: Huh, I guess not...")


lightdialogue6= input("???: Anyhow, there is no time to lose.")
while True:
  if lightdialogue6 == " ":
    break
  else:
    lightdialogue6 = input("???: Anyhow, there is no time to lose.")


lightdialogue7= input("???: This realm is sinking into grave darkness, they are in need of a great hero to prevent such a fate...")
while True:
  if lightdialogue7 == " ":
    break
  else:
    lightdialogue7 = input("???: This realm is sinking into grave darkness, they are in need of a great hero to prevent such a fate...")


lightdialogue8= input("???: The imbalance of light and dark is spinning out of control, you are this realm's last hope.")
while True:
  if lightdialogue8 == " ":
    break
  else:
    lightdialogue8 = input("???: The imbalance of light and dark is spinning out of control, you are this realm's last hope.")


    
    
    
# Naming:
name = input("???: Hero, what is your name?")
while True:
  yes_no_name = input(f'???: So, your name is {name},is that correct?[y/n]')
  if yes_no_name == "y" or "Y" or "yes" or "YES":
    break
  #very bugged from here on out
  if yes_no_name == "n" or "N" or "no" or "NO":
    name = input("What is your name?")
  else:
    yes_no_name = input(f'???: So, your name is {name},is that correct?[y/n]')


#Name Easter Eggs
"""if name == "Lunaarii" or "lunaarii" or "Satanmyninjas" or "satanmyninjas" :
  #print(name)
  nameeasteregg1_1 = input("???: An excellent name...")
  while True:
    if nameeasteregg1_1 == " ":
      break
    else:
      nameeasteregg1_1 = input("???: An excellent name...")
  
    
  nameeasteregg1_2 = input("???: ...in some strange way, it sounds...familiar...")
  while True:
    if nameeasteregg1_2 == " ":
      break
    else:
      nameeasteregg1_2 = input("???: ...in some strange way, it sounds...familiar...")
 
    
  nameeasteregg1_3 = input("???: Ah, nevermind... just forget I said anything...")
  while True:
    if nameeasteregg1_3 == " ":
      break
    else:
      nameeasteregg1_3 = input("???: Ah, nevermind... just forget I said anything...")
elif name != "Lunaarii" or "lunaarii" or "Satanmyninjas" or "satanmyninjas" :
    pass"""



  

# Dialogue
lightdialogue9 = input("???: So, in this realm, every mystic has a crystal assigned to them at birth, their crystals are infused with elemental magic, their stone determines what abilities they are able to wield and bend. It seems like you don't have one yet...")
while True:
  if lightdialogue9 == " ":
    break
  else:
    lightdialogue9 = input("???: So, in this realm, every mystic has a crystal assigned to them at birth, their crystals are infused with elemental magic, their stone determines what abilities they are able to wield and bend. It seems like you don't have one yet...")



lightdialogue10 = input("???: ...I have brought before you many mystical crystals from all over the Crystalline Realm...")
while True:
  if lightdialogue10 == " ":
    break
  else:
    lightdialogue10 = input("???: ...I have brought before you many mystical crystals from all over the Crystalline Realm...")


lightdialogue11 = input("???: ...just choose the one that calls out to you most...")
while True:
  if lightdialogue11 == " ":
    break
  else:
    lightdialogue11 = input("???: ...just choose the one that calls out to you most...")


lightdialogue12 = input("???: ...please choose wisely...")
while True:
  if lightdialogue12 == " ":
    break
  else:
    lightdialogue12 = input("???: ...please choose wisely...")
    
    
    
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
