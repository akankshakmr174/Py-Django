s=str(raw_input("Enter the sequence"))
seq1=[]  #Copying input sequence into a list
for c in s:
    seq1.append(c)

seq2=[]  #Copying input sequence into a list
for c in s:
    seq2.append(c)

asc_count=0
desc_count=0

def bubble_sort_asc(s): #To sort in Ascending order
    global asc_count
    for i in range(0,len(s)-1):
        for j in range(0,len(s)-i-1):
            if s[j]>s[j+1]:
                temp=s[j]
                s[j]=s[j+1]
                s[j+1]=temp
                asc_count+=1
    return s

def bubble_sort_desc(s):    #To sort in descending order
    global desc_count
    for i in range(0,len(s)-1):
        for j in range(0,len(s)-i-1):
            if s[j]<s[j+1]:
                temp=s[j]
                s[j]=s[j+1]
                s[j+1]=temp
                desc_count+=1
    return s

asc1=bubble_sort_asc(seq1)
desc1=bubble_sort_desc(seq2)

#Printing which method has lesser number of swaps
if asc_count<desc_count:
    print "Minimum number of swaps " + str(asc_count)
    for c in asc1:
        print "".join(c),
else:
    print "Minimum number of swaps " + str(desc_count)
    for c in desc1:
        print "".join(c),


