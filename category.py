class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)
            return f"{product} was added to the category"
        else:
            return f"{product} already exists in the category"
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            return f"{product} is removed from the category"
        else:
            return f"{product} does not exist in this category"
    def update_description(self, new_description):
        self.description = new_description
        return f"{self.name} description was updated"
        
category = Category("mangoess", "ripe medium-size")
add_product_result = category.add_product("oranges")
print(add_product_result)
update_description_result = category.update_description("green oranges")
print(update_description_result)
remove_product_result = category.remove_product("oranges")
print(remove_product_result)