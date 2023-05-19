class Payment:
    def __init__(self,ordering):
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
            return "Transaction Successful"
            
payment = Payment( [400])
result = payment.make_payment('Susan',2000,2200)
print(result)


















