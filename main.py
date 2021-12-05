# MAIN PROGRAM

# Python only looks in a limited list of directories if wanting to import modules. 
# This list can be accessed in the sys.path, after importing sys
# The first item on this list is the root directory of this program
# Rather than providing a static directory, sys.path[0] can be interpolated with /modules/ extension
import sys
sys.path.append(f"{sys.path[0]}/modules/")


from classes.game import *
#game Class has already imported Snake and Yummies and instantiated them within itself


if __name__ == "__main__":
    game = Game()  # this is our Game class
    game.run()     # execute the function run from Game




    

