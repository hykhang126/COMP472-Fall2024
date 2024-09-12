class Grid:
    def __init__(self, n):
        self.n = n
        self.grid = self._generate_grid()
    
    def _generate_grid(self):
        """Generates an n x n grid with default room."""
        # then randomzie each cell to have a room with a random state
        grid = [[0 for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                grid[i][j] = Room(i, j, Room.randomize_state())
        return grid
    
    def update_cell(self, row, col, value):
        """Updates a specific cell in the grid with a given value."""
        if 0 <= row < self.n and 0 <= col < self.n:
            self.grid[row][col] = value
        else:
            print("Index out of bounds.")
    
    def get_cell(self, row, col):
        """Returns the value of a specific cell in the grid."""
        if 0 <= row < self.n and 0 <= col < self.n:
            return self.grid[row][col]
        else:
            print("Index out of bounds.")
            return None
    
    def has_dirty_rooms(self):
        for row in self.grid:
            for room in row:
                if room.state == Room.DIRTY:
                    return True
        return False
    
    def draw_grid_state(self, n):
        """Draws an n x n grid with row and column labels in the console."""
        for row in range(n):
            # Print row label
            print(row, end=" | ")
            for col in range(n):
                state = self.grid[row][col].state
                print(state, end=" ")
            print()
        return ""
            
    def __str__(self):
        print(f"Grid of size {self.n}x{self.n}")
        return f"{self.draw_grid_state(self.n)}"

import random

class Room:
    # constants that represent the state of the room. Only clean and dirty states are considered.
    CLEAN = 0
    DIRTY = 1
    
    def __init__(self, posX, posY, state):
        self.posX = posX
        self.posY = posY
        self.state = state
    
    def update_position(self, posX, posY):
        self.posX = posX
        self.posY = posY
        
    def update_state(self, state):
        self.state = state
        
    def randomize_state():
        return random.choice([Room.CLEAN, Room.DIRTY])
    
    def __str__(self):
        state_str = self.state == self.CLEAN and "clean" or "dirty"
        return f"Room at ({self.posX}, {self.posY}) with state {state_str}"

# Example usage
if __name__ == "__main__":
    size = 5
    my_grid = Grid(size)
    
    print("Initial grid:")
    my_grid.print_grid()
    
    my_grid.update_cell(2, 3, 7)
    print("\nGrid after updating cell (2, 3) with value 7:")
    my_grid.print_grid()
    
    value = my_grid.get_cell(2, 3)
    print(f"\nValue at cell (2, 3): {value}")
