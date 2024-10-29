class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # This makes the class iterable
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
rectangle = Rectangle(5, 10)

# Iterating over the rectangle instance
for dimension in rectangle:
    print(dimension)
