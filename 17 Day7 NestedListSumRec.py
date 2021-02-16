def recursive_list_sum(l):
	total = 0
	for i in l:
		if type(i) == type([]):
			total = total + recursive_list_sum(i)
		else:
			total = total +i

	return total
print( recursive_list_sum([1, 2, [3,4],[5,6]]))
