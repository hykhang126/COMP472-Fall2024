# create an agent class that will interact with the environment
# agent can move up down left right
# agent can detect if the room is clean or dirty. If the room is dirty it will clean it
# agent stops when all rooms are clean
from Environment import Room
import random

class Agent:
    def __init__(self, grid):
        self.grid = grid
        self.posX = 0
        self.posY = 0
        
    def move(self, direction):
        if direction == "up":
            self.posX -= 1
        elif direction == "down":
            self.posX += 1
        elif direction == "left":
            self.posY -= 1
        elif direction == "right":
            self.posY += 1
        else:
            print("Invalid direction.")
        
    def clean(self):
        if self.grid.get_cell(self.posX, self.posY) == Room.DIRTY:
            self.grid.update_cell(self.posX, self.posY, Room.CLEAN)
            print(f"Room ({self.posX}, {self.posY}) cleaned.")
        else:
            print(f"Room ({self.posX}, {self.posY}) is already clean.")
    
    def detect(self):
        if self.grid.get_cell(self.posX, self.posY) == Room.DIRTY:
            print(f"Room ({self.posX}, {self.posY}) is dirty.")
            return True
        else:
            print(f"Room ({self.posX}, {self.posY}) is clean.")
            return False
    
    def run(self):
        while self.grid.has_dirty_rooms():
            if (self.detect()) : self.clean()
            print(self.grid)
            # Add position check
            self.move(random.choice(["up", "down", "left", "right"]))
        
        print("All rooms are clean.")