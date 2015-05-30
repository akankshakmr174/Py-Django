def gcd(a,b):
    if b!=0:
        return gcd(b,a%b)
    else:
        return a
        
def lcm(a,b):
    g=gcd(a,b)
    l=a*b/g
    return l

lst=[]
for i in range(1,21):
    lst.append(i)
    
l=lcm(lst[0],lst[1])
for i in range(0,20):
    l=lcm(l,lst[i])
    
print "The smallest positive number that is evenly divisible by \
all of the numbers from 1 to 20 is",l
