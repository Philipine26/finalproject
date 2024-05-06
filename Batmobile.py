"""
Name: Batmobile.py
Author:Philipine
Created:5/6/2024
Purpose: Make the Batmobile works """


# Ceate a class
class Batmobile:
    #TODO: Create a method to initialize the attributes 
    def __init__(self, name, color, capacity, speed):
        self._name = name
        self._color = color
        self._capacity = capacity
        self._speed = speed 


    

    #TODO: Create methods to make the batmobile move
    def take_off(self):
        print("The Batmobile is taking off")

    def accelerate(self):
        self._speed += 50 
        print(f" Current speed is : {self._speed}")
        
    def decelerate(self):
        self._speed -= 50
        if self._speed < 0:
            self._speed = 0
        
        print(f" Current speed is : {self._speed}")

    def eject(self):
        print(f"{self._name} has been eject from the vehicule ")

    def land(self):
        print(" The Batmobile is landing")
