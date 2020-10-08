class Location():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, name, address, capacity):
        self.name = name
        self.address = address
        self.capacity = capacity
        