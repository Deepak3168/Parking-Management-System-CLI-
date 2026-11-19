
class ParkingTicket:
    ticket_id = 0
    def __init__(self,vehicle,parking_slot,entry_time):
        ParkingTicket.ticket_id+=1
        self.__ticket_id = ParkingTicket.ticket_id
        self.__vehicle = vehicle 
        self.__parking_slot = parking_slot 
        self.__entry_time = entry_time 
        self.__record = None 
        self.__locked_charge = None 
        self.__exit_time = None

    def calculate_parking_duration(self):
        diff = self.__exit_time - self.__entry_time  
        return diff.total_seconds()/3600 


    def set_record(self):
        self.__record = f"{self.__vehicle.registration_no} - {self.__vehicle.owner_name} - {self.__parking_slot.slot_number} - {self.calculate_parking_duration()} - {self.__locked_charge}"


    def calculate_total_parking_charges(self):
        hours = self.calculate_parking_duration()
        charge = self.__vehicle.calculate_parking_fee(hours=hours)
        return charge

    def set_locked_charge(self):
        self.__locked_charge = self.calculate_total_parking_charges()



    def generate_parking_reciept(self):
        if self.__record is None : 
            self.set_locked_charge()
            self.set_record()
            return f"""
                ============= PARKING RECEIPT =============

                    Ticket ID         : {self.__ticket_id}
                    Registration No   : {self.__vehicle.registration_no}
                    Vehicle Type      : {self.__vehicle.__class__.__name__}
                    Parking Slot      : {self.__parking_slot.slot_number}

                    Entry Time        : {self.__entry_time.strftime("%A, %d %B %Y %I:%M %p")}
                    Exit Time         : {self.__exit_time.strftime("%A, %d %B %Y %I:%M %p")}
                    Duration          : { round(self.calculate_parking_duration(),2)} Hours

                    Parking Rate      : {self.__vehicle.__class__.hourly_fee}
                    Total Amount      : {round(self.calculate_total_parking_charges(),2)}

                    ============================================
                            THANK YOU!
                    ============================================
            """
        else : 
            return self.__record


    def set_exit_time(self,current_time):
        self.__exit_time = current_time 

    def get_record(self):
        return self.__record

    def get_parking_slot(self):
        return self.__parking_slot 

    def __str__(self):
        return f"{self.__parking_slot.slot_number} - {self.__vehicle.registration_no}"
    

 



