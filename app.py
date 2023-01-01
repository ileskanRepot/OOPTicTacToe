class Game():
	def __init__(self, startBoard, startTurn, countedWin = []):
		if len(startBoard) != 9:
			self.board = startBoard + (9 - len(startBoard))*[0]
		else:
			self.board = startBoard
		self.turn = startTurn
		self.wins = countedWin

	def place(self, spot):
		self.board[spot] = self.turn
		if self.turn == 1:
			self.turn = 2
		else:
			self.turn = 1

	def isOver(self):
		# Check rows
		if self.board.count(0) == 0:
			return 0
		for i in range(3):
			if self.board[i*3] == self.board[i*3 + 1] and self.board[i*3] == self.board[i*3 + 2] and self.board[i*3] != 0:
				return self.board[i*3]

		# Check columns
		for i in range(3):
			if self.board[i] == self.board[i + 3] and self.board[i] == self.board[i + 6] and self.board[i] != 0:
				return self.board[i]

		if self.board[0] == self.board[4] and self.board[0] == self.board[8] and self.board[0] != 0:
			return self.board[0]
		if self.board[2] == self.board[4] and self.board[2] == self.board[6] and self.board[2] != 0:
			return self.board[2]

		return -1

	def displayBoard(self):
		print("  A B C")
		print(" ┏━┳━┳━┓")
		for ii in range(3):
			print(str(ii+1)+"┃",end='')
			for jj in range(3):
				if self.board[ii * 3 + jj] == 0:
					print(' ',end='')
				elif self.board[ii * 3 + jj] == 1:
					print('X',end='')
				else:
					print('O',end='')
				print("┃",end='')
				# print(self.board[ii * 3 + jj], end=' ')
			print()
		print(" ┗━┻━┻━┛")

	def isCorrectMove(self, mov):
		try:
			if len(mov) != 2:
				return False
			if 0 > int(mov[1]) or 3 < int(mov[1]):
				return False
		except:
				return False
		return True

	def canPlace(self, place):
		return self.board[place] == 0

	def play(self,place):
		if self.canPlace(place):
			self.place(place)
			return True
		else:
			return False

	def playAuto(self,iteration):
		print("iteration",iteration)
		over = self.isOver()
		print(over)
		print(self.board)
		stats = []
		if over != -1:
			return self.wins + [over]
		for ii, jj in enumerate(self.board):
			if jj == 0:
				tmpBoard = self.board
				tmpBoard[ii] = turn
				tmpGame = Game(tmpBoard, (self.turn%2)+1, self.wins)
				stats += tmpGame.playAuto(iteration+1)
		#return self.wins + stats

	def start(self):
		self.displayBoard()
		while self.isOver() == -1:
			move = "D5"
			tur = 'X'
			if self.turn == 2:
				tur = 'O'
			move = input(tur + " Turn. Where to put (A1) ")
			if not self.isCorrectMove(move):
				return False
			place = (int(move[1])-1) * 3
			if move[0].upper() == 'A': place += 0
			elif move[0].upper() == 'B': place += 1
			else: place += 2

			self.play(place)
			self.displayBoard()
		over = self.isOver()
		if over == 1:
			print("X wins")
		elif over == 2:
			print("O wins")
		elif over == 0:
			print("Tie")

if __name__ == "__main__":
	board = []
	turn = 1
	game = Game(board, turn)
	# game.displayBoard()
	# game.start()
	# print(game.board)
	game.playAuto(0)
