word=raw_input("Enter a word consisting of any combination of any 2 letters: ")
n=len(word)-1
for i in range(0,(n/2)+1):
 if word[i]!=word[n-i]:
  c=word[i]
  d=word[n-i]
  break
count=0
for i in range(0,n+1):
 if word[i]==c:
  for j in range(0,i):
   if word[j]==d:
    count=count+1
print count 
  

