class Vehicle:
    def __init__(self, vehicle_id= None,make=None , model=None):
        #initializes these variables only
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.rented_vehicle = False

    def create_a_new_vehicle(self):
        self.vehicle_id= input("Enter vehicle id: ")
        self.make= input("Enter make : ").lower()
        self.model= input("Enter model : ").upper()

    def rent_a_vehicle(self):
        self.rented_vehicle = True
        #prevent a rented vehicle from being rented


    def return_a_vehicle(self):
        pass

    def search_for_vehicle(self):
        pass

