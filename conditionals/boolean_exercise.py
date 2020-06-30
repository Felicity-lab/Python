#Que1
moths_in_house = True
print("Get the moths!")

moths_in_house = False
print("No threats detected")

#Que2
moths_in_house = True
mitch_is_home = True
print("Hoooman! Help me get the moths!")

moths_in_house = False
mitch_is_home = False
print("No threats detected.")

moths_in_house = True
mitch_is_home = False
print("Meoooooooow! Hissssssss!")

moths_in_house = False
mitch_is_home = True
print("Climb on Mitch")

#Que3
light_colour = "Red" 
car_detected = False 

print()

light_colour = "Red" 
car_detected = True 
print("Flash!")

light_colour = "Green" 
car_detected = False 
print()

light_colour = "Green" 
car_detected = True 
print()

light_colour = "Amber" 
car_detected = False 
print()

light_colour = "Amber" 
car_detected = True 
print()

#Que4
height = int(input('How tall are you? '))
print(height)

if height <= 50 and height <= 119:
    print('Sorry, not today :(')

elif height >= 120 and height <= 191:
    print('Hop on!')

# elif height == 191:
    # print('Hop on!')

else:
    print()