def recur_fib(n):
   if n <= 1:
       return n
   else:
       return(recur_fib(n-1) + recur_fib(n-2))

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


max = int(input())

# Генератор списков
list_fib = [recur_fib(i) for i in range(max)]
print(list_fib)

#функции с yield
yield_fib = fib(max)
for i in range(max):
    print(yield_fib.__next__())
    
