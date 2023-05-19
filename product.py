class Store:
    def __init__(self):
        self.items = []
    def add_vegetables(self, vegetables):
        self.items.append(vegetables)
    def remove_vegetables(self, vegetables):
        self.items.remove(vegetables)
    def update_vegetables_quantity(self, vegetables, quantity):
        vegetables.quantity = quantity