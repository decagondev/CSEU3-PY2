class Category:
    def __init__(self, name, products = None):
        self.name = name
        self.products = products

    def __str__(self):
        return f'No products available in {self.name}'