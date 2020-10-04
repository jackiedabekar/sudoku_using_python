import numpy as np


#Define Empy Matrix
grid = []

"""
for i in range(1,10):
    a = []
    for j in range(1,10):
        a.append(int(input(f'Enter {j} element of {i} row element: ')))
    grid.append(a)

for i in range(9):
    for j in range(9):
        grid[i][j]
"""

for i in range(1,10):
	a = input(f"Enter The Element of {i} Row in Single line: \n")
	b = list(map(int,a))
	grid.append(b)


#For printing purpose
mat = np.matrix(grid)

print("<-----Original Unsolved Sudoku----->\n")
print(mat)
print("<---------------------------------->\n")



#A Function To Check Particular Numbeer Exits in 
#in the given location.
#Here y represent row and x represent col  and n represents number
#of the sudoku
def possible(y,x,n):
	"""
	This function is use to calculate if 
	a particular number 'N' can be put at location
	(y,x)
	were y = rows of sudoku
		 x = col of sudoku 
	"""
	global grid
	for i in range(0,9): 
		if grid[y][i] == n:
			return False
	for i in range(0,9):
		if grid[i][x] == n:
			return False
	x0 = (x//3)*3
	y0 = (y//3)*3
	for i in range(0,3):
		for j in range(0,3):
			if grid[y0+i][x0+j] == n:
				return False
	return True


#In this program 0 menas empt cell in sudoku puzzel
#the solve function check if some number can be
#place in y,x location with the help of possible function
def solve():
	"""
	This function check for the empty place in puzzle.
	And try number between 1-9 at that emply location
	with the help of possible function

	   [[5,3,0,0,7,0,0,0,0],
       [6,0,0,1,9,5,0,0,0],
       [0,9,8,0,0,0,0,6,0],
       [8,0,0,0,6,0,0,0,3],
       [4,0,0,8,0,3,0,0,1],
       [7,0,0,0,2,0,0,0,6],
       [0,6,0,0,0,0,2,8,0],
       [0,0,0,4,1,9,0,0,5],
       [0,0,0,0,8,0,0,0,0]]
	"""
	global grid
	for y in range(9):
		for x in range(9):
			if grid[y][x] == 0:
				for n in range(1,10):
					if possible(y,x,n):
						grid[y][x] = n
						solve()
						grid[y][x] = 0
				return
	print(np.matrix(grid))

print("<----- Solved Sudoku ----->")
solve()