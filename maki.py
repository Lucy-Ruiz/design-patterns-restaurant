from order import Order

class Maki(Order):
    def __init__(self, price):
        super().__init__('Maki', price)