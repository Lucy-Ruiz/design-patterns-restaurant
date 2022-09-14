from nigiri import Nigiri
from maki import Maki
from miso import Miso

class OrderFactory:
    def __init__(self):
       pass

#This one will need a return, with a food type
    @staticmethod
    def create_order(order_string):
        if order_string == 'Nigiri':
            return Nigiri(8)
        elif order_string == 'Maki':
            return Maki(18)
        elif order_string == 'Miso':
            return Miso(3)
        else:
            return print('Please enter a valid dish option')
    