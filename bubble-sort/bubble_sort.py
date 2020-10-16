def bubble_sort(lst):
    # sort the list via selection sort
	a = int(len(lst))
	bmin = 0
	newlst = []
	print(lst)
	if a == 1:
		return(lst)
	elif a > 1:
		for i in range (a):
			bmin = i
			for j in range(i+1, len(lst)):
				if lst[bmin] > lst[j]:
					bmin = j
					# change postion of minimum variable in list
			lst[i], lst[bmin] = lst[bmin], lst[i]
		return(lst)

# listt = [5,2,3,1,3,9,7,2,6]
# print(selection_sort(listt))