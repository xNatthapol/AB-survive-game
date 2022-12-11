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
