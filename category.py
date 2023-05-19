class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
    def add_product(self, product):
        self.products.append(product)
        return f"{name} was added into the category"
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            return f"{name} Is removed from the category"
    def update_description(self, new_description):
        self.description = new_description
        return f"{name} description was updated"