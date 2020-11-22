class Solution:
    def fib(self,num):
        n0 = 0
        n1 = 1
        if num <= 0:
            print("The requested series is",n0)
        else:
            print(n0, '\n', n1)
            for x in range(2, num):
               n2 = n0 +n1
               print(n2)
               n0 = n1
               n1 = n2

    def fib2(self,n):
        a,b = 0,1
        for i in range(0,n):
            print(a)
            a,b = b, a+b

    def fib_rec(self,n):
        if n <= 1:
            return n
        else:
            return(self.fib_rec(n - 1) + self.fib_rec(n - 2))

s = Solution()
for i in range(6):
       print(s.fib_rec(i))
#print(s.fib_rec(6))