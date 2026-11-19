from .parking_slot import ParkingSlot
from .parking_ticket import ParkingTicket
from datetime import datetime,timedelta

class ParkingLot:
    def __init__(self):
        self.parking_slots = [] 
        self.parking_records = [] 


    def register(self):
        slot = ParkingSlot()
        self.parking_slots.append(slot)
        return slot


    def show_parking_slots(self):
        print("============ PARKING SLOTS ======================")
        for i,parking_slot in enumerate(self.parking_slots) : 
            print(f"{i} , {parking_slot.slot_number} - {parking_slot.get_availability_status()}")

        print("==================================================")
        return "DONE"


    @staticmethod
    def park_vehicle(parking_slot,vehicle_registration_no,owner_name,type):
        try : 
            #creating a vehicle
            vehicle = type(registration_no=vehicle_registration_no,owner_name=owner_name)
            parking_slot.park_vehicle(vehicle)
            entry_time = datetime.now()
            parking_ticket = ParkingTicket(vehicle,parking_slot,entry_time)
            
            return "VEHHICLE PARKED",parking_ticket
        except ValueError as e : 
            return e ,None




    def release_vehicle(self,parking_ticket):
        try:
            parking_slot = parking_ticket.get_parking_slot()
            parking_slot.remove_vehicle()
            current_time = datetime.now()+timedelta(hours=3)
            parking_ticket.set_exit_time(current_time)
            print(parking_ticket.generate_parking_reciept())
            self.parking_records.append(parking_ticket)
            return "VEHICLE RELEASED"
        except ValueError as e :
            return e

    def display_available_parking_slots(self):
        print("================ AVAILABLE SLOTS ======================")

        for parking_slot in self.parking_slots :
            if parking_slot.get_availability_status() : 
                print(parking_slot)

        return "DONE"

    def display_parked_vehicles(self):
        print("================ PARKED VEHICLES  ======================")
        for parking_slot in self.parking_slots :
            if not parking_slot.get_availability_status() : 
                print(parking_slot.parked_vehicle_information())
        return "DONE"

    def display_parking_history(self):
        print("======================== PARKING HISTORY ==================")
        for parking_record in self.parking_records :
            print(parking_record.get_record())

        print("============================== END OF THE LINE ================================")


    

    
        

            


        