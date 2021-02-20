l=int(input())			#enter lower bound range
u=int(input())			#enter the upper bound range
if (l>=0 and l<u):
	for i in range(l,u+1):
		temp=i
		sum=0
		length=len(str(i))
		while temp >0:
			dig=temp%10			
			sum+=dig**length
			temp=temp//10
		if i ==sum:
			print(sum)
else:
	print('Wrong Input')