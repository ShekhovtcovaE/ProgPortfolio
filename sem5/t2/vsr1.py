import itertools

def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

max = int(input('Enter max '))
first_ten_fibs = list(itertools.islice(fibonacci(), max))

print(first_ten_fibs)
