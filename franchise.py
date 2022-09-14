from logger import logger
from orderfactory import OrderFactory

class Franchise:
    def __init__(self, location_number):
        self.location_number = int(location_number)

    def place_order(self):
        ask_order = input('Please choose: Nigiri, Maki or Miso ')
        order_asked = OrderFactory.create_order(ask_order)
        logger.log_transaction(order_asked, self.location_number)

        