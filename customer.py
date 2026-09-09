# The Customer class represents a customer in the vehicle management system. Each customer object has its own personal details that will store information about the customer. 
# The customer class also does not contain the list of rented vehicles, as this information can be found in the rental class.
class Customer:
    def __init__(self, customer_id, customer_name, phone_number,email, driver_license):
        #Adding validation to customer_id, customer_name, driver_license, and phone_number to ensure that an incomplete customer records are not
        #stored in the system.
        if not customer_id:
            raise ValueError("Customer ID cannot be empty.")
        if not customer_name:
            raise ValueError("Customer name cannot be empty.")
        if not driver_license:
            raise ValueError("Driver license cannot be empty.")
        if not phone_number:
            raise ValueError("Phone number cannot be empty.")

        self.customer_id = customer_id
        self.customer_name = customer_name
        self.phone_number = phone_number      # Phone number and email are kept separate so that each can be validated and displayed independently. 
        self.email = email
        self.driver_license = driver_license

    # Display the customer information in a format that will be easy to read by the user.
    def display_customer_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email Address: {self.email}")
        print(f"Driver License: {self.driver_license}")

