import multiprocessing


# Creating a Global Variable
results = []


def calc_square(numbers):
    global results
    for i in numbers:
        print('square: ', str(i*i))
        results.append(i*i)
        print('within a result: '+str(results))


if __name__ == "__main__":
    arr = [2, 3, 8, 9]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    # creating one Process here p1
    p1.start()
    # starting Processes here parallel by using start function.
    p1.join()
    # this join() will wait until the calc_square() function is    finished.
    print('result : '+str(results))
    # This print didn't work here we have to print it within the process
    print('Success')

