def log_base2(x):
    z = 0
    y = 2
    r = 1
    while y <= x:
        r = x-y
        y = y*2
        z = z+1
    print("z is {}".format(z))
    print("r is {}".format(r))
    print("2^{0} + {1} = {2}".format(z, r, x))


function_input = int(input("Please enter your number: "))
log_base2(function_input)
