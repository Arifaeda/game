# Text based game.
# with open("title_screen.txt", 'r') as lol:
  # print(lol)

"""
Weakness and strengths.
-------------------------

Jade < Garnet
Garnet < Opal
Opal < Sapphire
Sapphire < Moonstone
Moonstone < Rose Quartz
Rose Quartz < Tanzanite
Tanzanite < Diamond
Diamond < Jade

Places.
--------------------------

Gale Plateau
Lykos Taiga
Glaecon Volcano
Thyella Sea Cliff
Nefeloma Lake
Titania's Forest
Elder Woods
Lumina City

Elites.
--------------------------

Zephyr
Vulpia
Hephael
Nyssa
Diane
Roselia
Alaric
Lucille
"""

next_line = ""
# Opening text.
welcome = input("Welcome to the Crystalline Realm! (press z to continue)")
while True:
  if welcome == "z" or "Z":
    break
  else:
    welcome = input("Welcome to the Crystalline Realm! (press z to continue)")

# intro

# Naming
name = input("Hello Mystic! You have stumbled upon the Crystalline Realm! May I ask, what is your name?")


while True:
  yes_no_name = input(f'Ah, your name is {name},did I get that right?[y/n]')
  if yes_no_name == "y":
    
    break
  if yes_no_name == "n":
    name = input("What is your name?")

# Dialogue
player_element_before = input("In this realm, every mystic has a birthstone or crystal, their crystals are infused with elemental magic,their stone determines what abilities they are able to wield and bend. It seems like you don't have one...(press z to continue)")
while True:
  if player_element_before == "z" or "Z":
    break
  else:
    player_element_before = input("In this realm, every mystic has a birthstone or crystal, their crystals are infused with elemental magic,their stone determines what abilities they are able to wield and bend. It seems like you don't have one...(press z to continue)")
player_element_before2 = input("...luckily for you, I brought some stones with me, pick one, choose wisely...(press z to continue)")
while True:
  if player_element_before2 == "z" or "Z":
    break
  else:
    player_element_before2 = input("...luckily for you, I brought some stones with me, pick one, choose wisely...(press z to continue)")


# Crystal Selection
while True:
  player_crystal = input("  Jade  Rose-quartz  Sapphire  Celestite  Garnet  Tanzanite  Diamond  Opal ")

  
  # Wind and Earth abilities
  if player_crystal == "Jade" or "jade":
    yes_no_jade = input("Jade: a light green stone engraved with carvings of dragons, swirls, and spirals. Choose this crystal?[y/n]")
    if yes_no_jade == "Y" or "y":
      pass
    if yes_no_jade == "N" or "n":
      yes_no_jade = ""
      
      
    # Fairytale/Charm abilities
  if player_crystal.upper == "ROSE-QUARTZ" or "ROSE QUARTZ":
    yes_no_rosequartz = input("Rose-quartz: a light pink opaque crystal, it somehow looks... cute. Choose this crystal?[y/n]")
    if yes_no_rosequartz == "Y" or "y":
      pass
    if yes_no_rosequartz == "N" or "n":
      yes_no_rosequartz == ""
      player_element = input("  Jade  Rose-quartz  Sapphire  Celestite  Garnet  Tanzanite  Diamond  Opal ")
  # Storm abilities (electric and water)
  # Cosmic abilities
  # Tamer (Summon animals) and morphing abilities
  # Dark/Necromancy/Demonic abilities
  # Light/Metal abilities
  # Fire and Ice abilities
