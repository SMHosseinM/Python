# Write a small program to ask for a name and an age
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31)
# If they are, welcome them to the holiday, otherwise print
# a (polite) message repudiating them entry.

name = input("Please enter your name: ")
age = int(input("Please enter you age {0}: ".format(name)))
# if 18<= age <=30:
if age >= 18 and age <= 30:
    print("You are welcome to club 18-30 holiday {0}.".format(name))
else:
    print("""Sorry {0},
you are not between the desire age to go on holiday""".format(name))
