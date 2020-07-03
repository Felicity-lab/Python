number = input("Please enter a number  ")
while sum <= 8:

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
    
    price=round(float(groceries[i][1])*float(userList[i]),2)
    
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

