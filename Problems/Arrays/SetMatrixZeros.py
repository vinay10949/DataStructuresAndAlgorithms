'''
Problem Statement:

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
Example 1:





Input: 

[

  [1,1,1],

  [1,0,1],

  [1,1,1]

]

Output: 

[

  [1,0,1],

  [0,0,0],

  [1,0,1]

]



Example 2:





Input: 

[

  [0,1,2,0],

  [3,4,5,2],

  [1,3,1,5]

]

Output: 

[

  [0,0,0,0],

  [0,4,5,0],

  [0,3,1,0]

]


'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_flag, col_flag = False, False
        m = len(matrix)
        n = len(matrix[0])
        
        #Traverse the 
        for i in range(m):
            for j in range(n):
                if i==0 and matrix[i][j] == 0:
                    row_flag = True
                if j == 0 and matrix[i][j] == 0:
                    col_flag = True
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if row_flag == True:
            for i in range(n):
                matrix[0][i] = 0
        
        if col_flag:
            for j in range(m):
                matrix[j][0] = 0
        return matrix
        
        
        
        
        
    
    
    
        
        
        
        
        
        
        
        
        
    
