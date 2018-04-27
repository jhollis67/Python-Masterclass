# string = "1234567890"

# for char in string:
#     print(char)
# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
#
# print(next(my_iterator))

# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(char)




# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function
#
# Use a loop to loop "n" times, where n is the number of items in the list.
# Each time around the loop, use next() on your list to print the next item.
#
# Hint: use the len() function rather than counting the number of items in the list.





# stringChallenge = "12345678"
# stringIterator = iter(stringChallenge)
# for i in range(0, len(stringChallenge)):
#     nextItem = next(stringIterator)
#     print(nextItem)

myList = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
myIterator = iter(myList)
n = 0

while n < len(myList):
    print(next(myIterator))
    n += 1