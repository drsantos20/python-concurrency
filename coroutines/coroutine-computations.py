def func():
    x = 5
    print('Function Part 1')

    yield x
    x += 7
    print('Function part 2')

    yield x

    print('Function part 3')


try:
    # main function
    y = func()

    z = next(y)		# Function part 1 executed
    print(z)

    z = next(y)		# Function part 2 executed
    print(z)

    z = next(y)		# Function part 3 executed and StopIteration exception raised
    print(z) 	 	# This print will not be executed

except StopIteration as e:
    pass
