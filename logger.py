class Logger:
    def __init__(self,transaction_count, daily_sales):
        self.transaction_count = int(transaction_count)
        self.daily_sales = int(daily_sales)

    def log_transaction(self, order, number):
        self.order = order
        self.number = int(number)
