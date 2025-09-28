
# Singleton: Gerenciador único de pedidos
class OrderManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.orders = ""
        return cls._instance

    def add_order(self, pizza, payment):
        self.orders += f"Pedido: {pizza} | Pagamento: {payment.pay(20.0)}\n"

    def get_orders(self):
        return self.orders
