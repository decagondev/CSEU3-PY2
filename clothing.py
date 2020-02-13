from product import Product

class Clothing(Product):
    def __init__(self, name, price, colour, size):
        super().__init__(name, price)
        # call 56343 + offset(4)
        self.colour = colour
        self.size = size

# p = Product(...) ==> p -> 34321
# c = Clothing(...) ==> c -> 12345 super() -> 56343


# p count = 2
# c count = 1