def linear_search(lst, to_find):
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
	a = int(len(lst))
	for i in range (a):
		b = -1
		if to_find == lst[i]:
			b = i
			return(b)
			break
# alph = [1,2,3,24,5,6]
# ind = 5
# print(linear_search(alph,ind))