# importing "copy" for copy operations 
import copy 
import sys
sys.setrecursionlimit(5000)

def next_character(visited, current_row, current_column):
	word = ""
	visited.append((current_row, current_column))
	for letter in visited:
		word+=board[letter[0]][letter[1]]
	if(word.upper() in dictionary and (word not in word_candidates)):
		print(word)
		word_candidates.append(word)
	if(len(visited) > 9):
		return
	prev_row = current_row - 1
	next_row = current_row + 1
	prev_column = current_column - 1
	next_column = current_column + 1
	# print(word)
	# Adds the charcter S the current pos
	if(len(board[current_row]) > next_row and ((next_row, current_column) not in visited)):
		next_character(copy.deepcopy(visited), next_row, current_column)
	#Adds the character SE the current pos
	if(len(board[current_row]) > next_row and len(board) > next_column) and ((next_row, next_column) not in visited):
		next_character(copy.deepcopy(visited), next_row, next_column)
	# Adds the charcter E of the current pos
	if(len(board) > next_column and ((current_row, next_column) not in visited)):
		next_character(copy.deepcopy(visited), current_row, next_column)
	#Adds the character NE the current pos
	if(len(board) > next_column and prev_row >= 0 and ((prev_row, next_column) not in visited)):
		next_character(copy.deepcopy(visited), prev_row, next_column)
	# Adds the charcter N the current pos
	if(prev_row >= 0 and ((current_row -1, current_column) not in visited)):
		next_character(copy.deepcopy(visited), prev_row, current_column)
	# Adds the charcter NW of the current pos
	if(prev_row >= 0 and prev_column >= 0 and ((prev_row, prev_column) not in visited)):
		next_character(copy.deepcopy(visited), prev_row, prev_column)
	# Adds the charcter W of the current pos
	if(prev_column >= 0 and ((current_row, prev_column) not in visited)):
		next_character(copy.deepcopy(visited), current_row, prev_column)
	# Adds the charcter SW of the current pos
	if(prev_column >= 0 and len(board[current_row]) > next_row and ((next_row, prev_column) not in visited)):
		next_character(copy.deepcopy(visited), next_row, prev_column)
	return
def create_board(input):
	arr = [[input[0], input[1], input[2], input[3]],
	[input[4], input[5], input[6], input[7]],
	[input[8], input[9], input[10], input[11]],
	[input[12], input[13], input[14], input[15]]]
	print(input[0], input[1], input[2], input[3])
	print(input[4], input[5], input[6], input[7])
	print(input[8], input[9], input[10], input[11])
	print(input[12], input[13], input[14], input[15])
	return arr
f = open('wordlist-en.txt', 'r')
dictionary = set(f.read().splitlines())
input = input("the words? (max. 16)")
board = create_board(input)
word_candidates = []
for row in range(0,4):
	for column in range(0,4):
		next_character([], row, column)
# print(len(word_candidates))
# for word in word_candidates:
# 	if(word.upper() in dictionary):
# 		print(word)