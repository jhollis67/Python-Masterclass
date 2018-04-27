# combining dictionaries using the .update method
fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in branches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {"cabbage": "every child's favorite",
       "sprouts": "mmmmm, lovely",
       "spinach": "can I have some more fruit, please"}

print(veg)

# veg.update(fruit)
# print(veg)  # can also so fruit.update(veg), either works
#
# print(fruit.update(veg))
# print(fruit)

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
print(veg)
print(fruit)