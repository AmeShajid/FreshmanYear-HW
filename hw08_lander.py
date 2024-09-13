#Ame Shajid 
# 3/12/2024
# Prompt: There were many computer games developed in the 1970s that allowed players to simulate the moon landing. The goal was to pilot the lunar lander to a safe landing. In this lab, you will make a version of this game.

#this function askFuel ask the user to enter the amount of fuel to use.
def askFuel(currentFuel):
    # this part makes sure the value is a positive integer and does not exceed the available fuel.
    while True:
        try:
            fuel = int(input("Enter units of fuel to use: \n"))
            if fuel < 0:
                print("Cannot use negative fuel.")
            elif fuel > currentFuel:
                print(f"Not enough fuel. Max Fuel: {currentFuel}")
            else:
                return fuel
        except ValueError:
            print("Please Enter Integer Value.")

def playLevel(name, G, fuel):
    # This function simulates a lunar landing level.
    # It displays the initial setup for the level and enters a loop until the altitude is 0.
    print(f"Entering Level {level}")
    print(f"Landing on {name}")
    print(f"Gravity is {G:.2f} m/s^2")
    print(f"Initial Altitude: 50 meters")
    print(f"Initial Velocity: 0.00 m/s")
    print(f"Burning a unit of fuel causes 0.10 m/s slowdown.")
    print(f"Initial Fuel Level: {fuel} units")
    print("")
    print("GO")
    
    altitude = 50
    velocity = 0
    seconds = 0
    
    # Simulation loop until the lunar lander reaches the surface.
    while altitude > 0:
        fuelToBurn = askFuel(fuel)
        fuel = fuel - fuelToBurn
        velocity = velocity + G + 0.10 * fuelToBurn
        altitude = altitude + velocity
        seconds += 1


        # Display the current status during each iteration.
        if seconds > 0:
            print(f"After {seconds} seconds Altitude is {altitude:.2f} meters, velocity is {velocity:.2f} m/s. \nRemaining Fuel: {fuel} units.")

    # Check if the landing was successful or not.
    if -2 <= velocity <= 2:
        print("Landed Successfully.")
    else:
        print("Crashed!")
        # so right here I tried adding the feature where once it crashed it would ask you:
        # choice1 =input(f"Do you want to play level {level}? (yes/no) \n") 
        #if choice1.lower() == "no":
            #print(f"You made it past {level-1} levels. \nThank you for playing.")
        #this is what I want to do but everytime I would try to stop or break it, it wouldn't work so I will be stright up basically even if you crash idk how to make it ask you the same level again it just keeps moving you on

# Main game loop to navigate through levels.
#should i put if __name__ == __main__:? 
print("Welcome to Lunar Lander Game.")
level = 1
while level <= 11:
    choice = input(f"Do you want to play level {level}? (yes/no) \n")
    if choice.lower() == "yes":#lower because its only has us check for yes and not all others
        # Launch the corresponding level based on the current level.
        #these are all the possible levels we have
        if level == 1:
            playLevel("Moon", -1.622, 150)
        elif level == 2:
            playLevel("Earth", -9.81, 5000)  
        elif level == 3:
            playLevel("Pluto", -0.42, 5000)   
        elif level == 4:
            playLevel("Neptune", -14.07, 5000)  
        elif level == 5:
            playLevel("Uranus", -10.67, 5000)  
        elif level == 6:
            playLevel("Saturn", -11.08, 5000)  
        elif level == 7:
            playLevel("Jupiter", -25.95, 5000)  
        elif level == 8:
            playLevel("Mars", -3.77, 5000)  
        elif level == 9:
            playLevel("Venus", -8.87, 5000)  
        elif level == 10:
            playLevel("Mercury", -3.59, 5000)  
        elif level == 11:
            playLevel("Sun", -274.13, 5000)  
        level += 1
    else:
        break#if they enter no then we stop the code and just print the following or I could just put the print in there 

print(f"You made it past {level-2} levels. \nThank you for playing.")


#another problem I ran into is when it is the last second it always goes negative and calculates it and never goes to 0