def fib_it(n):#Through iteration
    f1=0
    f2=1
    print f1,f2,
    for i in range(2,n):
        f3=f1+f2
        print f3,
        f1=f2
        f2=f3

series = {0:0, 1:1} #to store the calculated values

def fib_rec(n): #Through recursion
    if n not in series:
        series[n] = fib_rec(n-1) + fib_rec(n-2)
    return series[n]

n=int(raw_input("Enter N"))
choice=1
while choice>=1 and choice<=2:
    print "1.Fibonacci through iteration"
    print "2.Fibonacci through recursion"
    choice=int(raw_input("Enter your choice"))
    if choice==1:
        fib_it(n)
    elif choice==2:
        fib_rec(n)
        for i in range(n+1):
            print series[i],
    else:
        print "Wrong choice"