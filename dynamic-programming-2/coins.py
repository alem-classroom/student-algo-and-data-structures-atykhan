def maxCoins(lst, n):
    # return maximum number of coins that can be acquired in the maze
	# sum = 0
	# sum2 = 0
	# m = 1
	# for i in range (m): change first row
	# 	for j in range (n):
	# 		sum = sum + lst[i][j]
	# 		lst[i][j] = sum
	# 		# print(lst[i][j])
	# 	sum = 0

	# for i in range (n): change first column
	# 	for j in range (m):
	# 		sum2 = sum2 + lst[i][j]
	# 		lst[i][j] = sum2
	# 		# print(lst[i][j])
	# 	sum = 0
	# print(lst)

	p = 0
	q = 0
	k = lst[0][n-1]
	# print(k)
	for p in range (n):
		for q in range (n):
			if lst[p-1][q] > lst[p][q-1]:
				lst[p][q] = lst[p][q] + lst[p-1][q]
			elif lst[p-1][q] > lst[p][q-1]:
				lst[p][q] = lst[p][q] + lst[p][q-1]
			else:
				lst[p][q] = lst[p][q] + lst[p][q-1]
			# print(lst[p][q])
	return(lst[n-1][n-1]-k)

		# return(lst)
# lst = [[3, 1, 4, 9, 9], [2, 4, 9, 6, 8], [7, 4, 9, 1, 7], [1, 2, 1, 2, 2], [2, 4, 9, 5, 5]]
# n = 5
# print(maxCoins(lst,n))