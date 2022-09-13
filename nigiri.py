from order import Order

class Nigiri(Order):
    def __init__(self, price):
        super().__init__('Nigiri', price)