def maxCoins(lst, n):
    # return maximum number of coins that can be acquired in the maze
	sum = 0
	sum2 = 0
	m = 1
	# change first row
	for i in range (m): 
		for j in range (n):
			sum = sum + lst[i][j]
			lst[i][j] = sum
			# print(lst[i][j])
		sum = 0
		# change first column
	for i in range (n): 
		for j in range (m):
			sum2 = sum2 + lst[i][j]
			lst[i][j] = sum2
			# print(lst[i][j])
		sum = 0
	# print(lst)

	p = 1
	q = 1
	# k = lst[0][n-1]
	# print(k)
	for p in range (1, n):
		for q in range (1, n):
			if p == 0 and q == 0:
				lst[0][0] = lst[0][0]
			elif lst[p-1][q] > lst[p][q-1]:
				lst[p][q] = lst[p][q] + lst[p-1][q]
			elif lst[p-1][q] > lst[p][q-1]:
				lst[p][q] = lst[p][q] + lst[p][q-1]
			else:
				lst[p][q] = lst[p][q] + lst[p][q-1]
			# print(lst[p][q])
	# print(lst)
	return(lst[n-1][n-1])

		# return(lst)
lst = [[3, 1, 4, 9, 9], [2, 4, 9, 6, 8], [7, 4, 9, 1, 7], [1, 2, 1, 2, 2], [2, 4, 9, 5, 5]]
n = 5
print(maxCoins(lst,n))