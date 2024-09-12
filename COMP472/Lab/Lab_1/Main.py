
from Environment import Grid
import Agent

# Main
if __name__ == '__main__':
    # Create a grid of size 5
    grid = Grid(5)
    
    # Print the grid
    print(grid)
    
    Agent = Agent.Agent(grid)
    
    Agent.run()
    