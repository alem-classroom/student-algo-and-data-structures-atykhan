def maxCoins(lst, n):
    # return maximum number of coins that can be acquired in the maze
	maxCoin = ((lst[0]+lst[1])-2)*n
	return(maxCoin)
# lit = [8,8]
# n = 1
# print(maxCoins(lit,n))