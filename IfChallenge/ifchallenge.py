name = input("What is your name? ")
age = int(input("How old are you, {}? ".format(name)))

if 18 <= age < 31:
    print("Welcome to the holiday, {0}!".format(name))
else:
    if age < 18:
        print("Sorry, you are too young for this holiday.")
    else:
        print("Sorry, you are too old for this holiday.")

