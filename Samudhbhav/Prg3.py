# Program to find smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20
def gcd(a,b): return b and gcd(b, a % b) or a # GCD function
def lcm(a,b): return a * b / gcd(a,b)         # LCM function
n = 1
for i in xrange(1, 21):
    n = lcm(n, i)
print n 
