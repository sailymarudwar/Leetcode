def fib(num):
    n0 = 0
    n1 = 1
    if num <= 0:
        print("The requested series is",n0)
    else:
        print(n0 + '\n' + n1)
        for x in range(2, num):
           n2 = n0 +n1
           print(n2)
           n0 = n1
           n1 = n2
fib(5)