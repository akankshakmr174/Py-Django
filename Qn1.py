def fibo_recursive(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo_recursive(n-1)+fibo_recursive(n-2)
        
def fibo_iteration(n):
    a=-1
    b=1
    count=1

    while count<=n:
        c=a+b
        print c,
        a=b
        b=c
        count+=1

choice=raw_input("Enter 'r' for  recursion or 'i' for iteration: " )
while(choice!='r' and choice!='i'):
    print "Incorrect choice.Enter again."
    choice=raw_input("Enter 'r' for  recursion or 'i' for iteration: " )

n=int(raw_input("Enter n: "))
while(n<1):
    print "Incorrect choice. Enter again."
    n=int(raw_input("Enter n: "))

if choice=='r':
    for i in range(n):
        print fibo_recursive(i),

elif choice=='i':
    fibo_iteration(n)
