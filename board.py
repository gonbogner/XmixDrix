import algo_board
# board definition
board_size=int(raw_input("Enter board size:"))

board = [[1 for x in range(board_size)] for y in range(board_size)] 
for row in range(board_size):
	for col in range(board_size):
		board[x][y]=0
for row in range(board_size):
	for col in range(board_size):
		x=raw_input int(("choose row for your move:"))
		y=raw_input int(("choose colom for your move:"))
		move=raw_input('Enter a move:')
		fill_yourself(board,x,y,move)
		
print algo_board.XmixDrix(board)		

def fill_yourself(brd,x,y,move):
	flag=1
	while flag==1:
		if brd[x][y]!=0:
			print "sorry, this place is already taken"
			print "please enter another location for your move:"
			x=raw_input int(("choose row for your move:"))
			y=raw_input int(("choose colom for your move:"))
		else:
			brd[x][y]=move
			flag=0
			return	

	
