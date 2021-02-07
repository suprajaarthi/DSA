def sum_list(l):
	if len(l)==0:
		return 0 


	last_num=l.pop()
	return sum_list(num+sum_list)