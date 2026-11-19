from abc import ABC,abstractmethod


#ABSTRACTION AND INHERITANCE 
class Vehicle(ABC):
    def __init__(self,registration_no,owner_name):
        self.registration_no = registration_no 
        self.owner_name = owner_name 


    def view_vehicle_details(self):
        return f"{self.owner_name}-{self.registration_no}"


    @abstractmethod 
    def calculate_parking_fee(self,hours):
        pass 




class Bike(Vehicle):
    hourly_fee = 30
    def calculate_parking_fee(self, hours):
        cls = type(self)
        return hours*cls.hourly_fee

    



class Car(Vehicle):
    hourly_fee = 50
    def calculate_parking_fee(self, hours):
        cls = type(self)
        return hours*cls.hourly_fee




