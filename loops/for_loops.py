# tea_collection = [
#     "Earl Grey",
#     "Melbourne Breakfast",
#     "Chai",
#     "Peppermint",
#     "Lemon and Ginger",
#     "Strawberry Cream",
#     "Chamomile",
#     "Green",
#     "Dandelion"
# ]

# for tea in tea_collection:
#     print(tea)
#     #    print(type(tea))
#     print(f"I have {tea} flavoured tea.")

# print("ended loop")

# for index in range(0,10):
#     print(index)

# print()

# for index in range(0,50, 5):
#     print(index)

#     for index,tea in enumerate(tea_collection):
#         print(index, tea)

tea_collection = [
    ["Black", "Earl Grey", "Melbourne Breakfast", "Chai"],
    ["Flavoured", "Peppermint", "Lemon and Ginger", "Strawberry Cream"],
    ["Health", "Chamomile", "Green", "Dandelion"]
]

for tea_category in tea_collection:
    print(f"{tea_category[0]} Teas:")
    for tea in tea_category[1:]:
        print(f"    {tea}")

groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

for item in groceries:
    print(f"{item[0]:<20} ${item[1]:.2f}")