#code created by Meerashine Joe

import pygame
from game import Game
import time


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 576
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

"""def game_intro(screen,clock):

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
        screen.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)"""

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def get_current_time():
    return round(time.time() * 1000)




def main():
    # Initialize all imported pygame modules
    pygame.init()
    # Set the width and height of the screen [width, height]
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    # Set the current window caption
    pygame.display.set_caption("PACMAN")
    
    #Loop until the user clicks the close button.
    done = False
    display_crash_text = True
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    #########
    bg = pygame.image.load(r".\Background\Unticccctled-1.jpg")
    #game_intro(screen,cloc
    screen.fill(black)
    largeText = pygame.font.SysFont('Helvetica',100)
    subText = pygame.font.SysFont('Helvetica',30)
    TextSurf, TextRect = text_objects("", largeText)
    subSurf, subRect = text_objects("", subText)
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    #subRect.bottom = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    start_time = get_current_time()
    while display_crash_text:
        screen.blit(bg,(50,0))
        screen.blit(TextSurf, TextRect)
        screen.blit(subSurf, subRect)
        pygame.display.update()

        if get_current_time() - start_time < 2500:
            display_crash_text= True

            
        else:
            display_crash_text = False
            print(display_crash_text)
    #while display_crash_text == True:
    
    while not display_crash_text:
        #clock.tick(60)
        
    # Create a game object
        game = Game()
    # -------- Main Program Loop -----------
        while not done:
    # --- Process events (keystrokes, mouse clicks, etc)
            done = game.process_events()
        # --- Game logic should go here
            game.run_logic()
        # --- Draw the current frame
            game.display_frame(screen)
        # --- Limit to 30 frames per second
            clock.tick(30)
        #tkMessageBox.showinfo("GAME OVER!","Final Score = "+(str)(GAME.score))
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
        pygame.quit()

if __name__ == '__main__':
    main()
