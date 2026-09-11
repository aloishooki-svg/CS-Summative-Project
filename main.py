from vehicle import Vehicle

vehicle_list = []


program_is_on = True

def add_vehicle():
    vehicle=Vehicle()
    vehicle.create_a_new_vehicle()
    vehicle_list.append(vehicle)


def list_of_vehicles():
    for vehicle in vehicle_list:
        print(vehicle)

while program_is_on:
    add_vehicle()
    add_vehicle()

    list_of_vehicles()


    program_is_on = False

