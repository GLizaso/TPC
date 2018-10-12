
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


i=0
serie = []

while True:

    if fib(i)%2 == 1:
        serie.append(fib(i))
    i=i+1

    if fib(i)> 10**6:
            break

suma = sum(serie)
print(suma)


