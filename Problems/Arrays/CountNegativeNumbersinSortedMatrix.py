'''
Problem Statement:

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.

Return the number of negative numbers in grid.

Example 1:


Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

Output: 8

Explanation: There are 8 negatives number in the matrix.



Example 2:





Input: grid = [[3,2],[1,0]]

Output: 0



Example 3:





Input: grid = [[1,-1],[-1,-1]]

Output: 3



Example 4:





Input: grid = [[-1]]

Output: 1

Constraints:



m == grid.length

n == grid[i].length

1 <= m, n <= 100

-100 <= grid[i][j] <= 100

'''




class Solution(object):
	def countNegatives(self,grid):
		rows=len(grid)
		cols=len(grid[0])
		i,j=rows-1,0
		count=0
		print(rows,cols,i,j)
		while i>=0 and j<cols:
			if grid[i][j]<0:
				count+=(cols-j)
			else:
				j+=1
		return count




s=Solution()
a=[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3],]
print(*a,sep="\n")
print(s.countNegatives(a))





