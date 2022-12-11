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
