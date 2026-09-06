# The Customer class represents a customer in the vehicle management system. Each customer object has its own personal details that will store information about the customer. 
class Customer:
    def __init__(self, customer_id, customer_name, phone_number,email, driver_license):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.email = email
        self.driver_license = driver_license
# Phone number and email are kept separate so that each can be validated and displayed independently. 
# The customer class also does not contain the list of rented vehicles, as this information can be found in the rental class.

