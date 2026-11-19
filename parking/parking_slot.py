
#ENCAPSULATION AND AGGREGATION 
 
class ParkingSlot:
    current_slot = 0
    def __init__(self,current_vehilce=None,availability_status=True):
        ParkingSlot.current_slot+=1
        self.slot_number = ParkingSlot.current_slot
        self.__availability_status = availability_status 
        self.__current_vehilce = current_vehilce


    
    def park_vehicle(self,vehilce):
        if self.__current_vehilce is None :
            self.__current_vehilce = vehilce 
            self.__availability_status = False
        else:
            raise ValueError("Cannot add Vehicle Since slot is not already booked")

    def remove_vehicle(self):
        if self.__availability_status is True  and self.__current_vehilce is None: 
            raise ValueError("Cannot Remove a vehicle which does not exist , slot is already available")
        else: 
            self.__current_vehilce = None 
            self.__availability_status = True 

    def currently_parked_vehicle_registration(self):
        return self.__current_vehilce.registration

    def get_availability_status(self):
        return self.__availability_status


    def __str__(self):
        return f"{self.slot_number } - {self.__availability_status }"

    def parked_vehicle_information(self):
        return f"{self.slot_number} - {self.__current_vehilce.registration_no} - {self.__current_vehilce.owner_name}"


    

