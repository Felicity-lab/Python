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
def my_list(): 
    request = input("Enter a string : ")
    li = list(request.split(" ")) 
    print(len(li), request.split())
    print(len(request), list(request))

    return li 
my_list() 

def my_list2(): 
    request = input("Enter a string : ")
    li = list(request.split(" ")) 
    print(len(li), request.split())
    print(len(request), list(request))

    return li 
my_list2() 


