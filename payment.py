class Payment:
    def __init__(self):
        self.ordering = []
    def make_payment(self, customer, total, balance):

        if total <= 0:
            return "Invalid amount"
        elif balance < 0:
            return "Invalid balance"
        elif balance < total:
            return "Insufficient balance"
        else:
            balance -= total
            self.ordering.append((customer, total))
            return "Transaction successful"



payment = Payment('Susan',1000)
result = payment.make_payment(500)
print(result) 







