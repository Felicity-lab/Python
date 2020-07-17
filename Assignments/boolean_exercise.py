#Que1
moths_in_house = True
print("Get the moths!")

moths_in_house = False
print("No threats detected")

#Que2
moths_in_house = True
mitch_is_home = True

if moths_in_house and mitch_is_home:
    print("Hoooman! Help me get the moths!")

elif not moths_in_house and not mitch_is_home:
    print("No threats detected.")

elif moths_in_house and not mitch_is_home:
    print("Meoooooooow! Hissssssss!")

elif not moths_in_house and mitch_is_home:
    print("Climb on Mitch")


#Que3
light_colour = "Red" 
car_detected = False 

if light_colour == "Red" and not car_detected:
    print("Do nothing.")

elif light_colour == "Red" and car_detected:
    print("Flash!")

elif light_colour == "Green" and not car_detected:
    print("Do nothing.")

elif light_colour == "Green" and car_detected:
    print("Do nothing.")

elif light_colour == "Amber" and not car_detected:
    print("Do nothing.")

elif light_colour == "Amber" and car_detected:
    print("Do nothing.")

else:
    print("Do nothing")

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
