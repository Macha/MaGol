import random

import rlereader

class Board:

    def __init__(self, size):
        self.size = size
        self.grid = self.make_blank_grid()
        self.furthest_col = 0
        self.furthest_row = 0

    def run_turns(self, num_turns):
        while num_turns > 0:
            self.run_turn()
            num_turns -= 1

    def run_turn(self):
        new_grid = self.make_blank_grid()
        for row in range(0, self.size):
            for col in range(0, self.size):
                new_grid[row][col] = self.get_cell_life(row, col)

        self.grid = new_grid

    def toggle_cell(self, row, col):
        self.grid[row][col] = not self.grid[row][col]

    def check_furthest(self, row, col):
        if row + 1 >= self.furthest_row:
            self.furthest_row = row + 2
        if col + 1 >= self.furthest_col:
            self.furthest_col = col + 2
          

    def get_cell_life(self, row, col):
        living_neighbours = self.count_active_neighbours(row, col)
        if self.grid[row][col]:
            if living_neighbours in [2, 3]:
                return True
            else:
                self.check_furthest(row, col)
                return False
        else:
            if living_neighbours == 3:
                self.check_furthest(row, col)
                return True
            return False

    def check_cell(self, row, col):
        if row < 0:
            row = self.size - 1
        if row > self.size - 1:
            row = 0

        if col < 0:
            col = self.size - 1
        if col > self.size - 1:
            col = 0

        return self.grid[row][col]

    def count_active_neighbours(self, row, col):
        active_count = 0
        to_check = [
            (row - 1, col - 1), # Top left
            (row - 1, col), # Top
            (row - 1, col + 1), # Top right
            (row, col - 1), # Left
            (row, col + 1), # Right
            (row + 1, col - 1), # Bottom left
            (row + 1, col), # Bottom
            (row + 1, col + 1) # Bottom Right
        ]

        for crow, ccol in to_check:
            if self.check_cell(crow, ccol):
                active_count += 1
        
        return active_count

    def make_blank_grid(self):
        grid = []   
        for row in range(0, self.size):
            grid.append([])
            for col in range(0, self.size):
                grid[row].append([])
                grid[row][col] = False
        return grid

    def load_rle_into_grid(self, rle):
        reader = rlereader.GRLEReader()
        data = reader.read_rle(rle)

        self.blank_grid()
        
        current_token = 0
        
        current_row = 0
        current_col = 0
        while True:
            try:
                token = data[current_token]
            except IndexError:
                break # Out of tokens
            if type(token) == rlereader.EOFToken:
                break
            if token.value in ['b', 'o']:
                self.grid[current_row][current_col] = (token.value == 'o')
                current_col += 1
                if current_col > self.size - 1:
                    print('Too wide an import, cancelling import.')
                    break
                if current_col >= self.furthest_col:
                    self.furthest_col = current_col + 2
            if token.value == '$':
                current_row += 1
                if current_row > self.size - 1:
                    print('Too high an import, cancelling import.')
                current_col = 0
                if current_row > self.furthest_row:
                    self.furthest_row = current_row + 2

            current_token += 1
    
    def randomise_grid(self):
        for row in range(0, self.size):
            for col in range(0, self.size):
                self.grid[row][col] = random.choice([True, False])

        self.furthest_row = self.size - 1
        self.furthest_col = self.size - 1
    
    def blank_grid(self):
        self.grid = self.make_blank_grid()    
