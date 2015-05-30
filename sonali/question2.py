def count(n):
    f=0
    sum2=0
    while f<len(n):
        if n[f]==" " or n[f]=="-":
            f+=1
        else:
            sum2+=1
            f+=1
    return sum2
a=True
sum1=0
while(a):
    c=raw_input("enter ur number in words: ")
    sum1+=count(c)
    k=raw_input("enter do u want to continue(1/0): ")
    if int(k)==0:
        break
print "sum is: ",sum1
