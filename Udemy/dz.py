# Домашние работы по курсу Полное руководство по Python 3: от новичка до специалиста

class Pizza():
    _order = 1
    def __init__(self, ingredients: list):
        self.ingredients = ingredients
        self.order_number = Pizza._order
        Pizza._order += 1

    @staticmethod
    def garden_feast():
        f = Pizza(["spinach", "olives", "mushroom"])
        # f.order_number = Pizza._order + 1
        return f

    @staticmethod
    def hawaiian():
        f = Pizza(["ham", "pineapple"])
        # f.order_number += 1
        # f.order_number = Pizza._order + 1
        return f

    @staticmethod
    def meat_festival():
        f = Pizza(["beef", "meatball", "bacon"])
        # f.order_number += 1
        # f.order_number = Pizza._order + 1
        return f


p1 = Pizza(['bacon', 'parmezan', 'ham'])
p2 = Pizza.garden_feast()
print(p1.ingredients)
print(p2.ingredients)
print(p1.order_number)
print(p2.order_number)
p3 = Pizza.meat_festival()
print(p3.ingredients)
print(p3.order_number)
