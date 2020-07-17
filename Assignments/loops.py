#Que1
# count = 0
# sum = 0
# number = 1
# num = []

# num1 = input("Please enter a number:")
# num.append(num1)
# num2 = input("Please enter another number:")
# num.append(num2)
# num3 = input("Please enter a 3rd number:")
# num.append(num3)
# num4 = input("Please enter a 4th number:")
# num.append(num4)
# print(num)

# count = 0
# sum = 0
# number = 1
# while number !=0:
#         number = int(input("enter a number? "))
#         if number < 8:
#             sum = sum + number
#             count += 1
#         elif sum < 8:
#             num2 = input("Please enter another number:")
#             sum = sum + num2
#             count += 1
#         elif sum < 8:
#             num3 = input("Please enter another number:")
#             sum = sum + num3
#             count += 1
#         pass
#           num.append(num2)


        # sum = sum + number
        # count += 1

print(sum)
# while True:
#     if num1 <= 8:
#         num2 = input("Please enter another number:")
#         num.append(num2)

# break
#     else: num2 = input("Enter another number: ")
#     if num1 and num2:

#     results = float(num1) + float(num2)
# print(results)

#Que2
mailing_list=[
        ["Roary", "roary@moth.catchers"], 
        ["Remus", "remus@kapers.dog"],
        ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
        ["Biscuit","biscuit@whippies.park"],
        ["Rory","rory@whippies.park"],
        ]
mailing_list
sent_str = ""
lst=[]
for i in mailing_list:
    sent_str=str(i[0])+':'+' '+str(i[1])
    lst.append(sent_str)

for j in lst:
    print(j)

#Que3
counter = 0
lst = []
counter = 0
while counter < 3:
    name = input("Please enter a name :")
    lst.append(name)
    counter = counter + 1
print(lst)

#Que4 
groceries = [
        ['Baby Spinach',2.78],
        ['Hot Chocolate', 3.70],
        ['Crackets',2.10],
        ['Bacon',9.00],
        ['Carrots',0.56],
        ['Oranges',3.08]
        ]

total=0   
lst=[] 
lst_total=[]
prc=[]
input_units = input("Enter units separated by space ")

print("\n")
userList = input_units.split()
    
for i in range(len(groceries)): 
    #print(i)
    price=float(groceries[i][1])*float(userList[i])
    
    lst=(groceries[i][0])
    lst_total.append(lst)
    prc.append(price)
    total+=price

mapped=zip(lst_total,prc)
mapped=list(mapped)

print("====Izzy' Food Emporium====")
for product, price in zip(lst_total,prc): 
    print ("%s    %d" %(product, price))

print('===========================')
print('The total is:',round(total,2))

