def gcd(a,b):
 while(a!=b):
  if(a>b):
   a=a-b
  else:
   b=b-a
 return a

lcm=2
for i in range (3,21): 
 a=lcm
 b=i
 gcd1=gcd(a,b)
 lcm=(a*b)/gcd1
print "Smallest positive number divisible by numbers from 1 to 20 is: %d"%lcm
 

 