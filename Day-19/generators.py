def display():
    l = ['10..50', '50..100', '101..150', '151..200']

    yield l[0]
    yield l[1]
    yield l[2]
    yield l[3]

scroll = display()

print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))

10..50
50..100
101..150
151..200
