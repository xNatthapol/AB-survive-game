import os


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
