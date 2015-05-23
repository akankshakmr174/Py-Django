# Program to find the Fibonacci series until N natural numbers using both recursion and iteration

N = int(raw_input("Enter the end number here "))
def fib(n) :  # Recursive function
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
print "Fibonacci series upto %d natural numbers" % N
for n in xrange(0,N):  # Iteration
    x = fib(n)
    print "%d +" % x, 
print fib(N)       # Printing 0 and fibonacci sequence upto N natural numbers 
                   # In total N+1 numbers in a series
