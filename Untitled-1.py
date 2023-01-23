def Maximal_Rectangle(M): 
	max_area = 0
	N = len(M)
	if N == 0: 
		return 0

	dp = [[0 for x in range(len(M[0]))] for y in range(N)] 
	
	for i in range(N): 
		for j in range(len(M[0])): 
			
			# update the entry in tp when 
			# only cell is 1 
			if (M[i][j] == 1): 
				dp[i][j] = dp[i][j - 1] + 1
				
			max_area = max(max_area, dp[i][j]) 
	
	return max_area * max_area 


# Driver Code 
M = [[1, 0, 1, 0, 0], 
	[1, 0, 1, 1, 1], 
	[1, 1, 1, 1, 1], 
	[1, 0, 0, 1, 0]] 

print('Area of Maximum Rectangle is', Maximal_Rectangle(M)) 

# Output:
# Area of Maximum Rectangle is 6