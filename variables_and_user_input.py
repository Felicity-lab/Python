#Que1 Addition
x = 3
y = 9
print(x + y)


x = -3
y = 9
print(x + y)

x = 3.0
y = -9
print(x + y)


#Que2 Multiplication
x = 3
y = 9
print(x * y)

x = -3
y = 9
print(x * y)

x = 3.0
y = -9
print(x * y)

#Que3 distance conversion

# # distance = input("Enter distance : ")
kilometers = int(input("Enter value in kilometers: "))
conv_fac = 1000
conv_fac2 = 100000

if kilometers == 10:

    meters = kilometers * conv_fac
    print('%0.2f kilometers is equal to %0.2f meters' %(kilometers,meters))

    cm = kilometers * conv_fac2
    print('%0.2f kilometers is equal to %0.2f centimeters' %(kilometers,cm))

else:
    print("Have an awesome day!!!")


    
kilometers = float(input("Enter kilometers float value : "))
conv_fac = 1000
conv_fac2 = 100000

if kilometers == 5.4:

    meters = kilometers * conv_fac
    meters = float(meters)
    print('%0.2f kilometers is equal to %0.2f meters' %(kilometers,meters))

    cm = kilometers * conv_fac2
    print('%0.2f kilometers is equal to %0.2f centimeters' %(kilometers,cm))

else:
    print("Have an awesome day!!!")


#Que4 Name and height
name = input("What is your name? ")
height = int(input("What is your height in cm? "))


if name == "William" and height == int(192):
    print (f" {name} is" f "{height}cm tall!" %(name,height))
elif name == "Roary" and height == 27:
    print ("Roary is 27cms tall.")
else:
    print(f"Hi, {name} have a great day")
