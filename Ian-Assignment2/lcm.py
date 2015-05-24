lst=[]
def gcd(a,b):   #function to find gcd
    while b>0:
        t=a%b
        a=b
        b=t
    return a

def lcm(a,b):   #function to find lcm
    lcm=a*b/gcd(a,b)
    return(lcm)

for i in range(1,21):
    lst.append(i)

lcm_num=1
for num in lst:
    lcm_num=lcm(num,lcm_num)

print lcm_num



