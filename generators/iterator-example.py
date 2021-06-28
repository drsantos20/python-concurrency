

# Traditional Way
x = [1, 2, 3, 4, 5]
for i in x:
    print(i)


# Same thing, but different
x = [1, 2, 3, 4, 5]
y = iter(x)
try:
    while True:
        print(next(y))
except StopIteration as e:
    pass
