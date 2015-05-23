num=1
for i in range(2,21):
	if num%i!=0:
		for j in range(2,i+1):
			if (num*j)%i==0:
				num*=j
print num
