n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
def count(n):
    a=1
    num=2
    f=0
    while a==1:
        while f<len(n):
            if num%n[f]==0:
                f+=1
            else:
                break
        num+=1
        if (f)==len(n):
            a=0
        f=0
    return num
print "the least number is: ",count(n)-1
                
