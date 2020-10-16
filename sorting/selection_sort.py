def selection_sort(lst):
    # sort the list via selection sort
	a = int(len(lst))
	bmin = 0
	newlst = []
	print(lst)
	if a == 1:
		return(lst)
	elif a > 1:
		for i in range (a):
			bmin = min(lst)
			cmax = max(lst)
			newlst.append(bmin)
			minpos = lst.index(min(lst))
			lst[minpos] = cmax
		return(newlst)