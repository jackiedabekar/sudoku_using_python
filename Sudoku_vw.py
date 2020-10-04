#Function To Print Grid
def printgrid():
	global grid
	for row in grid:
		print(row)

#Formimg the puzzel grid
def form_grid(puzzel_string):
	global grid
	print('The Sudoku Problem')
	for i in range(0, len(puzzel_string), 9):
		row = puzzel_string[i:i+9]
		temp = []
		for num in row:
			temp.append(int(num))
		grid.append(temp)
	printgrid()

#function to check if a digit can be placed in thegiver block
def possible(row, col, digit):
	global grid
	for i in range(0,9):
		if grid[row][i] == digit:
			return False
	for i in range(0,9):
		if grid[i][col] == digit:
			return False
	square_row = (row//3)*3
	square_col = (col//3)*3
	for i in range(0,3):
		for j in range(0,3):
			if grid[square_row + i][square_col + j] == digit:
				return False
	return True

def solve():
	global grid
	for row in range(9):
		for col in range(9):
			if grid[row][col] == 0:
				for digit in range(1,10):
					if possible(row,col,digit):
						grid[row][col] = digit
						solve()
						grid[row][col] = 0 #Backtrc step
				return
	print('\nThe Solution Is \n')
	printgrid()


puzzel_string = "004300209005009001070060043006002087190007400050083000600000105003508690042910300"
grid = []
form_grid(puzzel_string)
solve()
