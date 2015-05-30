
def fibonacci(f1,f2,sum1,n):
    sum1=f1+f2
    n=n+1
    if n==1:
        print "fibonacci series is: "+"0"
    elif sum1<n:
        f1=f2
        f2=sum1
        print sum1," ",
        fibonacci(f1,f2,sum1,n-1)

def fibno(f1,f2,k,sum1):
    if k==1:
        print "fibonacci series is: "+"0"
    else:
        while(sum1<k):
            f1=f2
            f2=sum1
            print sum1," ",
            sum1=f1+f2
c=raw_input("Enter a number: ")
f1=-1
f2=1
sum1=0
print "1.using recursion"
print "2.using iteration"
f=raw_input("enter ur choice: ")
if f==1:
    fibonacci(f1,f2,sum1,int(c)-1)
else:
    fibno(f1,f2,int(c),sum1)
