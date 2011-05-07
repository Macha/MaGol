#!/usr/bin/python2

from __future__ import division

import pygame
import sys

from board import Board

class PyGameGol:

    num_boxes = 100
    screen_size = 800
    
    def __init__(self):
        pygame.init()

        if len(sys.argv) >= 2:
            self.num_boxes = int(sys.argv[1])
        
        self.board = Board(self.num_boxes)
        self.box_size = self.screen_size // self.num_boxes

        if len(sys.argv) == 3:
            filename = sys.argv[2]
            with open(filename) as rlefile:
                self.board.load_rle_into_grid(rlefile)

        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        self.draw_grid()


        self.mainloop()

    def mainloop(self):
        clock = pygame.time.Clock()

        self.paused = True
        self.slow = False
        ticks = 0 
        while True:
            ticks += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.paused = not self.paused
                    if event.key == pygame.K_TAB:
                        self.board.randomise_grid()
                        self.draw_grid()
                    if event.key == pygame.K_r:
                        self.board.blank_grid()
                        self.draw_grid()
                    if event.key == pygame.K_s:
                        self.slow = not self.slow
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        x, y = pygame.mouse.get_pos()
                        self.handle_mouse_click(x, y)
            if not self.paused:
                if (ticks >= 50) or not self.slow:
                    self.board.run_turn()
                    self.draw_grid()
                    ticks = 0
            if self.slow:
                clock.tick(50)

    def handle_mouse_click(self, x, y):
        grid_x = x // self.box_size
        grid_y = y // self.box_size
        self.board.toggle_cell(grid_y, grid_x)
        self.draw_grid()

    def draw_grid(self):
        self.screen.fill((0, 0, 0))
        for row in range(0, self.board.size):
            for col in range(0, self.board.size):
                if self.board.grid[row][col]:
                    rect = pygame.Rect(col * self.box_size, row * self.box_size,
                            self.box_size, self.box_size)
                    self.screen.fill((255, 255, 255), rect)
        pygame.display.flip()

PyGameGol()
