# board definition
board_size=raw_input("Enter board size:")

board = [[1 for x in range(board_size)] for y in range(board_size)] 
for row in range(board_size):
	for col in range(board_size):
		board[row][col]=raw_input('Enter a move:')