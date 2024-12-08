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

# Game Development Features

## Main
- **Initialization**: Start by initializing the Pygame library to set up the window and resources.
- **Game Loop**: Implement a game loop that manages navigation through different menus and screens.
- **Termination**: Ensure the game can be properly exited, cleaning up resources and closing the Pygame window.

## Menu
- Develop a menu with interactive buttons from Arena to Museum, as well as an exit button.

## Arena
- Create an infinite strategic arena where players can face enemies.
- Each battle allows players to five enemies.
- Define the logic for enemies dropping money and experience.
- Levels of the enemy rise with the current level.
- Calculate player's level based on experience using the formula: `100 + 1.5**(level / 2)`
- Implement special attacks and their effects, unlocked every 10 levels:
  - **Double attack**: Double normal attack.
  - **Stun**: Stun enemy for 5 turns.
  - **Poison**: Deals 25% damage of normal attack every turn.
  - **Heal**: Heals the player by 25%.
  - **Magic armor**: Decreases damage taken by 80% for 5 turns.
  - **Vampirism**: Increase you health by the damage dealt.
  - **Deadly**: 10 times normal attack.
- Provide four potions of each type:
  - **HP**: Restores 50% of your HP.
  - **Energy**: Restores all your special attacks.
  - **Strength**: Doubles your damage.
  - **Shield**: Magic shield but better.

## Training
- Set up a training menu with buttons labeled from Melee to Agility plus a back button for navigation.

### Melee
- 

### Block
 - 

### Range
- 

### Agility
- 

## Shop
- Display the player's money and create buttons to purchase items (sword, shield, bow, armor).
- Adjust item prices using the formula: `100*2^(item level / 32)`.
- Set initial item level to 0, with a maximum level cap of 20.

## Museum
- Implement a feature listing all player statistics fetched from "data.txt", and include a back button.

## Save and Load
- Implement save and load functionality to allow players to save their progress and load it later.

## Coding Standards
- **Python Style Guide**: Ensure your code adheres to the Python Enhancement Proposals (PEP8, PEP257).
- **Google Python Style Guide**: Follow the guidelines outlined in the Google Python Style Guide for naming conventions, comments, and coding practices.
- **Explicit Typing**: Define all variables explicitly with clear types to enhance readability and maintainability.
