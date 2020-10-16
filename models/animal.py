class Animal():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, status, breed, location_id, customer_id):
        self.id = id
        self.name = name
        self.status = status
        self.breed = breed
        self.locationId = location_id
        self.customerId = customer_id
        self.location = None