from order import Order

class Miso(Order):
    def __init__(self, price):
        super().__init__('Miso', price)