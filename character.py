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
