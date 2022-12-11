# Project: AB survive game

## Project overview

This is a survival game where you attack bosses to level up. Playing will consist of a separate turn of player versus boss, with items to be used. When the player has finished hitting the boss, the boss will bounce back and forth until one of the sides' HP is turn to 0. In the game, you can use bags to store items and money to purchase armor, weapons, potions, and other items from the shop. When you defeat the boss, he will drop a random item, weapon and armor, money, and level.

## System in game

- This game has a register system for creating your game ID.
- This game has a login system that allows you to log in your game ID.
- This game has an add character system that allows you to create your character in your game ID.
- This game has a bag that contains items dropped by bosses or purchased from the shop.
- This game has a shop that you can buy and sell items or equipment.
- This game has an attack system that you can attack the boss.
- This game has a use item system that you can use your item in your bag.
- This game has a logout system that allows you to log out and save your game ID.

## Class implemented

- ### Character from character.py
    This class get name, exp, hp, weapon, armor, money and bag from player data and show that player character data.
- ### Shop from shop.py
    This class get bag from class Character, item and equipment data in shop data, in this class there is a method for buying and selling items and equipment.
- ### Boss from boss.py
    This class get boss name, boss hp, boss level, weapon that boss use, armor drop from boss, money earn from boss, exp earn from boss and item drop from boss and show that boss data.
- ### AB from attack_boss.py
    This class get character of player from class Character and boss data from class Boss.In this class has method attack to attack boss, use item for use you item in your bag, claim reward to claim your reward from killing boss.

## Additional files

- ### ultimate_sword.py
    To display the ultimate of the sword.
    - The relevant file is sword-xxxxx.png
- ### ultimate_bow.py
    To display the ultimate of the bow.
    - The relevant file is bow-xxxxx.png
- ### ultimate_sword.py
    To display the ultimate of the hammer.
    - The relevant file is hammer-xxxxx.png
- ### boss_data.json
    json file for storing boss data.
- ### equipment_shop.json
    json file for storing equipment shop data.
- ### item_shop.json
    json file for storing item shop data.
- ### player_data.json
    json file for storing player data.

## How to install this game

First, you need to create your own folder (folder name can be whatever)
Second, clone this file.

``git clone https://github.com/xNatthapol/AB-survive-game.git``

### Installation requirements

- Python 3.8 or higher

## How to play this game

- If you're using an IDE to run the code, go to the main.py file and click run.
- Select register to create your game ID.
- If you already have a game ID, you can select login.
- Select Add character if you want to add more character.
- Then choose Start Game! to attack the boss.
- You can use item from select Use Item.
- You can buy item and equipment from shop.
- If you successfully kill the boss you will receive a reward.
- If you want to exit the game, select Log out and save.

## Github of this project
>https://github.com/xNatthapol/AB-survive-game
