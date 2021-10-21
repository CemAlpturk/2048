import numpy as np


class Game:
    def __init__(self, grid_size=4):
        self.grid_size = grid_size
        self.grid = np.zeros((self.grid_size, self.grid_size), dtype=int)
        self.grid_prev = np.zeros((self.grid_size, self.grid_size), dtype=int)
        self.round = 0
        self.score = 0
        self.end = False
        self._init_grid()

    def _init_grid(self):
        i, j = np.random.randint(self.grid_size, size=2)
        self.grid[i][j] = 2

    def add_random_tile(self):
        empty = np.argwhere(self.grid == 0)
        num_cells = empty.shape[0]
        if num_cells != 0 and (self.grid != self.grid_prev).any():
            cell = empty[np.random.randint(num_cells)]
            self.grid[cell[0]][cell[1]] = 2
        elif self.check_moves():
            self.end = True

    def _move_left(self):
        for i in range(self.grid_size):
            # Move
            for j in range(1, self.grid_size):
                if self.grid[i][j] != 0:
                    k = 1
                    while j-k >= 0 and self.grid[i][j-k] == 0:
                        k += 1
                    if k > 1:
                        self.grid[i][j-k+1] = self.grid[i][j]
                        self.grid[i][j] = 0
            # Merge
            for j in range(1, self.grid_size):
                if self.grid[i][j] != 0 and self.grid[i][j] == self.grid[i][j-1]:
                    self.grid[i][j-1] *= 2
                    self.grid[i][j] = 0
                    self.score += self.grid[i][j-1]

            # Move
            for j in range(1, self.grid_size):
                if self.grid[i][j] != 0:
                    k = 1
                    while j-k >= 0 and self.grid[i][j-k] == 0:
                        k += 1
                    if k > 1:
                        self.grid[i][j-k+1] = self.grid[i][j]
                        self.grid[i][j] = 0
        # self.add_random_tile()

    def _move_right(self):
        for i in range(self.grid_size):
            # Move
            for j in range(self.grid_size-2, -1, -1):
                if self.grid[i][j] != 0:
                    k = 1
                    while j+k < self.grid_size and self.grid[i][j+k] == 0:
                        k += 1
                    if k > 1:
                        self.grid[i][j+k-1] = self.grid[i][j]
                        self.grid[i][j] = 0
            # Merge
            for j in range(self.grid_size-2, -1, -1):
                if self.grid[i][j] != 0 and self.grid[i][j] == self.grid[i][j+1]:
                    self.grid[i][j+1] *= 2
                    self.grid[i][j] = 0
                    self.score += self.grid[i][j+1]

            # Move
            for j in range(self.grid_size-2, -1, -1):
                if self.grid[i][j] != 0:
                    k = 1
                    while j+k < self.grid_size and self.grid[i][j+k] == 0:
                        k += 1
                    if k > 1:
                        self.grid[i][j+k-1] = self.grid[i][j]
                        self.grid[i][j] = 0
        # self.add_random_tile()


    def _move_up(self):
        for j in range(self.grid_size):
            # Move
            for i in range(1, self.grid_size):
                if self.grid[i][j] != 0:
                    k = 1
                    while i-k >= 0 and self.grid[i-k][j] == 0:
                        k += 1
                    if k > 1:
                        self.grid[i-k+1][j] = self.grid[i][j]
                        self.grid[i][j] = 0
            # Merge
            for i in range(1, self.grid_size):
                if self.grid[i][j] != 0 and self.grid[i][j] == self.grid[i-1][j]:
                    self.grid[i-1][j] *= 2
                    self.grid[i][j] = 0
                    self.score += self.grid[i-1][j]

            # Move
            for i in range(1, self.grid_size):
                if self.grid[i][j] != 0:
                    k = 1
                    while i-k >= 0 and self.grid[i-k][j] == 0:
                        k += 1
                    if k > 1:
                        self.grid[i-k+1][j] = self.grid[i][j]
                        self.grid[i][j] = 0
        # self.add_random_tile()


    def _move_down(self):
        for j in range(self.grid_size):
            # Move
            for i in range(self.grid_size-2, -1, -1):
                if self.grid[i][j] != 0:
                    k = 1
                    while i+k < self.grid_size and self.grid[i+k][j] == 0:
                        k += 1
                    if k > 1:
                        self.grid[i+k-1][j] = self.grid[i][j]
                        self.grid[i][j] = 0
            # Merge
            for i in range(self.grid_size-2, -1, -1):
                if self.grid[i][j] != 0 and self.grid[i][j] == self.grid[i+1][j]:
                    self.grid[i+1][j] *= 2
                    self.grid[i][j] = 0
                    self.score += self.grid[i+1][j]

            # Move
            for i in range(self.grid_size-2, -1, -1):
                if self.grid[i][j] != 0:
                    k = 1
                    while j+k < self.grid_size and self.grid[i+k][j] == 0:
                        k += 1
                    if k > 1:
                        self.grid[i+k-1][j] = self.grid[i][j]
                        self.grid[i][j] = 0
        # self.add_random_tile()

    def step(self, d):
        if not self.end:
            if d == 0:
                self._move_left()
            elif d == 1:
                self._move_right()
            elif d == 2:
                self._move_up()
            else:
                self._move_down()
            self.add_random_tile()
            self.grid_prev = self.grid.copy()
        else:
            print("Game has ended")

    def check_moves(self):
        padded = np.zeros((self.grid_size+2, self.grid_size+2), dtype=int)
        padded[1:self.grid_size+1, 1:self.grid_size+1] = self.grid  # Copy?
        for i in range(1, self.grid_size+1):
            for j in range(1, self.grid_size+1):
                up = padded[i][j] == padded[i][j-1]
                down = padded[i][j] == padded[i][j+1]
                left = padded[i][j] == padded[i-1][j]
                right = padded[i][j] == padded[i+1][j]

                if up or down or left or right:
                    return False
        return True




if __name__ == '__main__':
    g = Game()
    print(g.grid)
    while not g.end:
        g.step(np.random.randint(4))
        print(g.grid)
        print(g.score)
