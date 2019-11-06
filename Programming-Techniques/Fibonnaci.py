import time

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fibonacci2(n):
    fibNumbers = [0,1]
    for i in range(2,n+1):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
    return fibNumbers[n]

number = int(input("Please enter a number "))

startTime1 = time.perf_counter()
endTime1 = time.perf_counter()
startTime1
print(fib(number))
endTime1
print(endTime1)

startTime2 = time.perf_counter()
endTime2 = time.perf_counter()
startTime2
print(fibonacci2(number))
endTime2
print(endTime2)
