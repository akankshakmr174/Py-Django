

def fibo(num):
	if num==0:
		return 0

	if num==1:
		#print "0\n1"
		return 1
	else:
		#sum=fibo(num-1)+fibo(num-2)
		
		return fibo(num-1)+fibo(num-2)
ch=int(raw_input("1.Iteration\n2.Recursion\nSelect option:"))
if ch==2:
	x=int(raw_input("Enter no. of terms:"))

	for i in range(x):
		print fibo(i) 
else:
	x=int(raw_input("enter no. of terms:"))
	one=0
	two=1
	print "0\n1"
	for i in range(x-2):
		three=one+two
		print three
		one=two
		two=three
