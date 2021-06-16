def fib_max(max):
    old = 0
    fib = 1
    while fib + old < max:
        t = fib
        fib = old + fib
        old = t
    return fib


class Fibonacci:

    def __init__(self, max):
        self.lim = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.lim:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

max = int(input('enter max '))
print(fib_max(max))
new_fib = Fibonacci(max)
for i in new_fib:
    print(i)
