def binary_search(lst, to_find):
    # search for the element to_find inside lst
    # if found, return index of element
    # else return -1
	a = int(len(lst))
	b = int(a/2)
	for i in range (b):
		B = lst[:len(lst)//2]
		C = lst[len(lst)//2:]
		if to_find in B:
			lst = B
		elif to_find in C:
			lst = C
	return(lst[0])

# listt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# asd = 9
# print(binary_search(listt,asd))