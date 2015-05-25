count=0
num=0


def num_check1(num): #for rest of numbers
    tens=num/10
    digit=num%10
    global count
    if digit==1 or digit==2 or digit==6:
        count+=3
    elif digit==3 or digit==7 or digit==8:
        count+=5
    else:
        count+=4
    if tens==2 or tens==3 or tens==8 or tens==9:
        count+=6
    elif tens==4 or tens==5 or tens==6:
        count+=5
    elif tens==7:
        count+=7
    else:
        count+=0

def num_check2(num): #for numbers from 10 to 19
    digit=num%10
    global count
    if digit==1 or digit==2:
        count+=6
    elif digit==3 or digit==4 or digit==8 or digit==9:
        count+=8
    elif digit==5 or digit==6:
        count+=7
    elif digit==7:
        count+=9
    elif digit==0:
        count+=3


for num in range(1,10):
    num_check1(num)
for num in range(10,20):
    num_check2(num)
for num in range(20,100):
    num_check1(num)

count+=len("one")+len("hundred")    #since length of one hundred is omitted
print "Number of letters used " +str(count)

