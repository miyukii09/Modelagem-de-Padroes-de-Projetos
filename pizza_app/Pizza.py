
# Prototype: Permite clonar pizzas
import copy

class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.toppings = None

    def __str__(self):
        return f"Pizza com {self.dough}, {self.sauce}, {self.cheese}, Toppings: {self.toppings}"

    def clone(self):
        return copy.deepcopy(self)
