class Logger:
    def __init__(self):
        self.transaction_count = 0
        self.daily_sales = 0

#This method requires a that order is a type Order
    def log_transaction(self, order, store_number):
        self.transaction_count += 1
        self.daily_sales += order.price
        file = open('log.txt', 'a')
        file.write(f"""
        Your order number {self.transaction_count} of {order.dish_name} from {store_number} for {order.price}. 
        Total so far {self.daily_sales}\n""")
        file.close()

logger = Logger()
