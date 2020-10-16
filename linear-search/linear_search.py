def linear_search(lst, to_find):
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
	a = int(len(lst))
	if to_find in lst:
		for i in range (a):
			if to_find == lst[i]:
				b = lst[i]
				break
		return(b)
	return(-1)
# alph = [1,2,3,24,5,6]
# ind = 55
# print(linear_search(alph,ind))
# words = ["keyboard","клавиатура","mouse","мышка","computer","компьютер","printer","принтер","monitor","монитор"]
# print(linear_search(words,"computer"))