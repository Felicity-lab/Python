# is_raining = False
# is_cold = False

# if is_raining:
#     print("You will need an umbrella today!")

# if is_cold:
#     print("You will need a jumper today!")    

# temperature = 16

# if temperature < 12:
#     print("OMG it is actually slightly cool in Perth")
# else:
#     print("ugh when can I wear my jeans?!?!?")

# numbers and if else
# is_raining = False
# temperature = 16
# windchill = 4
# is_cold = temperature - windchill < 16
# print(is_cold)

# if is_cold:
#     print("You will need a jumper today!")
# else:
#     print("No need for a jumper")

# # nesting if statements
# if is_cold and is_raining:
#     print("Just stay home.")
# else:
#     if is_raining:
#         print("You will need an umbrella today!")
#     if is_cold:
#         print("You will need a jumper")

# if, elif and else
is_raining = False
temperature = 16
windchill = 4
is_cold = temperature - windchill < 16
print(is_cold)
is_hot = temperature - windchill > 25

if is_cold:
    print("You definitely need a jersey today")

elif is_hot:
    print("euck, stay indoors, its blazing hot outside!!")
else:
    print("Have an awesome day!!!")
