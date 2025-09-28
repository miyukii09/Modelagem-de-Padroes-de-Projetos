
# Factory Method: Classe abstrata para criar pagamentos
class PaymentCreator:
    def create_payment(self, amount):
        raise NotImplementedError

class CreditCardPaymentCreator(PaymentCreator):
    def create_payment(self, amount):
        return CreditCardPayment()

class CashPaymentCreator(PaymentCreator):
    def create_payment(self, amount):
        return CashPayment()

class Payment:
    def pay(self, amount):
        raise NotImplementedError

class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Pago {amount} com Cartão de Crédito"

class CashPayment(Payment):
    def pay(self, amount):
        return f"Pago {amount} em Dinheiro"
