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

def sum_series_list(list,first=0,second=1):
    return [sum_series(num,first,second) for num in list]
print(sum_series_list([4,5,7,3],2,1))