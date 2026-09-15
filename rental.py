class Rental:
    def __init__(self, rental_id, vehicle_id, customer_id, days, total_cost=0.0, is_active=True):
        self.rental_id = rental_id
        self.vehicle_id = vehicle_id
        self.customer_id = customer_id
        self.days = int(days)
        self.total_cost = float(total_cost)
        # True means the car is currently with the customer
        self.is_active = is_active

    def calculate_cost(self, daily_rate):
        # Figure out the price by multiplying days by the car's rate
        self.total_cost = self.days * daily_rate
        return self.total_cost

    def display_details(self):
        if self.is_active:
            status = "Active"
        else:
            status = "Completed"
            
        print(f"Rental #{self.rental_id} | Vehicle: {self.vehicle_id} | Customer: {self.customer_id} | Days: {self.days} | Total: ${self.total_cost} | {status}")

    def to_dictionary(self):
        return {
            "rental_id": self.rental_id,
            "vehicle_id": self.vehicle_id,
            "customer_id": self.customer_id,
            "days": self.days,
            "total_cost": self.total_cost,
            "is_active": self.is_active
        }