a=6

def fib(num):
    if num <= 1:
        if num == 0:
            return 0
        else: 
            return 1
            
    return fib(num-1) + fib(num-2)

def lucas(num):
    if num <= 1:
        if num == 0:
            return 2
        else: 
            return 1
            
    return lucas(num-1) + lucas(num-2)

def sum_series(n,first=0,second=1):
    if n <= 1:
        if n == 0:
            return first 
        else: 
            return second
            
    return sum_series(n-1,first,second) + sum_series(n-2,first,second)

print(sum_series(7,3,9))
