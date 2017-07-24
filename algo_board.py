
			
#board function
def rows(brd,player):
	for x in range(board_size-1):
		result = 1
		for y in range(board_size-1):
			if brd[x][y]!=player:
				result = 0
				break
		if result==1:
			break
	return result

def cols(brd,player):
	for x in range(board_size-1):
		result = 1
		for y in range(board_size-1):
			if brd[y][x]!=player:
				result = 0
				break
		if result==1:
			break
	return result
def axis(brd,player):
	result_a=0
	result_b=0
	for x in range(board_size-1):
		if brd[x][x]==player:
			result_a+=1
		if brd[x][board_size-1-x]==player:
			result_b+=1	

	if result_a==board_size or result_b==board_size:
		return 1
	return 0	



def XmixDrix(brd):
	result=rows(brd,"x") or rows(brd,"o") or cols(brd,"x") or cols(brd,"o") or axis(brd,"x") or axis(brd,"o")	 		
	if result==1:
		return "we have a winner!"
	else:
		"its a tie game"		