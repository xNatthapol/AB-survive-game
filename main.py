import json
import sys
from json.decoder import JSONDecodeError
from character import Character
from shop import Shop
from boss import Boss
from attack_boss import AB


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

stop_loop = 0
while stop_loop == 0:
    with open("player_data.json", "r") as data_file:
        data = json.load(data_file)

    dict_cha = {}
    count = 0
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
    if count != 3:
        print('-' * 50)
        print(f"{'Character':^50}")
        print('-' * 50)
        print(f" You have {count} character {3 - count} slot left")
        for i in range(len(dict_cha)):
            print(f" Character {i + 1}: {dict_cha[str(i + 1)]}")
        print(" You want to add character or not?")
        print(" 1. Add character")
        print(" 2. No")
        number = input(" Enter number: ")
        while number != "1" and number != "2":
            print(" >>System: please choose 1 or 2.")
            number = input(" Enter number: ")
        if number == "1":
            add_character(username)
        elif number == "2":
            stop_loop += 1
    else:
        break

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
    print(" 3. Bag")
    print(" 4. Shop")
    print(" 5. Boss List")
    print(" 6. Log out and save")
    number = input(" Enter number: ")
    while number != "1" and number != "2" and number != "3" and number != "4" and number != "5" and number != "6":
        print(" >>System: please choose number 1 - 6.")
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
        character_1.show_item_bag()
    elif number == "4":
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

    elif number == "5":
        print('-' * 50)
        print(f"{'Boss List':^50}")
        print('-' * 50)
        i = 0
        for boss in list_boss:
            print(f" {i+1}. {boss}")
            i += 1

    elif number == "6":
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
