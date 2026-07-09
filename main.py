import pygame
import time
import random

WIDTH, HEIGHT = 1000, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# display is the mode responsible for display
# set_mode is used to initilizes the window and we specify the width and height in the tuple.

pygame.display.set_caption("Space Dogde")

#The display module handles things related to the game window/screen.
#set_caption() is a function that sets the title of the game window.

# ====At the current stage of the program, the window appears and closes immediately.

# To fix this issue, we need to set up the main game loop, which is while loop.

# function main() => where main game logic exist
def main():
    run = True

    while run:
        for event in pygame.event.get():   # pygame.event.get() -- It contains a list of events that have already occurred.
            if event.type == pygame.QUIT:  # This code checks whether the current event is the user trying to close the game window.
                run = False                # end the while loop
                break                      # end the for loop
    pygame.quit()   # it close the pygame window for us
    

if __name__ == "__main__":    #This line checks, is this Python file being run directly?
    main()                    # calling main() function
    