CUSTOMERS = [
    {
      "id": 1,
      "name": "Hannah Hall",
      "address": "7002 Chestnut Ct"
    },
    {
      "id": 2,
      "name": "David Johnson",
      "address": "124 Lynwood Ct"
    },
    {
      "id": 3,
      "name": "Lee LaVigne",
      "address": "11011 Baldwin Ave"
    },
    {
      "email": "travis1000@icloud.com",
      "password": "123",
      "name": "Travis Brigman",
      "id": 4
    }
]


def get_all_customers():
    return CUSTOMERS

    # Function with a single parameter

def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer