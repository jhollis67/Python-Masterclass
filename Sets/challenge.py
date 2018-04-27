# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order
#
# You can either enter the text from the keyboard or
# initialize a string variable with a string

# ATTEMPT
string = set("I am learning some Python today")

string2 = string.difference("a", "e", "i", "o", "u")

print(sorted(string2))
print("=" * 100)


# ANSWER
sampleText = "Python is a very powerful language"

vowels = frozenset("aeiou")
finalSet = set(sampleText).difference(vowels)
# print(finalSet)

finalList = sorted(finalSet)
print(finalList)
