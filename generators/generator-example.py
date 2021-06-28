# A simple generator function
def my_gen():
    n = 1
    print('Primeiro print, n e igual a {}'.format(n))
    # Generator function contains yield statements
    yield n

    n += 1
    print('Segundo print, n e igual a {}'.format(n))
    yield n

    n += 1
    print('Terceiro e ultimo print , n e igual a {}'.format(n))
    yield n
