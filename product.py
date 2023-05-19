class Store:
    def __init__(self):
        self.inventory = {"vegetables": {}, "fruits": {}}

    def add_product(self, category, product_name, price, quantity):
        if category in self.inventory:
            if product_name in self.inventory[category]:
                self.inventory[category][product_name]["price"] = price
                self.inventory[category][product_name]["quantity"] += quantity
            else:
                self.inventory[category][product_name] = {"price": price, "quantity": quantity}
        else:
            self.inventory[category] = {product_name: {"price": price, "quantity": quantity}}

    def remove_product(self, category, product_name):
        if category in self.inventory and product_name in self.inventory[category]:
            del self.inventory[category][product_name]

    def update_product_quantity(self, category, product_name, quantity):
        if category in self.inventory and product_name in self.inventory[category]:
            self.inventory[category][product_name]["quantity"] = quantity



storeA = Store()
storeB = Store()

storeA.add_product("vegetables", "Kales", 2.45, 20)
storeA.add_product("vegetables", "Managu", 3.8, 8)

storeB.add_product("fruits", "oranges", 3.70, 9)
storeB.add_product("fruits", "mango", 2.50, 15)


storeA.remove_product("vegetables", "Kales")

storeB.update_product_quantity("fruits", "mango", 55)

print(storeA.inventory)
print(storeB.inventory)
