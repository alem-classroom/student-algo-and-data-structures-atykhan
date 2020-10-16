def steps(num):
    # solve the problem via dynamic programming
    # return number of required steps
    fprev = 0
    fprev2 = 1
    if num == 0:
    	return(0)
    elif num == 1:
    	return(1)
    else:
    	for i in range (num):
    		fsled = fprev2 + fprev
    		fprev = fprev2
    		fprev2 = fsled
    	return(fprev)

# print(steps(11))


