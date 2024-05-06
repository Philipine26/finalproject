



# import utils
import utils
from Batmobile import Batmobile

batmobile = True

#TODO: Create a method to get the input
def main():
    
    #TODO: Get the title
    print(utils.title("  Batmobile Life Saver  "))
    
    #TODO: Get input
    name = input("Enter Pilot's name: ")
    color = input("What is the vehicule color: ")
    capacity = utils.get_int("Enter the maximun capacity: ")
    speed = utils.get_float("Enter maximum speed: ")
    print("")
    
    #TODO: Get a car object
    my_batmobile = Batmobile(name, color, capacity, speed)
    
    #TODO: Share the information by print
    print(f"{name} has a {color} Batmobile that can contain {capacity} max. It has a maximum speed of {speed}.")
    print("")

    # Create the loop
    while batmobile == True:
        # Get the user input
            command = input("(T)ake off | (A)ccellerate | (D)ecelerate | (E)ject | (L)and | e(X)it: ")
            
            # Loop to choose a command
            if command == 't':
            
                # Demonstrate method take off
                my_batmobile.take_off()

            elif command == 'a':
            
                # Demonstrate method accelerate
                my_batmobile.accelerate()

            elif command == 'd':
            
                # Demonstrate method decelerate
                my_batmobile.decelerate()

            elif command == 'e':
            
                # Demonstrate method eject
                my_batmobile.eject()
            
            elif command == 'l':
            
                # Demonstrate method land
                my_batmobile.land()

            # Get out of the loop
            elif command == 'x':
                print("Thank to have help with the Batmobile")
                break



if __name__ == "__main__":
    main()