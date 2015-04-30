def get_multiples(start, end, multiple):
	extra = start % multiple
	if extra == 0:
		num = start
	else:
		num = start - extra + multiple
	ret = []
	while num <= end:
		ret.append(num)
		num += multiple
	return ret