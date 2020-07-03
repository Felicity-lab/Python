# Que1
foods = ["orange","apple","banana","strawberry","grape","blueberry",
["carrot", "cauliflower", "pumpkin"],
"passionfruit","mango","kiwifruit"
]

print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
print(foods[-3:])
print(foods[6][2])


# Que2

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
    
lst=[]    
name1=input("Please enter 1st name: ") 
lst.append(name1)
name2=input("Please enter 2nd name: ") 
lst.append(name2)
name3=input("Please enter 3rd name: ") 
lst.append(name3)
print(lst)

#Que4 

grociers=[
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

for i in range(len(grociers)): 
    #print(i)
    
    price=round(float(grociers[i][1])*float(userList[i]),2)
    
    lst=(grociers[i][0])
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

