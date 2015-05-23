# Program to find minimum number of inversions (swapping two neighbouring letters) in the input required 
# such that a single kind of letter is adjacent to each other. 

# Inversion definition: A pair of elements (ai,aj) where i and j are the indices is called 
# an inversion in a permutation a if i<j and ai>aj.

# There are two cases since after inversions the final string can have a set of either of the two characters 
# at the start and the other set succeeding.
# For ex: AAAAKK or KKAAAA 
# Find the minimum of these cases 

s = raw_input("Enter a word with any number of repetitions of any two letters in a random order")              
a = s[0]
s1 = [] 
i = 0
l = len(s)
t1 = 0
t2 = 0
# First case
for i in xrange(0,l):
    if(s[i] == a):
        s1.append(1)
    else: s1.append(2)  # Converting to integer array for comparison
    i += 1
for i in xrange(0,l):
    for j in xrange(0,l):
        if s1[i]>s1[j] and i<j:  # From inversion definition
            t1 += 1
# Repeat again for second case since assigning 1 and 2 to the two characters which are input can also be done other way round.
for i in xrange(0,l):
    if(s[i] == a):
        s1.append(2)
    else: s1.append(1) # Converting to integer array for comparison
for i in xrange(0,l):
    for j in xrange(0,l):
        if s1[i]>s1[j] and i<j:  # From inversion definition
            t2 += 1
    
print "Minimum number of inversions is:"
if(t1<t2): print t1  # Since we require minimum inversions
else: print t2
