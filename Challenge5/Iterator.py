# Create a list of items (you may use either strings or numbers in the list)
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.

courses = ["Distributed system", "Java programming", "Maths", "Computation"]
# Making an iterator
courses_iterator = iter(courses)
counter = 0
while counter < len(courses):
    print(next(courses_iterator))
    counter += 1
