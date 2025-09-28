import tkinter as tk
from tkinter import scrolledtext
from OrderManager import OrderManager
from PizzaIngredientFactory import NYPizzaIngredientFactory, ChicagoPizzaIngredientFactory
from PizzaBuilder import PizzaBuilder
from Pizza import Pizza
from PaymentCreator import CreditCardPaymentCreator, CashPaymentCreator

class PizzaApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pedido de Pizza - Padrões Criacionais")
        self.root.geometry("500x400")

        self.style_var = tk.StringVar(value="New York")
        tk.Label(self.root, text="Estilo de Pizza:").pack()
        tk.OptionMenu(self.root, self.style_var, "New York", "Chicago").pack()

        tk.Label(self.root, text="Toppings:").pack()
        self.toppings_entry = tk.Entry(self.root)
        self.toppings_entry.pack()

        tk.Button(self.root, text="Construir Pizza (Builder + Abstract Factory)", command=self.build_pizza).pack()
        tk.Button(self.root, text="Clonar Pizza (Prototype)", command=self.clone_pizza).pack()
        tk.Button(self.root, text="Pagar com Cartão (Factory Method)", command=self.pay_credit).pack()
        tk.Button(self.root, text="Pagar em Dinheiro (Factory Method)", command=self.pay_cash).pack()
        tk.Button(self.root, text="Mostrar Pedidos (Singleton)", command=self.show_orders).pack()

        self.output = scrolledtext.ScrolledText(self.root, height=10)
        self.output.pack()

        self.current_pizza = None

        self.root.mainloop()

    def build_pizza(self):
        factory = NYPizzaIngredientFactory() if self.style_var.get() == "New York" else ChicagoPizzaIngredientFactory()
        builder = PizzaBuilder(factory)
        self.current_pizza = builder.add_dough().add_sauce().add_cheese().add_toppings(self.toppings_entry.get()).build()
        self.output.insert(tk.END, f"Pizza construída: {self.current_pizza}\n")

    def clone_pizza(self):
        if self.current_pizza:
            cloned = self.current_pizza.clone()
            cloned.toppings += " (Clonada com extras)"
            self.output.insert(tk.END, f"Pizza clonada: {cloned}\n")
            self.current_pizza = cloned
        else:
            self.output.insert(tk.END, "Construa uma pizza primeiro!\n")

    def pay_credit(self):
        if self.current_pizza:
            creator = CreditCardPaymentCreator()
            payment = creator.create_payment(20.0)
            OrderManager().add_order(self.current_pizza, payment)
            self.output.insert(tk.END, "Pedido adicionado com pagamento por cartão.\n")
        else:
            self.output.insert(tk.END, "Construa uma pizza primeiro!\n")

    def pay_cash(self):
        if self.current_pizza:
            creator = CashPaymentCreator()
            payment = creator.create_payment(20.0)
            OrderManager().add_order(self.current_pizza, payment)
            self.output.insert(tk.END, "Pedido adicionado com pagamento em dinheiro.\n")
        else:
            self.output.insert(tk.END, "Construa uma pizza primeiro!\n")

    def show_orders(self):
        self.output.insert(tk.END, "Pedidos gerenciados: \n" + OrderManager().get_orders() + "\n")

if __name__ == "__main__":
    PizzaApp()