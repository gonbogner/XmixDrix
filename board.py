def fill_yourself(brd,x,y,move):
	flag=1
	while flag==1:
		if brd[x][y]!=0:
			print "sorry, this place is already taken"
			print "please enter another location for your move:"
			x=int(raw_input ("choose row for your move:"))
			y=int(raw_input ("choose colom for your move:"))
		else:
			brd[x][y]=move
			flag=0	





import algo_board
# board initialization
board_size=int(raw_input("Enter board size:"))
board = [[0 for x in range(board_size)] for y in range(board_size)] 

# main loop
for turns in range(1,board_size**2):
	print "Turn number ", turns
	x=int(raw_input ("choose row for your move:"))
	y=int(raw_input ("choose colom for your move:"))
	move=raw_input('Enter a move:')
	fill_yourself(board,x,y,move)	
	res=algo_board.XmixDrix(board)
	if (res=="x"):
		print "X is the winner"
		break
	elif (res=="o"):
		print "O is the winner"
		break

if algo_board.XmixDrix(board)==0:
	print "No one won"
		

