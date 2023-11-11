#!/usr/bin/env python3
import pygame
import math
import random

# set up display
pygame.init()
WIDTH, HEIGHT = 1500, 900 #making the constant variables in caps as convention
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman by Trisha")

#button variables
RADIUS = 20
GAP = 15
letters = [] # [x, y, letter, boolean to make letter disappear]
startx = round((WIDTH - (RADIUS * 2 + GAP)*13)/2)
starty = 800
A = 65 # ASCII values with increment i
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2)) # // means ignore the decimal part after division
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 80)


# loading of images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

print(images)

# game variables
hangman_status = 0 # status of where we are in the game
words = ["JUHI", "SRUTHI", "HUSNA", "SNIGDHA"]
word = random.choice(words)
guessed = []

#colours
BLUE = (137, 207, 240)
BLACK = (0,0,0)

# setup game loop
FPS = 60 # frames per second, it determines the speed of the game
clock = pygame.time.Clock()
run = True

def draw(): 
    win.fill(BLUE)

    #draw title
    text = TITLE_FONT.render("developer hangman", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word : 
        if letter in guessed :
            display_word += letter + " "
        else :
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (800, 400))

    # draw buttons
    for letter in letters :
        x, y, ltr, visible = letter
        if visible : 
            pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3) #we write win because we want to draw it on the window, ergo location
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x-text.get_width()/2, y-text.get_height()/2))
        
    win.blit(images[hangman_status], (100,50))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(2000)
    win.fill(BLUE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
    

while run :
    clock.tick(FPS) #to make sure the clock runs at the FPS set at the start


    #using a for loop to check for events
    for event in pygame.event.get(): #stores events that happen, we will loop through events and store the one happeneing here 
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN : #clicking of mouse functionality
            m_x, m_y = pygame.mouse.get_pos() #x and y coordinate of the mouse
            for letter in letters :
                x, y, ltr, visible = letter
                if visible : 
                    dis = math.sqrt((x-m_x)**2 + (y-m_y)**2)
                    if dis < RADIUS :
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1

    draw()

# checking so see if the user won
    won = True
    for letter in word :
        if letter not in guessed :
            won = False
            break

    if won :
        display_message("YOU WON OMG")
        break

    if hangman_status == 6 :
        display_message("loser lmao")
        break

