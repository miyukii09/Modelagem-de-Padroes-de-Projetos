
# Abstract Factory: Interface para criar famílias de ingredientes
class PizzaIngredientFactory:
    def create_dough(self):
        raise NotImplementedError

    def create_sauce(self):
        raise NotImplementedError

    def create_cheese(self):
        raise NotImplementedError

class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return "Massa Fina"

    def create_sauce(self):
        return "Molho Marinara"

    def create_cheese(self):
        return "Queijo Reggiano"

class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return "Massa Grossa"

    def create_sauce(self):
        return "Molho de Tomate Plum"

    def create_cheese(self):
        return "Queijo Mozzarella"
