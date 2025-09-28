
# Builder: Constrói pizzas passo a passo
class PizzaBuilder:
    def __init__(self, ingredient_factory):
        self.pizza = Pizza()
        self.ingredient_factory = ingredient_factory

    def add_dough(self):
        self.pizza.dough = self.ingredient_factory.create_dough()
        return self

    def add_sauce(self):
        self.pizza.sauce = self.ingredient_factory.create_sauce()
        return self

    def add_cheese(self):
        self.pizza.cheese = self.ingredient_factory.create_cheese()
        return self

    def add_toppings(self, toppings):
        self.pizza.toppings = toppings
        return self

    def build(self):
        return self.pizza
