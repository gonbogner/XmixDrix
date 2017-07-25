def fill_yourself(brd,x,y):
	flag=1
	while flag==1:
		if brd[x][y]!=0:
			print "sorry, this place is already taken"
			print "please enter another location for your move:"
			x=int(raw_input ("choose row for your move:"))
			y=int(raw_input ("choose colom for your move:"))
		else:
			brd[x][y]="x"
			flag=0	

def computer(brd):
	move=0
	while move==0:
		row=random.randint(0,board_size-1)
		colom=random.randint(0,board_size-1)
		if brd[row][colom]==0:
			brd[row][colom]="o"
			move=1

		



def print_xo(brd):
	for prow in range(board_size):
		s=""
		for pcol in range(board_size):
			s=s+"|"+str(brd[prow][pcol])+"|"
		
		print s
		print "-----------"	



def number(brd):
	mone_x=0
	mone_o=0
	mone=0
	for x in range(board_size):
		for y in range(board_size):
			if brd[x][y]=="x":
				mone_x+=1
			elif brd[x][y]=="o":
				mone_o+=1
			else:
				mone+=1

	print "the number of X is :%d" % mone_x
	print "the number of o is :%d" % mone_o
	print "the number of 0 is :%d" % mone			
			

import algo_board
import random
# board initialization
board_size=int(raw_input("Enter board size:"))
board = [[0 for x in range(board_size)] for y in range(board_size)] 
# main loop
for turns in range(1,board_size**2):
	print "Turn number ", turns
	if turns%2!=0:
		x=int(raw_input ("choose row for your move:"))
		y=int(raw_input ("choose colom for your move:"))
		fill_yourself(board,x,y)
	elif turns%2==0:
		computer(board)	
	print_xo(board)
	number(board)	
	res=algo_board.XmixDrix(board)
	if (res=="x"):
		print "You are the winner"
		break
	elif (res=="o"):
		print "The computer is the winner"
		break

if algo_board.XmixDrix(board)==0:
	print "No one won"
		
