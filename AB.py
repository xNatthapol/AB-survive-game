import csv
import json
import os
from json.decoder import JSONDecodeError
import sys
import turtle
import time


def register():
    print('-' * 50)
    print(f"{'Register new player':^50}")
    print('-' * 50)
    try:
        with open("player_data.json", "r") as data_file:
            data = json.load(data_file)
    except JSONDecodeError:
        username = input(" Enter username: ")
        password = input(" Enter password: ")
        name = input(" Enter character name: ")
        weapon = {}
        print(" Starter weapon")
        print(" 1. Sword")
        print(" 2. Bow")
        print(" 3. Hummer")
        number = input(" Enter number: ")
        while number != "1" and number != "2" and number != "3":
            print(" >>System: please choose number 1 - 3.")
            number = input(" Enter number: ")
        if number == "1":
            weapon = {"weapon": "Wood Sword", "lv": 1}
        elif number == "2":
            weapon = {"weapon": "Wood Bow", "lv": 1}
        elif number == "3":
            weapon = {"weapon": "Wood Hummer", "lv": 1}

        new_player = {
            username: {
                "password": password,
                "item_bag": {"potion": 5},
                "money": {"money": 200},
                "character1": {
                    "name": name,
                    "exp": 1000,
                    "hp": 100,
                    "weapon": weapon,
                    "armor": {"armor": "Wood Armor", "lv": 1},
                }
            }
        }

        with open("player_data.json", "w") as data_file:
            json.dump(new_player, data_file, indent=4)
    else:
        username = input(" Enter username: ")
        while username in data:
            print(" >>System: Username already used!")
            username = input(" Enter username: ")
        password = input(" Enter password: ")
        name = input(" Enter character name: ")
        weapon = {}
        print(" Starter weapon")
        print(" 1. Sword")
        print(" 2. Bow")
        print(" 3. Hummer")
        number = input(" Enter number: ")
        while number != "1" and number != "2" and number != "3":
            print(" >>System: pls choose number 1 - 3.")
            number = input(" Enter number: ")
        if number == "1":
            weapon = {"weapon": "Wood Sword", "lv": 1}
        elif number == "2":
            weapon = {"weapon": "Wood Bow", "lv": 1}
        elif number == "3":
            weapon = {"weapon": "Wood Hummer", "lv": 1}

        new_player = {
            username: {
                "password": password,
                "item_bag": {"potion": 5},
                "money": {"money": 200},
                "character1": {
                    "name": name,
                    "exp": 1000,
                    "hp": 100,
                    "weapon": weapon,
                    "armor": {"armor": "Wood Armor", "lv": 1},
                }
            }
        }

        data.update(new_player)
        with open("player_data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)


def login():
    print('-' * 50)
    print(f"{'Log In game':^50}")
    print('-' * 50)
    try:
        with open("player_data.json", "r") as data_file:
            data = json.load(data_file)
        username = input(" Username: ")
        while username not in data:
            print(" >>System: Username not found!")
            username = input(" Username: ")
        password = input(" Password: ")
        while password != data[username]["password"]:
            print(" >>System: Invalid password!")
            password = input(" Password: ")
        return username
    except JSONDecodeError:
        print('-' * 50)
        print(f"{'You are the first player!':^50}")
        print('-' * 50)
        register()


def add_character(username):
    with open("player_data.json", "r") as data_file:
        data = json.load(data_file)

    dict_cha = {}
    count = 0
    print('-' * 50)
    print(f"{'Character':^50}")
    print('-' * 50)
    for cha in data[username]:
        if cha != "password":
            if cha == "character1":
                dict_cha["1"] = data[username][cha]['name']
                count += 1
            if cha == "character2":
                dict_cha["2"] = data[username][cha]['name']
                count += 1
            if cha == "character3":
                dict_cha["3"] = data[username][cha]['name']
                count += 1

    print(f" You have {count} character {3-count} slot left")

    for i in range(len(dict_cha)):
        print(f" Character {i+1}: {dict_cha[str(i+1)]}")
    if count != 3:
        print(" You want to add character or not?")
        print(" 1. Add character")
        print(" 2. No")
        number = input(" Enter number: ")
        while number != "1" and number != "2":
            print(" >>System: please choose 1 or 2.")
            number = input(" Enter number: ")
        if number == "1":
            name = input(" Enter character name: ")
            data[username][f'character{str(count+1)}'] = {
                                            "name": name,
                                            "exp": 1000,
                                            "hp": 100,
                                            "weapon": {"weapon": "wood sword", "lv": 1},
                                            "armor": {"armor": "wood armor", "lv": 1},
                                        }
            with open("player_data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
    else:
        print("No more available slots.")


def system_login():
    while True:
        print(" 1. Register")
        print(" 2. Login")
        number = input(" Enter number: ")
        while number != "1" and number != "2":
            print(" >>System: please choose 1 or 2.")
            # print(" 1. Register")
            # print(" 2. Login")
            number = input(" Enter number: ")
        if number == "1":
            register()
            return login()
        elif number == "2":
            return login()


class Character:
    def __init__(self, name, exp, weapon, armor, money, item_bag):
        self.__name = name
        self.__exp = exp
        self.__weapon = weapon
        self.__armor = armor
        self.__money = money
        self.__item_bag = item_bag

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return (self.__exp//1000) * 100

    @property
    def level(self):
        return self.__exp//1000

    @property
    def weapon(self):
        return self.__weapon

    @property
    def armor(self):
        return self.__armor

    @property
    def money(self):
        return self.__money

    @property
    def item_bag(self):
        return self.__item_bag

    def show_item_bag(self):
        print('-' * 50)
        print(f"{'Bag':^50}")
        print('-' * 50)
        i = 1
        for item, many in self.item_bag.items():
            print(f" {i}. {item} have {many}.")
            i += 1

    def __repr__(self):
        return f"{'-' * 50}\n"\
               f"{'Character info':^50}\n"\
               f"{'-' * 50}\n"\
               f" Name: {self.name}\n"\
               f" Hp: {self.hp}\n"\
               f" Level: {self.level}\n"\
               f" Weapon: {self.weapon['weapon']}[lv.{self.weapon['lv']}]\n"\
               f" Armor: {self.armor['armor']}[lv.{self.armor['lv']}]\n"\
               f" Money: {self.money['money']}-c"


class Shop:
    def __init__(self, item_shop, equipment_shop, pyb):
        self.__item_shop = item_shop
        self.__equipment_shop = equipment_shop
        self.__pyb = pyb

    @property
    def item_shop(self):
        return self.__item_shop

    @property
    def equipment_shop(self):
        return self.__equipment_shop

    @property
    def pyb(self):
        return self.__pyb

    def show_item_shop(self):
        i = 1
        for item, price in self.item_shop.items():
            print(f" {i}. {item} {price}-c.")
            i += 1

    def show_equipment_shop(self):
        for type_ in self.equipment_shop:
            i = 1
            print(f"{f'---- {type_} ----':^10}")
            for name in self.equipment_shop[type_]:
                print(
                    f" {i}. {name} lv.{self.equipment_shop[type_][name]['level']} {self.equipment_shop[type_][name]['price']}-c.")
                i += 1

    def buy_equipment(self):
        print("You buy it!")

    def sell_equipment(self):
        pass

    def buy(self, item_name):
        if item_name in self.pyb.item_bag:
            self.pyb.item_bag[item_name] += 1
            self.pyb.money["money"] -= self.item_shop[item_name]
        else:
            self.pyb.item_bag[item_name] = 1
            self.pyb.money["money"] -= self.item_shop[item_name]

    def sell(self, item_name):
        if item_name in self.pyb.item_bag:
            self.pyb.item_bag[item_name] -= 1
            self.pyb.money["money"] += self.item_shop[item_name]
            if self.pyb.item_bag[item_name] == 0:
                self.pyb.item_bag.pop(item_name)
        else:
            return None



class Boss:
    def __init__(self, boss_name, boss_hp, boss_level, boss_weapon, boss_money, boss_level_earn, boss_item_drop, boss_weapon_drop, boss_armor_drop):
        self.__boss_name = boss_name
        self.__boss_hp = boss_hp
        self.__boss_level = boss_level
        self.__boss_weapon = boss_weapon
        self.__boss_money = boss_money
        self.__boss_level_earn = boss_level_earn
        self.__boss_item_drop = boss_item_drop
        self.__boss_weapon_drop = boss_weapon_drop
        self.__boss_armor_drop = boss_armor_drop


    @property
    def boss_name(self):
        return self.__boss_name


    @property
    def boss_hp(self):
        return self.__boss_hp


    @property
    def boss_level(self):
        return self.__boss_level


    @property
    def boss_weapon(self):
        return self.__boss_weapon


    @property
    def boss_money(self):
        return self.__boss_money


    @property
    def boss_level_earn(self):
        return self.__boss_level_earn


    @property
    def boss_item_drop(self):
        return self.__boss_item_drop

    @property
    def boss_weapon_drop(self):
        return self.__boss_weapon_drop


    @property
    def boss_armor_drop(self):
        return self.__boss_armor_drop


class AB:
    def __init__(self, cha1, cha2, cha3, cb):
        self.party = [cha1, cha2, cha3]
        self.cb = cb


    def player_use_item(self):
        pass


    def update_exp(self):
        pass


    def update_level(self):
        pass


    def update_money(self):
        pass


    def item_drop_add(self):
        pass

    def weapon_change(self):
        pass

    def armor_change(self):
        pass

    def attack(self):
        pass



character_data_1 = {}
character_data_2 = {}
character_data_3 = {}

character_1 = {}
character_2 = {}
character_3 = {}


print('=' * 50)
print(f"{'Welcome to AB survive game':^50}")
print('=' * 50)
username = system_login()


with open("player_data.json", "r") as data_file:
    data = json.load(data_file)

data_player = data[username]
if 'character1' in data_player:
    character_data_1 = data_player['character1']
    character_1 = Character(character_data_1['name'],
                            character_data_1['exp'],
                            character_data_1['weapon'],
                            character_data_1['armor'],
                            data_player['money'],
                            data_player['item_bag'])

if 'character2' in data_player:
    character_data_2 = data_player['character2']
    character_2 = Character(character_data_2['name'],
                            character_data_2['exp'],
                            character_data_2['weapon'],
                            character_data_2['armor'],
                            data_player['money'],
                            data_player['item_bag'])

if 'character3' in data_player:
    character_data_3 = data_player['character3']
    character_3 = Character(character_data_3['name'],
                            character_data_3['exp'],
                            character_data_3['weapon'],
                            character_data_3['armor'],
                            data_player['money'],
                            data_player['item_bag'])

while True:
    print('-' * 50)
    print(f"{'- Menu -':^50}")
    print('-' * 50)
    print(" 1. Attack Boss")
    print(" 2. Show character player info")
    print(" 3. Add character")
    print(" 4. Bag")
    print(" 5. Shop")
    print(" 6. Exit and save game")
    number = input(" Enter number: ")
    while number != "1" and number != "2" and number != "3" and number != "4" and number != "5" and number != "6":
        print(" >>System: please choose number 1 - 6.")
        number = input(" Enter number: ")
    if number == "1":
        pass
    elif number == "2":
        if character_1 != {}:
            print(character_1)
        if character_2 != {}:
            print(character_2)
        if character_3 != {}:
            print(character_3)
    elif number == "3":
        add_character(username)
        with open("player_data.json", "r") as data_file:
            data = json.load(data_file)
        data_player = data[username]
        if 'character1' in data_player:
            character_data_1 = data_player['character1']
            character_1 = Character(character_data_1['name'],
                                    character_data_1['exp'],
                                    character_data_1['weapon'],
                                    character_data_1['armor'],
                                    data_player['money'],
                                    data_player['item_bag'])

        if 'character2' in data_player:
            character_data_2 = data_player['character2']
            character_2 = Character(character_data_2['name'],
                                    character_data_2['exp'],
                                    character_data_2['weapon'],
                                    character_data_2['armor'],
                                    data_player['money'],
                                    data_player['item_bag'])

        if 'character3' in data_player:
            character_data_3 = data_player['character3']
            character_3 = Character(character_data_3['name'],
                                    character_data_3['exp'],
                                    character_data_3['weapon'],
                                    character_data_3['armor'],
                                    data_player['money'],
                                    data_player['item_bag'])

        if character_1 != {}:
            print(character_1)
        if character_2 != {}:
            print(character_2)
        if character_3 != {}:
            print(character_3)
    elif number == "4":
        character_1.show_item_bag()
    elif number == "5":
        print('-' * 50)
        print(f"{'Shop':^50}")
        print('-' * 50)
        print(" 1. Item Shop")
        print(" 2. Equipment Shop")
        number = input(" Enter number: ")
        while number != "1" and number != "2":
            print(" >>System: please choose number 1 or 2.")
            number = input(" Enter number: ")

        with open("item_shop.json", "r") as data_file:
            data_shop_item = json.load(data_file)

        with open("equipment_shop.json", "r") as data_file:
            data_shop_equipment = json.load(data_file)

        shop = Shop(data_shop_item, data_shop_equipment, character_1)

        if number == "1":
            print('-' * 50)
            print(f"{'Item Shop':^50}")
            print('-' * 50)
            shop.show_item_shop()
            print(" You want to (b)buy or (s)sell ?")
            choice = input(" If you dont want press enter: ")
            while choice != "b" and choice != "s" and choice != "":
                print(" >>System: please choose b or s or enter.")
                print(" You want to (b)buy or (s)sell")
                choice = input(" If you dont want press enter: ")
            if choice == "b":
                print('-' * 50)
                print(f"{'Buy Item':^50}")
                print('-' * 50)
                shop.show_item_shop()
                print(" Which one you want to buy?")
                number = input(" If you dont want press enter: ")
                if number == "1":
                    shop.buy("potion")
                elif number == "2":
                    shop.buy("magic block")
                elif number == "3":
                    shop.buy("shield")
            elif choice == "s":
                print('-' * 50)
                print(f"{'Sell Item':^50}")
                print('-' * 50)
                character_1.show_item_bag()
                print(" Which one you want to sell?")
                number = input(" If you dont want press enter: ")
                if number == "1":
                    shop.sell("potion")
                elif number == "2":
                    shop.sell("magic block")
                elif number == "3":
                    shop.sell("shield")
        elif number == "2":
            print('-' * 50)
            print(f"{'Equipment Shop':^50}")
            print('-' * 50)
            shop.show_equipment_shop()
            print(" You want to (b)buy or (s)sell ?")
            choice = input(" If you dont want press enter: ")
            while choice != "b" and choice != "s" and choice != "":
                print(" >>System: please choose b or s or enter.")
                print(" You want to (b)buy or (s)sell")
                choice = input(" If you dont want press enter: ")
            if choice == "b":
                print('-' * 50)
                print(f"{'Buy equipment':^50}")
                print('-' * 50)
                shop.show_equipment_shop()
                print(" Which one you want to buy?")
                print(" - Ex. If you want Silver Sword enter w1")
                print(" --- w from Weapon and 1 from first weapon")
                number = input(" If you dont want press enter: ")
                if number == "w1":
                    shop.buy_equipment()
                elif number == "2":
                    shop.buy_equipment()
                elif number == "3":
                    shop.buy_equipment()
            elif choice == "s":
                print('-' * 50)
                print(f"{'Sell equipment':^50}")
                print('-' * 50)
                character_1.show_item_bag()
                print(" Which one you want to sell?")
                number = input(" If you dont want press enter: ")
                if number == "1":
                    shop.sell("potion")
                elif number == "2":
                    shop.sell("magic block")
                elif number == "3":
                    shop.sell("shield")


    elif number == "6":
        with open("player_data.json", "r") as data_file:
            data = json.load(data_file)

        data[username].update(data_player)
        with open("player_data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
        sys.exit()








# print(character_1)
# print(character_2)
# print(character_1.item_bag)
# print(character_2.item_bag)
# print(character_1.money)
# print(character_2.money)


# print(character_2)
# print(character_3)
# print(data_player)

# wp = {'weapon': ['Wood sword', 1]}
# ar = {'armor': ['Wood armor', 1]}
# bg = {'Banana': 3, 'Apple': 5, 'gal':5}
# shop = {'hal': 10, 'gal': 20}
# a = Character("Sato", 1000, 1000, wp, ar, 1000, bg)
# # name, hp, exp, weapon, armor, money, item_bag
# print(a)
# # # b = Shop(shop, a)



# p = Character()
# q = Character()
# r = Character()
#
# player = [p, q, r]
