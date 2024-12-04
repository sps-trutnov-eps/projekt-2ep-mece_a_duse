# Meče & Duše

Tahová bojovka postavená na hře Sword & Souls.

## Funkce

- [ ] Tréninková budova
- [ ] Obchod
- [ ] Levelový systém

### Doplňkové funkce

- [ ] Speciální útoky
- [ ] Budova muzea (statistiky)

You are tasked with developing a copycat game of "Swords & Souls: Neverseen" in Python using the Pygame library, while adhering to specified design elements and coding practices. This detailed prompt will guide you through the various aspects of the game including mechanics, design, and coding standards.

## Game Development Features

### Main
- **Initialization**: Start by initializing the Pygame library to set up the window and resources.
- **Game Loop**: Implement a game loop that manages navigation through different menus and screens.
- **Termination**: Ensure the game can be properly exited, cleaning up resources and closing the Pygame window.

### Menu
- Develop a menu with interactive buttons from Arena to Museum, as well as an exit button.

### Arena
- Create an infinite strategic arena where players can face enemies.
- Each battle allows players to fight up to three enemies and select which to attack.
- Define the logic for enemies dropping experience and money calculated using the formula 2^(enemy level / 32).
- Levels of the enemy rise widht the curent level.
- Calculate player's level based on experience using the formula: player's experience / 2^(player's level / 32).
- Implement special attacks and their effects, unlocked every 20 levels:
  - Triple attack (Triple normal attack)
  - Stun (Stun player for 5 turns)
  - Poison (Deals 75% of normal attack for 5 turns)
  - Heal (Heals the player by 50%)
  - Magic armor (Increse armor by 25%)
  - Vampirism (Increase you health by the damage dealt)
  - Impatient (Decrese skill couldown)
  - Deadly (25% chance for instakill, reloading ever 5 levels)
- Introduce a 10% critical hit chance to inflict 10x damage on enemies.
- Provide five potions of each type:
  - HP (Restores your HP)
  - Energy (Restores all your special attacks)
  - Strengh (Doubles your damage)

### Training
- Set up a training menu with buttons labeled from Melee to Agility plus a back button for navigation.

### Shop
- Display the player's money and create buttons to purchase items (sword, shield, bow, armor).
- Adjust item prices using the formula: 100*2^(item level / 32).
- Set initial item level to 0, with a maximum level cap of 20.

### Museum
- Implement a feature listing all player statistics fetched from "data.txt", and include a back button.

### Melee
- 

### Block
 - 

### Range
- 

### Agility
- 

## Coding Standards

- Ensure the codebase complies with the Python Enhancement Proposals (PEP8, PEP257) and Google Python Style Guide.
- Ensure all the variables in the codebase anse clearly defined with explicit types.
