# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == 'spam':
#         break
#
#     print("Buy " +item)

meal = ["egg", "bacon", "spam", "sausages"]
nastyFoodItem = ''

for item in meal:
    if item == 'spam':
        nastyFoodItem = item
        break
else:
    print("I'll have a plate of that, then, please")

if nastyFoodItem == 'spam':
    print("Can't I have anything without spam in it?")
