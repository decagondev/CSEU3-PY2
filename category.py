class Category:
    def __init__(self, name): #TODO: , products)
        self.name = name

    def __str__(self):
        return f'No products available in {self.name}'