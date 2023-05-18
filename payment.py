class Payment:
    def __init__(self):
        self.ordering = []

    def make_payment(self, customer, total, balance):
        if balance < total:
            return "Insufficient balance"
        else:
            balance -= total
            self.ordering.append((customer, total))
            return "Transaction successful"