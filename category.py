class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []
    def add_product(self, product):
        if product in self.products:
            self.products.append(product)
            return f"{name} was added into the category"
        else:
            return f"{name} Already exist"
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            return f"{name} Is removed from the category"
        else:
            return f"{name}does not exist in this category"
    def update_description(self, new_description):
        self.description = new_description
        return f"{name} description was updated"
        category=new Category(name)


        category= Category("mangoes","ripe medium-size")
        category.name("oranges")
        category.description("green oranges")
