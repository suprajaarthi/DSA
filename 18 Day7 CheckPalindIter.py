def checkPal(string):
	l=len(string)
	i=0;j=l-1
	while  i<j:
		if(string[i]!=string[j]):
			return False 
		i=i+1
		j=j-1
	return True