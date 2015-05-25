def count(num):
    if num==1 or num==2 or num==6 or num==10:
        return 3
    elif num==3 or num==7 or num==8:
        return 5
    elif num==4 or num==5 or num==9:
        return 4
    elif num==0:
        return 0
        
def tens_place(num):
    if num==2 or num==3 or num==8 or num==9:
        return 6
    elif num==4 or num==5 or num==6:
        return 5
    elif num==7:
        return 7

def elev_twenty(num):
    if num==11 or num==12 :
        return 6
    elif num==13 or num==14 or num==18 or num==19:
        return 8
    elif num==15 or num==16:
        return 7
    elif num==17:
        return 9

sum=0
for i in range(1,11):
    sum=sum+count(i)

for i in range(11,20):
    sum=sum+elev_twenty(i)
for i in range(20,100):
    n=i
    dig=n%10
    if dig!=0:
        sum=sum+count(dig)
    n=n/10
    if n!=0:
        dig2=n%10
        sum=sum+tens_place(dig2)
sum=sum+10 #one hundred
           
print "No. of letters in number names from 1-100 is",sum
