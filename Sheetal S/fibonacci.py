print "\n\n---Program to display Fibonacci series until N natural numbers\n\n"
n=int(raw_input("Enter the value of N: "))
print "There are 2 ways to solve the program. It is by recursion or iteration. "
x=0
while (x!=1) and (x!=2):
 x=int(raw_input("Enter 1 for recursion and 2 for iteration: "))
if x==1: #Recursion Case
 a=0
 b=1
 print b,
 m=1
 def rec(a,b,m):
  if m>=n:
   return
  c=a+b
  print c,
  a=b
  b=c
  m=m+1
  rec(a,b,m)
 rec(a,b,m)
  
else: #Iteration case
 a=0
 b=1
 print b,
 for m in range(2,n+1):
   c=a+b
   print c,
   a=b
   b=c
   
   
   
   
   
  
  

 

