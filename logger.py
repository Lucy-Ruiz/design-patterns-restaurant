class Logger:
    def __init__(self,transaction_count, daily_sales):
        self.transaction_count = int(transaction_count)
        self.daily_sales = int(daily_sales)

#This method requires a that order is a type Order
    def log_transaction(self, order, number):
        pass
