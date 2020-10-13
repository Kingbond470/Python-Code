iteration=0
while iteration < 10:
	count=0
	for letter in "hello world":
		count +=1
		if iteration % 2 == 0 :
			break
	print("iteration "+str(iteration)+" count is: "+str(count))
	iteration +=1