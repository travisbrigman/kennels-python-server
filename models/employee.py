class Employee():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, name, location_id, animal_id):
        self.name = name
        self.location_id = location_id
        self.animal_id = animal_id