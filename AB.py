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
            weapon = {"name": "Wood Sword", "level": 1, "power": 10}
        elif number == "2":
            weapon = {"name": "Wood Bow", "level": 1, "power": 10}
        elif number == "3":
            weapon = {"name": "Wood Hummer", "level": 1, "power": 10}

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
                    "armor": {"name": "Wood Armor", "level": 1, "power": 10},
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
            weapon = {"name": "Wood Sword", "level": 1, "power": 10}
        elif number == "2":
            weapon = {"name": "Wood Bow", "level": 1, "power": 10}
        elif number == "3":
            weapon = {"name": "Wood Hummer", "level": 1, "power": 10}

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
                    "armor": {"name": "Wood Armor", "level": 1, "power": 10},
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
                weapon = {"name": "Wood Sword", "level": 1, "power": 10}
            elif number == "2":
                weapon = {"name": "Wood Bow", "level": 1, "power": 10}
            elif number == "3":
                weapon = {"name": "Wood Hummer", "level": 1, "power": 10}
            data[username][f'character{str(count+1)}'] = {
                                            "name": name,
                                            "exp": 1000,
                                            "hp": 100,
                                            "weapon": weapon,
                                            "armor": {"name": "Wood Armor", "level": 1, "power": 10},
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
               f" Weapon: {self.weapon['name']}[lv.{self.weapon['level']}][ATK:{self.weapon['power']}]\n"\
               f" Armor: {self.armor['name']}[lv.{self.armor['level']}][DEF:{self.armor['power']}]\n"\
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
                if type_ == "Weapon":
                    print(f" {i}. {name}[lv.{self.equipment_shop[type_][name]['level']}][ATK:{self.equipment_shop[type_][name]['power']}] {self.equipment_shop[type_][name]['price']}-c.")
                elif type_ == "Armor":
                    print(f" {i}. {name}[lv.{self.equipment_shop[type_][name]['level']}][DEF:{self.equipment_shop[type_][name]['power']}] {self.equipment_shop[type_][name]['price']}-c.")
                i += 1

    def buy_equipment(self, equipment):
        for type_ in self.equipment_shop:
            for name in self.equipment_shop[type_]:
                if type_ == "Weapon":
                    if name == equipment:
                        self.pyb.weapon['name'] = equipment
                        self.pyb.weapon['level'] = self.equipment_shop[type_][equipment]['level']
                        self.pyb.weapon['power'] = self.equipment_shop[type_][equipment]['power']
                        self.pyb.money['money'] -= self.equipment_shop[type_][equipment]['price']
                elif type_ == "Armor":
                    if name == equipment:
                        self.pyb.armor['name'] = equipment
                        self.pyb.armor['level'] = self.equipment_shop[type_][equipment]['level']
                        self.pyb.armor['power'] = self.equipment_shop[type_][equipment]['power']
                        self.pyb.money['money'] -= self.equipment_shop[type_][equipment]['price']

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
    def __init__(self, boss_name, boss_hp, boss_level, boss_weapon, boss_armor_drop, boss_money, boss_exp_earn, boss_item_drop):
        self.__boss_name = boss_name
        self.__boss_hp = boss_hp
        self.__boss_level = boss_level
        self.__boss_weapon = boss_weapon
        self.__boss_armor_drop = boss_armor_drop
        self.__boss_money = boss_money
        self.__boss_exp_earn = boss_exp_earn
        self.__boss_item_drop = boss_item_drop

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
    def boss_exp_earn(self):
        return self.__boss_exp_earn

    @property
    def boss_item_drop(self):
        return self.__boss_item_drop

    @property
    def boss_armor_drop(self):
        return self.__boss_armor_drop

    def __repr__(self):
        return f"{'-' * 50}\n" \
               f"{'Boss info':^50}\n" \
               f"{'-' * 50}\n" \
               f" Name: {self.boss_name}\n" \
               f" Hp: {self.boss_hp}\n" \
               f" Level: {self.boss_level}\n" \
               f" Weapon: {self.boss_weapon['name']}[lv.{self.boss_weapon['level']}][ATK:{self.boss_weapon['power']}]\n" \
               f" Money earn: {self.boss_money}-c\n" \
               f" Exp earn: {self.boss_exp_earn}\n" \
               f" Item drop: {self.boss_item_drop['name']} {self.boss_item_drop['many']}\n" \
               f" Weapon drop: {self.boss_weapon['name']}[lv.{self.boss_weapon['level']}][ATK:{self.boss_weapon['power']}]\n" \
               f" Armor drop: {self.boss_armor_drop['name']}[lv.{self.boss_armor_drop['level']}][DEF:{self.boss_armor_drop['power']}]"


class AB:
    def __init__(self, cha1, cha2, cha3, cb):
        self.__party = [cha1, cha2, cha3]
        self.__cb = cb

    @property
    def party(self):
        return self.__party

    @property
    def cb(self):
        return self.__cb


    def attack(self):
        pass


    def use_item(self):
        pass


    def claim_reward(self):
        pass

    def weapon_change(self):
        pass

    def armor_change(self):
        pass

    # def update_exp(self):
    #     pass
    #
    # def update_level(self):
    #     pass
    #
    #
    # def update_money(self):
    #     pass
    #
    #
    # def item_drop_add(self):
    #     pass



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

with open("boss_data.json", "r") as data_file:
    data_boss = json.load(data_file)

list_boss = []
for name_boss in data_boss:
    list_boss.append(name_boss)


while True:
    print('=' * 50)
    print(f"{'- Menu -':^50}")
    print('=' * 50)
    print(" 1. Start Game!")
    print(" 2. Show character player info")
    print(" 3. Add character")
    print(" 4. Bag")
    print(" 5. Shop")
    print(" 6. Boss List")
    print(" 7. Exit without save")
    print(" 8. Exit and save game")
    number = input(" Enter number: ")
    while number != "1" and number != "2" and number != "3" and number != "4" and number != "5" and number != "6" and number != "7":
        print(" >>System: please choose number 1 - 8.")
        number = input(" Enter number: ")
    if number == "1":
        print('-' * 50)
        print(f"{'Boss list':^50}")
        print('-' * 50)
        list_number = []
        i = 0
        for boss in list_boss:
            print(f" {i+1}. {boss}")
            i += 1
            list_number.append(str(i))

        print(" Which boss you want to attack?")
        number = input(" Enter number: ")
        while number not in list_number:
            print(f" >>System: please choose number 1 - {i}.")
            number = input(" Enter number: ")
        boss_ = list_boss[int(number)-1]
        boss_choose_data = data_boss[boss_]

        # boss_name, boss_hp, boss_level, boss_weapon, boss_money, boss_exp_earn, boss_item_drop, boss_armor_drop

        boss_choose = Boss(boss_choose_data['name'],
                           boss_choose_data['hp'],
                           boss_choose_data['level'],
                           boss_choose_data['weapon'],
                           boss_choose_data['armor'],
                           boss_choose_data['money'],
                           boss_choose_data['exp'],
                           boss_choose_data['item'])
        while True:
            print('=' * 50)
            print(f"{'- Attack Boss -':^50}")
            print('=' * 50)
            print(" 1. Attack Boss!")
            print(" 2. Use Item")
            print(" 3. Show Boss info")
            print(" 4. Back to menu")
            number = input(" Enter number: ")
            while number != "1" and number != "2" and number != "3" and number != "4":
                print(" >>System: please choose number 1 - 4.")
                number = input(" Enter number: ")
            if number == "1":
                pass
            elif number == "2":
                pass
            elif number == "3":
                print('=' * 50)
                print(f"{'Boss info':^50}")
                print('=' * 50)
                print(boss_choose)
            elif number == "4":
                break


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
        shop_2 = Shop(data_shop_item, data_shop_equipment, character_2)
        shop_3 = Shop(data_shop_item, data_shop_equipment, character_3)

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
            print(f"{'Select Character':^50}")
            print('-' * 50)
            shop_ = ""
            count = 0
            if character_1 != {}:
                count += 1
                print(f" 1. {character_1.name}")
            if character_2 != {}:
                count += 1
                print(f" 2. {character_2.name}")
            if character_3 != {}:
                count += 1
                print(f" 3. {character_3.name}")
            if count == 1:
                shop_ = shop
            elif count == 2:
                cha = input("Enter number: ")
                if cha == "1":
                    shop_ = shop
                elif cha == "2":
                    shop_ = shop_2
                while cha != "1" and cha != "2":
                    print(" >>System: please choose 1 or 2")
                    cha = input("Enter number: ")
            elif count == 3:
                cha = input("Enter number: ")
                if cha == "1":
                    shop_ = shop
                elif cha == "2":
                    shop_ = shop_2
                elif cha == "3":
                    shop_ = shop_3
                while cha != "1" and cha != "2" and cha != "3":
                    print(" >>System: please choose 1 - 3")
                    cha = input("Enter number: ")

            print('-' * 50)
            print(f"{'Equipment Shop':^50}")
            print('-' * 50)
            shop_.show_equipment_shop()
            print(" Which one you want to buy?")
            print(" - Ex. If you want Silver Sword enter w1")
            print(" --- w from Weapon and 1 from first weapon")
            number = input(" If you dont want press enter: ")
            if number == "w1":
                shop_.buy_equipment("Silver Sword")
            elif number == "w2":
                shop_.buy_equipment("Silver Bow")
            elif number == "w3":
                shop_.buy_equipment("Silver Hummer")
            elif number == "a1":
                shop_.buy_equipment("Silver Armor")
            elif number == "a2":
                shop_.buy_equipment("Gold Armor")

    elif number == "6":
        print('-' * 50)
        print(f"{'Boss List':^50}")
        print('-' * 50)
        i = 0
        for boss in list_boss:
            print(f" {i+1}. {boss}")
            i += 1
    elif number == "7":
        sys.exit()

    elif number == "8":
        with open("player_data.json", "r") as data_file:
            data = json.load(data_file)

        data[username].update(data_player)
        with open("player_data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
        sys.exit()


# p = Character()
# q = Character()
# r = Character()
#
# player = [p, q, r]
