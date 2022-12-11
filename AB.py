import json
import os
from json.decoder import JSONDecodeError
import sys


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
            weapon = {"name": "Wood Hammer", "level": 1, "power": 10}

        new_player = {
            username: {
                "password": password,
                "item_bag": {"potion": 5},
                "money": {"money": 200},
                "character1": {
                    "name": name,
                    "exp": {"exp": 1000},
                    "hp": {"hp": 100},
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
        print(" 3. Hammer")
        number = input(" Enter number: ")
        while number != "1" and number != "2" and number != "3":
            print(" >>System: pls choose number 1 - 3.")
            number = input(" Enter number: ")
        if number == "1":
            weapon = {"name": "Wood Sword", "level": 1, "power": 10}
        elif number == "2":
            weapon = {"name": "Wood Bow", "level": 1, "power": 10}
        elif number == "3":
            weapon = {"name": "Wood Hammer", "level": 1, "power": 10}

        new_player = {
            username: {
                "password": password,
                "item_bag": {"potion": 5},
                "money": {"money": 200},
                "character1": {
                    "name": name,
                    "exp": {"exp": 1000},
                    "hp": {"hp": 100},
                    "weapon": weapon,
                    "armor": {"name": "Wood Armor", "level": 1, "power": 10},
                }
            }
        }

        data.update(new_player)
        with open("player_data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    return username

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
        username = register()
        return username


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
            while name == "" :
                print(" >>System: name is not empty.")
                name = input(" Enter character name: ")
            weapon = {}
            print(" Starter weapon")
            print(" 1. Sword")
            print(" 2. Bow")
            print(" 3. Hammer")
            number = input(" Enter number: ")
            while number != "1" and number != "2" and number != "3":
                print(" >>System: please choose number 1 - 3.")
                number = input(" Enter number: ")
            if number == "1":
                weapon = {"name": "Wood Sword", "level": 1, "power": 10}
            elif number == "2":
                weapon = {"name": "Wood Bow", "level": 1, "power": 10}
            elif number == "3":
                weapon = {"name": "Wood Hammer", "level": 1, "power": 10}
            data[username][f'character{str(count+1)}'] = {
                                            "name": name,
                                            "exp": {"exp": 1000},
                                            "hp": {"hp": 100},
                                            "weapon": weapon,
                                            "armor": {"name": "Wood Armor", "level": 1, "power": 10},
                                        }
            with open("player_data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
    else:
        print(" >>System: No more available slots.")


def system_login():
    while True:
        print(" 1. Register")
        print(" 2. Login")
        number = input(" Enter number: ")
        while number != "1" and number != "2":
            print(" >>System: please choose 1 or 2.")
            number = input(" Enter number: ")
        if number == "1":
            register()
            return login()
        elif number == "2":
            return login()


class Character:
    def __init__(self, name, exp, hp, weapon, armor, money, item_bag):
        self.__name = name
        self.__exp = exp
        self.__hp = hp
        self.__weapon = weapon
        self.__armor = armor
        self.__money = money
        self.__item_bag = item_bag

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @property
    def exp(self):
        return self.__exp

    @property
    def level(self):
        return self.__exp['exp']//1000

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
               f" Hp: {self.hp['hp']}\n"\
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
                        print(f" >>System: you get {equipment}!")
                elif type_ == "Armor":
                    if name == equipment:
                        self.pyb.armor['name'] = equipment
                        self.pyb.armor['level'] = self.equipment_shop[type_][equipment]['level']
                        self.pyb.armor['power'] = self.equipment_shop[type_][equipment]['power']
                        self.pyb.money['money'] -= self.equipment_shop[type_][equipment]['price']
                        print(f" >>System: you get {equipment}!")

    def buy(self, item_name):
        if item_name in self.pyb.item_bag:
            self.pyb.item_bag[item_name] += 1
            self.pyb.money['money'] -= self.item_shop[item_name]
            print(f" >>System: {item_name} add to your bag!")
        else:
            self.pyb.item_bag[item_name] = 1
            self.pyb.money['money'] -= self.item_shop[item_name]
            print(f" >>System: {item_name} add to your bag!")

    def sell(self, item_name):
        if item_name in self.pyb.item_bag:
            if self.pyb.item_bag[item_name] >= 0:
                self.pyb.item_bag.pop(item_name)
            else:
                self.pyb.item_bag[item_name] -= 1
                self.pyb.money['money'] += self.item_shop[item_name]
                print(f" >>System: you sold {item_name}.")
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
               f" Hp: {self.boss_hp['hp']}\n" \
               f" Level: {self.boss_level['level']}\n" \
               f" Weapon: {self.boss_weapon['name']}[lv.{self.boss_weapon['level']}][ATK:{self.boss_weapon['power']}]\n" \
               f" Money earn: {self.boss_money['money']}-c\n" \
               f" Exp earn: {self.boss_exp_earn['exp']}exp\n" \
               f" Item drop: {self.boss_item_drop['name']} {self.boss_item_drop['many']}\n" \
               f" Weapon drop: {self.boss_weapon['name']}[lv.{self.boss_weapon['level']}][ATK:{self.boss_weapon['power']}]\n" \
               f" Armor drop: {self.boss_armor_drop['name']}[lv.{self.boss_armor_drop['level']}][DEF:{self.boss_armor_drop['power']}]"


class AB:
    def __init__(self, cha1, cha2, cha3, cb):
        self.__party = []
        if cha1 != {}:
            self.__party.append(cha1)
        if cha2 != {}:
            self.__party.append(cha2)
        if cha3 != {}:
            self.__party.append(cha3)
        self.__cb = cb

    @property
    def party(self):
        return self.__party

    @property
    def cb(self):
        return self.__cb


    def attack(self, ultimate_count, reward_count, save_hp_1, save_hp_2, save_hp_3, save_hp_boss):
        print('-' * 50)
        print(f"{'- Battle -':^50}")
        print('-' * 50)
        for cha in self.party:
            if cha != {} and cha.hp['hp'] > 0:
                if ultimate_count != 3:
                    if self.cb.boss_hp['hp'] <= 0:
                        self.cb.boss_hp['hp'] = self.cb.boss_hp['hp'] - self.cb.boss_hp['hp']
                        print(" - Boss dead! -")
                        if reward_count == 0:
                            for cha in self.party:
                                if cha != {}:
                                    if self.party.index(cha) == 0 and save_hp_1 != {}:
                                        cha.hp['hp'] = save_hp_1['hp']
                                    elif self.party.index(cha) == 1 and save_hp_2 != {}:
                                        cha.hp['hp'] = save_hp_2['hp']
                                    elif self.party.index(cha) == 2 and save_hp_3 != {}:
                                        cha.hp['hp'] = save_hp_3['hp']
                            self.claim_reward(save_hp_boss)
                        break
                    else:
                        self.cb.boss_hp['hp'] -= cha.weapon['power']
                        if self.cb.boss_hp['hp'] <= 0:
                            self.cb.boss_hp['hp'] = self.cb.boss_hp['hp'] - self.cb.boss_hp['hp']
                            print(f" {cha.name} attack {cha.weapon['power']}!")
                            print(" - Boss dead! -")
                            if reward_count == 0:
                                for cha in self.party:
                                    if cha != {}:
                                        if self.party.index(cha) == 0 and save_hp_1 != {}:
                                            cha.hp['hp'] = save_hp_1['hp']
                                        elif self.party.index(cha) == 1 and save_hp_2 != {}:
                                            cha.hp['hp'] = save_hp_2['hp']
                                        elif self.party.index(cha) == 2 and save_hp_3 != {}:
                                            cha.hp['hp'] = save_hp_3['hp']
                                self.claim_reward(save_hp_boss)
                            break
                    if cha.hp['hp'] > 0:
                        print(f" {cha.name} attack {cha.weapon['power']}!")
                        print(f" Boss hp: {self.cb.boss_hp['hp']}")
                    if "use_magic_block" in cha.item_bag:
                        print(f" >>System: {cha.name} blocks the boss attack.")
                    if ("use_magic_block" not in cha.item_bag) and ("use_shield"+f"_{str(self.party.index(cha))}" not in cha.item_bag):
                        cha.hp['hp'] -= (self.cb.boss_weapon['power'] - cha.armor['power'])
                        if cha.hp['hp'] <= 0:
                            print(f" >>System: {cha.name} dead.")
                            cha.hp['hp'] = cha.hp['hp'] - cha.hp['hp']
                        else:
                            print(f" {cha.name} hp: {cha.hp['hp']}")
                    if "use_shield"+f"_{str(self.party.index(cha))}" in cha.item_bag:
                        print(f" >>System: {cha.name} blocks the boss attack.")
                        self.party[0].item_bag["use_shield"+f"_{str(self.party.index(cha))}"] -= 1
                        if self.party[0].item_bag["use_shield"+f"_{str(self.party.index(cha))}"] <= 0:
                            self.party[0].item_bag.pop("use_shield"+f"_{str(self.party.index(cha))}")
                elif ultimate_count == 3:
                    if self.cb.boss_hp['hp'] <= 0:
                        self.cb.boss_hp['hp'] = self.cb.boss_hp['hp'] - self.cb.boss_hp['hp']
                        print(" - Boss dead! -")
                        if reward_count == 0:
                            for cha in self.party:
                                if cha != {}:
                                    if self.party.index(cha) == 0 and save_hp_1 != {}:
                                        cha.hp['hp'] = save_hp_1['hp']
                                    elif self.party.index(cha) == 1 and save_hp_2 != {}:
                                        cha.hp['hp'] = save_hp_2['hp']
                                    elif self.party.index(cha) == 2 and save_hp_3 != {}:
                                        cha.hp['hp'] = save_hp_3['hp']
                            self.claim_reward(save_hp_boss)
                        break
                    else:
                        self.cb.boss_hp['hp'] -= (cha.weapon['power']*10)
                        if self.cb.boss_hp['hp'] <= 0:
                            self.cb.boss_hp['hp'] = self.cb.boss_hp['hp'] - self.cb.boss_hp['hp']
                            if "Sword" in cha.weapon['name']:
                                os.system('python ultimate_sword.py')
                            elif "Bow" in cha.weapon['name']:
                                os.system('python ultimate_bow.py')
                            elif "Hammer" in cha.weapon['name']:
                                os.system('python ultimate_hammer.py')
                            print(f" {cha.name} attack {cha.weapon['power']*10}!")
                            print(" - Boss dead! -")
                            if reward_count == 0:
                                for cha in self.party:
                                    if cha != {}:
                                        if self.party.index(cha) == 0 and save_hp_1 != {}:
                                            cha.hp['hp'] = save_hp_1['hp']
                                        elif self.party.index(cha) == 1 and save_hp_2 != {}:
                                            cha.hp['hp'] = save_hp_2['hp']
                                        elif self.party.index(cha) == 2 and save_hp_3 != {}:
                                            cha.hp['hp'] = save_hp_3['hp']
                                self.claim_reward(save_hp_boss)
                            break
                    if cha.hp['hp'] > 0:
                        if "Sword" in cha.weapon['name']:
                            os.system('python ultimate_sword.py')
                        elif "Bow" in cha.weapon['name']:
                            os.system('python ultimate_bow.py')
                        elif "Hammer" in cha.weapon['name']:
                            os.system('python ultimate_hammer.py')
                        print(f" {cha.name} attack {cha.weapon['power']}!")
                        print(f" Boss hp: {self.cb.boss_hp['hp']}")
                    if "use_magic_block" in cha.item_bag:
                        print(f" >>System: {cha.name} blocks the boss attack.")
                    if ("use_magic_block" not in cha.item_bag) and ("use_shield"+f"_{str(self.party.index(cha))}" not in cha.item_bag):
                        cha.hp['hp'] -= (self.cb.boss_weapon['power'] - cha.armor['power'])
                        if cha.hp['hp'] <= 0:
                            print(f" >>System: {cha.name} dead.")
                            cha.hp['hp'] = cha.hp['hp'] - cha.hp['hp']
                        else:
                            print(f" {cha.name} hp: {cha.hp['hp']}")
                    if "use_shield"+f"_{str(self.party.index(cha))}" in cha.item_bag:
                        print(f" >>System: {cha.name} blocks the boss attack.")
                        self.party[0].item_bag["use_shield"+f"_{str(self.party.index(cha))}"] -= 1
                        if self.party[0].item_bag["use_shield"+f"_{str(self.party.index(cha))}"] <= 0:
                            self.party[0].item_bag.pop("use_shield"+f"_{str(self.party.index(cha))}")
        if "use_magic_block" in self.party[0].item_bag:
            self.party[0].item_bag['use_magic_block'] -= 1
            if self.party[0].item_bag['use_magic_block'] <= 0:
                self.party[0].item_bag.pop('use_magic_block')

    def use_item(self, character, item_name, save_hp):
        print('-' * 50)
        print(f"{'Use Item':^50}")
        print('-' * 50)
        if item_name == "potion":
            if character.hp['hp'] == save_hp['hp']:
                print(" System: your hp is full!")
            elif character.hp['hp'] <= 0:
                print(f" System: {character.name} dead!")
            elif character.hp['hp'] > 0:
                character.item_bag['potion'] -= 1
                character.hp['hp'] += 20
                if character.hp['hp'] > save_hp['hp']:
                    character.hp['hp'] = save_hp['hp']
                if character.item_bag['potion'] <= 0:
                    character.item_bag.pop('potion')
                print(f" >>System: {character.name} use potion.")
                print(f" >>System: {character.name} hp: {character.hp['hp']}")
        elif item_name == "banana":
            if character.hp['hp'] == save_hp['hp']:
                print(" System: your hp is full!")
            elif character.hp['hp'] <= 0:
                print(f" System: {character.name} dead!")
            elif character.hp['hp'] > 0:
                character.item_bag['banana'] -= 1
                character.hp['hp'] += 20
                if character.hp['hp'] > save_hp['hp']:
                    character.hp['hp'] = save_hp['hp']
                if character.item_bag['banana'] <= 0:
                    character.item_bag.pop('banana')
                print(f" >>System: {character.name} eat banana.")
                print(f" >>System: {character.name} hp: {character.hp['hp']}")
        elif item_name == "revive card":
            if character.hp['hp'] <= 0:
                character.item_bag['revive card'] -= 1
                character.hp['hp'] += save_hp['hp']
                if character.item_bag['revive card'] <= 0:
                    character.item_bag.pop('revive card')
                print(f" >>System: {character.name} has been revived!")
            else:
                print(f" >>System: {character.name} is still alive!")
        elif item_name == "magic block":
            if "use_magic_block" in character.item_bag:
                character.item_bag['use_magic_block'] += 1
                character.item_bag['magic block'] -= 1
                if character.item_bag['magic block'] <= 0:
                    character.item_bag.pop('magic block')
            if "use_magic_block" not in character.item_bag:
                character.item_bag['use_magic_block'] = 1
                character.item_bag['magic block'] -= 1
                if character.item_bag['magic block'] <= 0:
                    character.item_bag.pop('magic block')
            print(f" >>System: The party use magic block!")
        elif item_name == "shield":
            if "use_shield" in character.item_bag:
                character.item_bag["use_shield"+f"_{str(self.party.index(character))}"] += 1
                character.item_bag['shield'] -= 1
                if character.item_bag['shield'] <= 0:
                    character.item_bag.pop('shield')
            if "use_shield" not in character.item_bag:
                character.item_bag["use_shield"+f"_{str(self.party.index(character))}"] = 1
                character.item_bag['shield'] -= 1
                if character.item_bag['shield'] <= 0:
                    character.item_bag.pop('shield')
            print(f" >>System: {character.name} use shield!")
        elif item_name == "tangmo":
            if character.hp['hp'] == save_hp['hp']:
                print(" System: your hp is full!")
            elif character.hp['hp'] <= 0:
                print(f" System: {character.name} dead!")
            elif character.hp['hp'] > 0:
                character.item_bag['tangmo'] -= 1
                character.hp['hp'] += 20
                if character.hp['hp'] > save_hp['hp']:
                    character.hp['hp'] = save_hp['hp']
                if character.item_bag['tangmo'] <= 0:
                    character.item_bag.pop('tangmo')
                print(f" >>System: {character.name} eat tangmo.")
                print(f" >>System: {character.name} hp: {character.hp['hp']}")

    def claim_reward(self, save_hp_boss):
        for cha in self.party:
            cha.exp['exp'] = cha.exp['exp'] + self.cb.boss_exp_earn['exp']
            cha.hp['hp'] = cha.hp['hp'] + save_hp_boss['hp']
            print(f" >>System: {cha.name} get {self.cb.boss_exp_earn['exp']}exp!")
            print(f" >>System: {cha.name} hp+{save_hp_boss['hp']}!")
        self.party[0].item_bag[f"{self.cb.boss_item_drop['name']}"] = self.cb.boss_item_drop['many']
        self.party[0].money['money'] += self.cb.boss_money['money']
        print(f" >>System: {self.cb.boss_item_drop['name']} {self.cb.boss_item_drop['many']} add to your bag!")
        print(f" >>System: You get {self.cb.boss_money['money']}-c!")
        print(f" >>System: You get {self.cb.boss_weapon['name']}[lv.{self.cb.boss_weapon['level']}][ATK:{self.cb.boss_weapon['power']}]!")
        print(f" >>System: You get {self.cb.boss_armor_drop['name']}[lv.{self.cb.boss_armor_drop['level']}][DEF:{self.cb.boss_armor_drop['power']}]!")
        i = 0
        for cha in self.party:
            print(f" {i + 1}. {cha.name}")
            i += 1
        print(f" Which character will you choose to wear {self.cb.boss_weapon['name']}?")
        number = input(" Enter number: ")
        if i == 1:
            while number != "1":
                print(" >>System: please choose 1 or 2.")
                number = input(" Enter number: ")
        elif i == 2:
            while number != "1" and number != "2":
                print(" >>System: please choose 1 or 2.")
                number = input(" Enter number: ")
        elif i == 3:
            while number != "1" and number != "2" and number != "3":
                print(" >>System: please choose 1 - 3.")
                number = input(" Enter number: ")

        if number == "1":
            self.weapon_change(0)
        elif number == "2":
            self.weapon_change(1)
        elif number == "3":
            self.weapon_change(2)

        n = 0
        for cha in self.party:
            print(f" {n + 1}. {cha.name}")
            n += 1
        print(
            f" Which character will you choose to wear {self.cb.boss_armor_drop['name']}?")
        numbers = input(" Enter number: ")
        if n == 1:
            while numbers != "1":
                print(" >>System: please choose 1 or 2.")
                numbers = input(" Enter number: ")
        elif n == 2:
            while numbers != "1" and numbers != "2":
                print(" >>System: please choose 1 or 2.")
                numbers = input(" Enter number: ")
        elif n == 3:
            while numbers != "1" and numbers != "2" and numbers != "3":
                print(" >>System: please choose 1 - 3.")
                numbers = input(" Enter number: ")

        if numbers == "1":
            self.armor_change(0)
        elif numbers == "2":
            self.armor_change(1)
        elif numbers == "3":
            self.armor_change(2)


    def weapon_change(self, cha_index):
        self.party[cha_index].weapon['name'] = self.cb.boss_weapon['name']
        self.party[cha_index].weapon['level'] = self.cb.boss_weapon['level']
        self.party[cha_index].weapon['power'] = self.cb.boss_weapon['power']
        print(f" >>System: {self.party[cha_index].name} get {self.cb.boss_weapon['name']}[lv.{self.cb.boss_weapon['level']}][ATK:{self.cb.boss_weapon['power']}]")

    def armor_change(self, cha_index):
        self.party[cha_index].armor['name'] = self.cb.boss_armor_drop['name']
        self.party[cha_index].armor['level'] = self.cb.boss_armor_drop['level']
        self.party[cha_index].armor['power'] = self.cb.boss_armor_drop['power']
        print(f" >>System: {self.party[cha_index].name} get {self.cb.boss_armor_drop['name']}[lv.{self.cb.boss_armor_drop['level']}][ATK:{self.cb.boss_armor_drop['power']}]")



character_data_1 = {}
character_data_2 = {}
character_data_3 = {}

character_1 = {}
character_2 = {}
character_3 = {}

save_hp_1 = {}
save_hp_2 = {}
save_hp_3 = {}

save_hp_boss = {}

print('=' * 50)
print(f"{'Welcome to AB survive game':^50}")
print('=' * 50)
username = system_login()


with open("player_data.json", "r") as data_file:
    data = json.load(data_file)

data_player = data[username]

if 'character1' in data_player:
    character_data_1 = data_player['character1']
    save_hp_1['hp'] = character_data_1['hp']['hp']
    character_1 = Character(character_data_1['name'],
                            character_data_1['exp'],
                            character_data_1['hp'],
                            character_data_1['weapon'],
                            character_data_1['armor'],
                            data_player['money'],
                            data_player['item_bag'])


if 'character2' in data_player:
    character_data_2 = data_player['character2']
    save_hp_2['hp'] = character_data_2['hp']['hp']
    character_2 = Character(character_data_2['name'],
                            character_data_2['exp'],
                            character_data_2['hp'],
                            character_data_2['weapon'],
                            character_data_2['armor'],
                            data_player['money'],
                            data_player['item_bag'])


if 'character3' in data_player:
    character_data_3 = data_player['character3']
    save_hp_3['hp'] = character_data_3['hp']['hp']
    character_3 = Character(character_data_3['name'],
                            character_data_3['exp'],
                            character_data_3['hp'],
                            character_data_3['weapon'],
                            character_data_3['armor'],
                            data_player['money'],
                            data_player['item_bag'])


with open("boss_data.json", "r") as data_file:
    data_boss = json.load(data_file)

list_boss = []
for name_boss in data_boss:
    list_boss.append(name_boss)

ultimate_count = []
reward_count = []
for _ in range(len(list_boss)):
    ultimate_count.append(0)
    reward_count.append(0)


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
    print(" 8. Exit and save")
    number = input(" Enter number: ")
    while number != "1" and number != "2" and number != "3" and number != "4" and number != "5" and number != "6" and number != "7" and number != "8":
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
        boss_name = list_boss[int(number)-1]
        boss_choose_data = data_boss[boss_name]
        save_hp_boss[boss_name] = {}
        save_hp_boss[boss_name]['hp'] = boss_choose_data['hp']['hp']
        boss_choose = Boss(boss_choose_data['name'],
                           boss_choose_data['hp'],
                           boss_choose_data['level'],
                           boss_choose_data['weapon'],
                           boss_choose_data['armor'],
                           boss_choose_data['money'],
                           boss_choose_data['exp'],
                           boss_choose_data['item'])
        ab = AB(character_1, character_2, character_3, boss_choose)

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
                ab.attack(ultimate_count[list_boss.index(boss_name)], reward_count[list_boss.index(boss_name)], save_hp_1, save_hp_2, save_hp_3, save_hp_boss[boss_name])
                if ab.cb.boss_hp['hp'] <= 0:
                    if reward_count[list_boss.index(boss_name)] == 0:
                        reward_count[list_boss.index(boss_name)] += 1
                        if save_hp_1 != {}:
                            save_hp_1['hp'] = ab.party[0].hp['hp']
                        if save_hp_2 != {}:
                            save_hp_2['hp'] = ab.party[1].hp['hp']
                        if save_hp_3 != {}:
                            save_hp_3['hp'] = ab.party[2].hp['hp']
                if ultimate_count[list_boss.index(boss_name)] < 3:
                    ultimate_count[list_boss.index(boss_name)] += 1
                elif ultimate_count[list_boss.index(boss_name)] == 3:
                    ultimate_count[list_boss.index(boss_name)] -= 3
            elif number == "2":
                print('-' * 50)
                print(f"{'Select Item':^50}")
                print('-' * 50)
                list_item = []
                i = 0
                for item, many in character_1.item_bag.items():
                    if "use" not in item:
                        print(f" {i+1}. {item} have {many}.")
                        list_item.append(item)
                        i += 1
                print(" Which item you want to use?")
                number_ = input(" Enter number: ")
                if i == 1:
                    while number_ != "1":
                        print(" >>System: please choose 1 or 2.")
                        number_ = input(" Enter number: ")
                elif i == 2:
                    while number_ != "1" and number != "2":
                        print(" >>System: please choose 1 or 2.")
                        number_ = input(" Enter number: ")
                elif i == 3:
                    while number_ != "1" and number != "2" and number != "3":
                        print(" >>System: please choose 1 - 3.")
                        number_ = input(" Enter number: ")
                elif i == 4:
                    while number_ != "1" and number != "2" and number != "3" and number != "4":
                        print(" >>System: please choose 1 - 4.")
                        number_ = input(" Enter number: ")
                elif i == 5:
                    while number_ != "1" and number != "2" and number != "3" and number != "4" and number != "5":
                        print(" >>System: please choose 1 - 5.")
                        number_ = input(" Enter number: ")
                if list_item[int(number_)-1] != "magic block":
                    print('-' * 50)
                    print(f"{'Select Character':^50}")
                    print('-' * 50)
                    i = 0
                    for cha in ab.party:
                        print(f" {i + 1}. {cha.name}")
                        i += 1
                    print(" Which character will you choose to use item?")
                    number = input(" Enter number: ")
                    if i == 1:
                        while number != "1":
                            print(" >>System: please choose 1.")
                            number = input(" Enter number: ")
                    elif i == 2:
                        while number != "1" and number != "2":
                            print(" >>System: please choose 1 or 2.")
                            number = input(" Enter number: ")
                    elif i == 3:
                        while number != "1" and number != "2" and number != "3":
                            print(" >>System: please choose 1 - 3.")
                            number = input(" Enter number: ")
                if number == "1":
                    ab.use_item(ab.party[int(number)-1], list_item[int(number_)-1], save_hp_1)
                elif number == "2":
                    ab.use_item(ab.party[int(number)-1], list_item[int(number_)-1], save_hp_2)
                elif number == "3":
                    ab.use_item(ab.party[int(number)-1], list_item[int(number_)-1], save_hp_3)

            elif number == "3":
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
        if save_hp_1 == {}:
            if 'character1' in data_player:
                character_data_1 = data_player['character1']
                save_hp_1['hp'] = character_data_1['hp']['hp']
                character_1 = Character(character_data_1['name'],
                                        character_data_1['exp'],
                                        character_data_1['hp'],
                                        character_data_1['weapon'],
                                        character_data_1['armor'],
                                        data_player['money'],
                                        data_player['item_bag'])
        if save_hp_2 == {}:
            if 'character2' in data_player:
                character_data_2 = data_player['character2']
                save_hp_2['hp'] = character_data_2['hp']['hp']
                character_2 = Character(character_data_2['name'],
                                        character_data_2['exp'],
                                        character_data_2['hp'],
                                        character_data_2['weapon'],
                                        character_data_2['armor'],
                                        data_player['money'],
                                        data_player['item_bag'])

        if save_hp_3 == {}:
            if 'character3' in data_player:
                character_data_3 = data_player['character3']
                save_hp_3['hp'] = character_data_3['hp']['hp']
                character_3 = Character(character_data_3['name'],
                                        character_data_3['exp'],
                                        character_data_3['hp'],
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
        shop_ = shop

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
                elif number == "4":
                    shop.buy("revive card")
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
                elif number == "4":
                    shop.buy("revive card")
        elif number == "2":
            print('-' * 50)
            print(f"{'Select Character':^50}")
            print('-' * 50)
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
                cha = input(" Enter number: ")
                if cha == "1":
                    shop_ = shop
                elif cha == "2":
                    shop_ = shop_2
                while cha != "1" and cha != "2":
                    print(" >>System: please choose 1 or 2")
                    cha = input("Enter number: ")
            elif count == 3:
                cha = input(" Enter number: ")
                if cha == "1":
                    shop_ = shop
                elif cha == "2":
                    shop_ = shop_2
                elif cha == "3":
                    shop_ = shop_3
                while cha != "1" and cha != "2" and cha != "3":
                    print(" >>System: please choose 1 - 3")
                    cha = input(" Enter number: ")

            print('-' * 50)
            print(f"{'Equipment Shop':^50}")
            print('-' * 50)
            shop_.show_equipment_shop()
            print(" Which one you want to buy? Weapon(w) or Armor(a)")
            print(" - Ex. If you want Silver Sword enter w1")
            print("   = w from Weapon and 1 from first weapon")
            number = input(" If you dont want press enter: ")
            while True:
                if number == "w1":
                    shop_.buy_equipment("Silver Sword")
                    break
                elif number == "w2":
                    shop_.buy_equipment("Silver Bow")
                    break
                elif number == "w3":
                    shop_.buy_equipment("Silver Hammer")
                    break
                elif number == "a1":
                    shop_.buy_equipment("Silver Armor")
                    break
                elif number == "a2":
                    shop_.buy_equipment("Gold Armor")
                    break
                else:
                    print(" >>System: please select weapon or armor that show.")
                    number = input(" If you dont want press enter: ")

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

        if character_1 != {} and (data_player['character1']['hp']['hp'] < save_hp_1['hp']):
            data_player['character1']['hp']['hp'] = save_hp_1['hp']
        if character_2 != {} and (data_player['character2']['hp']['hp'] < save_hp_2['hp']):
            data_player['character2']['hp']['hp'] = save_hp_2['hp']
        if character_3 != {} and (data_player['character3']['hp']['hp'] < save_hp_3['hp']):
            data_player['character3']['hp']['hp'] = save_hp_3['hp']

        data[username].update(data_player)
        with open("player_data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
        sys.exit()
