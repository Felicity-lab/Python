name = input("What is your name? ")
print(name)

age_prompt =f"Hi {name}, how old are you? "
age = input(age_prompt)

years_until_100 = 100 - int(age)

print(f"Wow! {name}, you will be 100 in {years_until_100} years!")