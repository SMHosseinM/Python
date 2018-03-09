# Create a program that takes an IP address entered at the keyword
# and print out the number of segments it contains, and the length of each segment.

# An IP address consists of 4 numbers, separated from each other with a full stop. But
# your program should just count however many are entered
# Example of the input you may get are:
#     127.0.0.1.
#     .192.168.0.1
#     10.0.123456.255
#     172.16
#     255
#
# So your program should even work with invalid IP addresses. We're just interested in th
# number of segments and how long each one is.
#
# Once you have a working program, here are some suggestions for invalid input to test.
#     .123.45.678.91
#     123.4567.8.9.os
#     123.156.289.10123456
#     10.10t.10.10
#     12.9.34.6.12.90
#     ''-that is, press enter without typing anything
#
# This challenge is intended to practise for loops and if/else statements, so although
# you could use other techniques (such as splitting the string up), that's not the
# approach we're looking for here

IP = input("Please enter the IP address: ")
if IP[-1] != ".":
    IP += "."
numberOfSegments = 0
segmentLength = 0
segmentLengthContainer = ""
validInput = False

for char in IP:
    if char in "0123456789":
        segmentLength += 1
        continue
    else:
        segmentLengthContainer += str(segmentLength)
        numberOfSegments += 1
        if validInput is False:
            if numberOfSegments != 4:
                validInput = True
        segmentLength = 0

print("The number of elements are: {0}".format(numberOfSegments))
print()
if IP[0] == "." or validInput is True:
    print("The IP is invalid")
print()
for i in range(0, len(segmentLengthContainer)):
    print("The length of the {0} is: {1}".format(i+1, segmentLengthContainer[i]))



