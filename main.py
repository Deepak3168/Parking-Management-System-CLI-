from parking.parking_lot  import ParkingLot  
from vehicle import Bike,Car

car_lot = ParkingLot()
bike_lot = ParkingLot()

for i in range(20):
    bike_lot.register()
    car_lot.register()


vehicles=set()

issued_tickets = []

def print_issued_tickets(tickets):
    for i,ticket in enumerate(tickets):
        print("Token:",i,"Ticket:",ticket)

def park_vehicle_in_lot(lot,vehicle_class):
    lot.show_parking_slots()
    duplicate = True 
    while duplicate :
        reg_no = input("Enter vehicle Registration no ")
        if reg_no not in vehicles : 
            vehicles.add(reg_no)
            duplicate = False 
        else:
            print("Vehicle with Registration Number already exist ")
    owner_name  = input("Enter name ")
    invalid = True
    while invalid:
        slot_index = int(input("Enter Slot"))
        try:
            parking_slot = lot.parking_slots[slot_index]
        except IndexError as e : 
            print(e)

        message,ticket = lot.park_vehicle(parking_slot,reg_no,owner_name,vehicle_class)
        print(message)
        issued_tickets.append(ticket)

        if ticket : 
            invalid = False
    return message,ticket
   

billing = True

while billing : 
    print("""
        ===================================
            PARKING LOT MANAGEMENT
        ===================================
        1. Park Vehicle
        2. Display Available Slots
        3. Remove Vehicle
        4. Display Parked Vehicles
        5. View Parking History
        . Generate Parking Receipt
        6. Exit

        ===================================
        Enter your choice:
    """)

    op = int(input("Enter your operation"))

    if op == 1 : 
        print("1) Bike ")
        print("2) Car ")
        type = int(input("Enter Vehicle Type"))
        if type == 1 : 
            message,ticket = park_vehicle_in_lot(bike_lot,Bike)
            print(message)
        elif type == 2 :
            park_vehicle_in_lot(car_lot,Car)
        else:
            print("Invalid Type")
    elif op == 2 : 
        print("1) Bike")
        print("2) Car")
        type = int(input("Enter Vehicle Type"))
        if type == 1 : 
            bike_lot.display_available_parking_slots()
        elif type == 2 :
            car_lot.display_available_parking_slots()
        else:
            print("Invalid Type")
    elif op == 3 :
        print("1) Bike")
        print("2) Car")
        type = int(input("Enter Vehicle Type"))
        if type == 1 : 
            print_issued_tickets(issued_tickets)
            ticket_index = int(input("Enter index of issued ticket"))
            ticket = issued_tickets[ticket_index]
            print(bike_lot.release_vehicle(ticket)) 
        elif type == 2 :
            print_issued_tickets(issued_tickets)
            ticket_index = int(input("Enter index of issued ticket"))
            ticket = issued_tickets[ticket_index]
            print(car_lot.release_vehicle(ticket))
        else:
            print("Invalid type ")

    elif op == 4 : 
        print("1) Bike")
        print("2) Car")
        type = int(input("Enter Vehicle Type"))
        if type == 1 :
            print(bike_lot.display_parked_vehicles())
        elif  type == 2 : 
            print(car_lot.display_parked_vehicles())

        else:
            print("Invalid Type")


    elif op == 5:
        print("1) Bike")
        print("2) Car")
        type = int(input("Enter Vehicle Type"))
        if type == 1 :
            bike_lot.display_parking_history()
        elif type==2 :
            car_lot.display_parking_history()
        else:
            print("Invalid Type")

    elif op == 6 :
        billing = False 

    else:
        print("Invalid Operation")





         


        





