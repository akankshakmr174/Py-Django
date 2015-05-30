def bsort1(name):
    lst=list(name)
    t=''
    count1=0
    for i in range(len(name)):
        for j in range(0,len(name)-i-1):
            if lst[j]>lst[j+1]:
                t=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=t
                count1+=1
                
    return count1
    
def bsort2(name):
    lst=list(name)
    t=''
    count2=0
    for i in range(len(name)):
        for j in range(0,len(name)-i-1):
            if lst[j]<lst[j+1]:
                t=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=t
                count2+=1
                
    return count2
    
word=raw_input("Enter sequence of initials: ")    
c1=bsort1(word)
c2=bsort2(word)

print "Minimum no. of changes required is",
if c1<c2:
    print c1
else:
    print c2
