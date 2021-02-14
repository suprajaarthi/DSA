def remove(string):
	stack=[]
	i=0;
	while  i<len(string):
		if len(stack)==0 or stack[-1]!=string[i]:
			stack.append(string[i])
			i+=1
		else:
			stack.pop()
			i+=1
	return stack
print(remove("apple"))