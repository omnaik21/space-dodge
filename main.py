import pygame
import time
import random
pygame.font.init()     #initializing the font module
# =====================================================================================
WIDTH, HEIGHT = 1000, 800                                       
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5                   #How many pixels player moves

STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont('comicsans', 30)    # font object

# =======================================================================================
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# display is the mode responsible for display
# set_mode is used to initilizes the window and we specify the width and height in the tuple.

pygame.display.set_caption("Space Dogde")

#The display module handles things related to the game window/screen.
#set_caption() is a function that sets the title of the game window.

# ====At the current stage of the program, the window appears and closes immediately.

# To fix this issue, we need to set up the main game loop, which is while loop.

#===========================================================================================

BG = pygame.transform.scale(pygame.image.load('BG.jpg'),(WIDTH, HEIGHT))  #loading background image form local computer
# we have now back ground image.
# need to display on the screen
# pygame.transform.scale ==> used to scale the bg image



# draw function ==> show background image on game window and update screen with latest changes
# player is argument in draw function

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0,0))      # Draw image onto game display
    
    time_text = FONT.render(f'Time: {round(elapsed_time)}sec', 1, 'white')
    WIN.blit(time_text,(10,10)) # To render the above text on the screen
    
    pygame.draw.rect(WIN,'red', player) # Draws the rectangle player on the game window
    
    for star in stars:
        pygame.draw.rect(WIN, 'white', star)
    
    
    pygame.display.update()  # Function that updates the screen with the latest changes



# =======================================================================================
# function main() => where main game logic exist
def main():
    run = True
    
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT) # creates a rectangle player a position(x,y)
    
    clock = pygame.time.Clock()
    
    start_time = time.time()   # will give us the current time, we will grab the current time when the game start.
    elapsed_time = 0
    
    
    star_add_increment = 2000    # first star increment in 2000 milli second
    star_count = 0               # These variable tells us, when we should add the next star
    
    stars = []                   # stores stars currently on screen, then draw all of them inside of these list    
    hit = False

    while run:
        
        star_count += clock.tick(60)       #Try to limit the game loop to a maximum of 60 iterations (frames) per second.
        # star_count += clock.tick(60) ==> returns number of millisecond when the last clock tick
        
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
                
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0
        
        
        elapsed_time = time.time() - start_time    # game start time - current time, gives the game playing time
        
        # quit event  
        for event in pygame.event.get():   # pygame.event.get() -- It contains a list of events that have already occurred.
            if event.type == pygame.QUIT:  # This code checks whether the current event is the user trying to close the game window.
                run = False                # end the while loop
                break                      # end the for loop
            
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_WIDTH + PLAYER_VEL <= WIDTH:
            player.x += PLAYER_VEL
            
            
        
        for star in stars[:]:                # removing the stars from stars list who hiting the bottom or player
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
            
        
        
        if hit:
            lost_text = FONT.render("GAME OVER!!", 1, 'white')
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_width()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        
        
        draw(player, elapsed_time, stars)                             # calling draw function, player is argument
        
    pygame.quit()   # it close the pygame window for us
    

if __name__ == "__main__":    #This line checks, is this Python file being run directly?
    main()                    # calling main() function
    