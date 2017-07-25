
#board function
def rows(brd,player):
	board_size=len(brd)
	for x in range(board_size):
		result = 1
		for y in range(board_size):
			if brd[x][y]!=player:
				result = 0
				break
		if result==1:
			break
	return result

def cols(brd,player):
	board_size=len(brd)
	for x in range(board_size):
		result = 1
		for y in range(board_size):
			if brd[y][x]!=player:
				result = 0
				break
		if result==1:
			break
	return result
def axis(brd,player):
	result_a=0
	result_b=0
	board_size=len(brd)
	for x in range(board_size):
		if brd[x][x]==player:
			result_a+=1
		if brd[x][board_size-1-x]==player:
			result_b+=1	

	if result_a==board_size or result_b==board_size:
		return 1
	return 0	



def XmixDrix(brd):
	if rows(brd,"x") or  cols(brd,"x") or axis(brd,"x"):
		return 'x' 	 		
	elif rows(brd,"o") or  cols(brd,"o") or axis(brd,"o"):
		return 'o'
	else:
		return "0"		