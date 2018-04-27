# myList = list(range(10))
# print(myList)
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
#
# print(even)
# print(odd)

# myString = "abcdefghijklmnopqrstuvqxyz"
# print(myString.index('e'))
# print(myString[4])
#
# smallDecimals = range(0, 10)
# print(smallDecimals)
#
# print(smallDecimals.index(3))
#
# odd = range(1, 10000, 2)
# print(odd)
#
# print(odd[985])
#
# sevens = range(7, 1000000, 7)
# x = int(input("Please enter a positive number less than one million: "))
# if x in sevens:
#     print("{} is divisible by seven".format(x))
#
# print(smallDecimals)
#
# myRange = smallDecimals[::2]
# print(myRange)
# print(myRange.index(4))
#
# decimals = range(0, 100)
# myRange = decimals[3:40:3]
# print(myRange == range(3, 40, 3))
# print(range(0, 5, 2) == range(0, 6, 2))
# print(list(range(0, 5, 2)))
# print(list(range(0, 6, 2)))
#
# r = range(0, 100)
# print(r)
#
# # The following two commands are identical
#
# for i in r[::-2]:
#     print(i)
#
# print('=' * 50)
# for i in range(99, 0, -2):
#     print(i)
#
# print('=' * 50)
# print(range(0, 100)[::-2] == range(99, 0, -2))

backString = "egaugnal lufrewop yrev a si nohtyP"
print(backString[::-1])

r = range(0, 10)
for i in r[::-1]:
    print(i)
