counter = 10

while counter > 0:
    print(counter)
    if  counter%2 == 0:
        print(f"{counter} is an even number.")
    else:
        print(f"{counter} is an odd number.")
    counter = counter - 1