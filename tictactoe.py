import numpy as np
import time
from tkinter import *
import tkinter.font as tkFont
from enum import Enum

class STATUS(Enum):
	IN_PROGRESS = 1
	DRAW = 2
	WINNER = 3


class Game():
	def __init__(self):
		self.root = Tk()
		self._button_list = []

		buttonFont = tkFont.Font ( family="Helvetica",size=36 )
		infoFont = tkFont.Font ( family="Helvetica",size=20 )
		restart = Button(self.root, text="New Game", font=infoFont, command=self._newGame)
		restart.grid(columnspan = 3)
		for x in range(3):
			for y in range(3):
				b = Button(self.root, height=1, width=3, text="", font=buttonFont, command=lambda x=x, y=y: self._handleClick(x, y))
				self._button_list.append(b)
				b.grid(row = y + 1, column = x, padx=(2, 2), pady=(2, 2))
		self.info = Label(self.root, height=2, width=18, text="The next player is X", font=infoFont)
		self.info.grid(columnspan = 3)

		self._newGame()
		mainloop()

	def _handleClick(self, x, y):
		if not self.status:
			return

		# Check for valid click
		if self._board[x][y] != 0:
			return

		# Apply click
		self._udpdateBoard(x, y)

		# Check for game status
		if self._checkStatus() != STATUS.IN_PROGRESS:
			self.status = False
			return

		# Change to the other player
		self._current_player = 3 - self._current_player
		self.info.config(text = "The next player is: {}".format(self._getPlayerIcon(self._current_player)))

	def _udpdateBoard(self, x, y):
		self._board[x][y] = self._current_player
		self._button_list[3 * x + y].config(text=self._getPlayerIcon(self._current_player))
		self._movecounter += 1

	def _checkStatus(self):
		# check for rows
		for x in range(3):
			if self._board[x][0] == self._board[x][1] == self._board[x][2] != 0:
				self.info.config(text = "The Winner is: {}!".format(self._getPlayerIcon(self._current_player)))
				self._button_list[3 * x + 0].config(background="yellow")
				self._button_list[3 * x + 1].config(background="yellow")
				self._button_list[3 * x + 2].config(background="yellow")
				return STATUS.WINNER

		# check for columns
		for y in range(3):
			if self._board[0][y] == self._board[1][y] == self._board[2][y] != 0:
				self.info.config(text = "The Winner is: {}!".format(self._getPlayerIcon(self._current_player)))
				self._button_list[0 + y].config(background="yellow")
				self._button_list[3 + y].config(background="yellow")
				self._button_list[6 + y].config(background="yellow")
				return STATUS.WINNER

		# check for diagonals
		if self._board[0][0] == self._board[1][1] == self._board[2][2] != 0:
			self.info.config(text = "The Winner is: {}!".format(self._getPlayerIcon(self._current_player)))
			self._button_list[0].config(background="yellow")
			self._button_list[4].config(background="yellow")
			self._button_list[8].config(background="yellow")
			return STATUS.WINNER
		if self._board[0][2] == self._board[1][1] == self._board[2][0] != 0:
			self.info.config(text = "The Winner is: {}!".format(self._getPlayerIcon(self._current_player)))
			self._button_list[2].config(background="yellow")
			self._button_list[4].config(background="yellow")
			self._button_list[6].config(background="yellow")
			return STATUS.WINNER

		# check if gameboard full
		if self._movecounter == 9:
			self.info.config(text = "The game is draw!")
			return STATUS.DRAW
		return STATUS.IN_PROGRESS

	def _getPlayerIcon(self, id):
		if id == 1:
			return "X"
		return "O"

	def _newGame(self):
		self._current_player = 1
		self._movecounter = 0
		self._board = np.zeros((3, 3))
		self.status = True
		for button in self._button_list:
			button.config(text = "", background='#F0F0F0')
		self.info.config(text = "The next player is X")





game = Game()