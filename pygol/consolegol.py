#!/usr/bin/python2

from __future__ import print_function

from board import Board
import sys


class GameOfLifeConsole:

    def __init__(self):
        print('Welcome to PyGol')
        print('What board size do you want?')

        board_size = raw_input()

        while not board_size.isdigit():
            print('Please enter a number for the board size:')
            board_size = raw_input()

        self.board = Board(int(board_size))
        self.board.randomise_grid()
        self.mainloop()

    def mainloop(self):
        while True:
            print('How many turns do you want to run (0 to stop)?')
            num_turns = raw_input()

            while not num_turns.isdigit():
                print('Please enter a number for the amount of turns:')
                num_turns = raw_input()
            
            num_turns = int(num_turns)

            if num_turns <= 0:
                print('Goodbye')
                sys.exit()
            
            self.board.run_turns(num_turns)

            for row in self.board.grid:
                for col in row:
                    if col:
                        print('0', end='')
                    else:
                        print('1', end='')
                print()

GameOfLifeConsole()
