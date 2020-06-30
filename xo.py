import pygame
import time
from pygame.locals import *
import numpy as numpy

pygame.init()

# MOVE COUNTER 
moves = 0
# LOCATION LIST
loc_list = [[None]*3, [None]*3, [None]*3] 
# XO CHANGER
XO = 'x'
# SCORE BOARD
x_win = 0
o_win = 0
# PRIMARY COLOR USAGE
primary_color = (51,51,51)
background_color = (255,255,255)

# SURFACE DIMENSIONS
display_width = 300
display_height = 300

# BOARD PLACEMENTS
board_x = (display_width - 200)//2
board_y = (display_height - 200)//2

# ALL IMAGES NEEDED FOR THE GAME
boxImg = pygame.image.load('./images/game_bg.png')
xImg = pygame.image.load('./images/x_image.png')
oImg = pygame.image.load('./images/o_image.png')

# gameDisplay IS THE GAME SURFACE
gameDisplay = pygame.display.set_mode((display_width,display_height))

# SET TITLE HEAD TO OUR GAME
pygame.display.set_caption('X & O')

clock = pygame.time.Clock()

def game_reset():
    global XO, loc_list, loc_row, loc_colm, x_win, o_win, moves
    time.sleep(5)
    loc_list = [[None]*3, [None]*3, [None]*3]
    moves = 0
    XO = 'x'
    loc_row = None
    loc_colm = None
    x_win = int(x_win)
    o_win = int(o_win)
    game_loop()

def winner(winner_player):
    global x_win, o_win
    font = pygame.font.SysFont(None, 30)
    textWinner = font.render(winner_player.upper() + ' Wins!', True, primary_color)
    gameDisplay.blit(textWinner, (105,258))
    if winner_player == 'x':
        x_win += 1
    elif winner_player == 'o':
        o_win += 1
    scoreFont = pygame.font.SysFont(None, 20)
    scoreText = scoreFont.render('X = '+ str(x_win) +'  O = ' +str(o_win),True, primary_color)
    gameDisplay.blit(scoreText, (105, 280))        
    pygame.display.update()
    game_reset()

def welcome():
    font = pygame.font.SysFont(None, 50)
    text = font.render("X & O", True, primary_color)
    gameDisplay.blit(text, (105,15))

def Varimage(x,y):
    global XO, loc_list
    if XO == 'x':
        gameDisplay.blit(xImg,(x,y))
        XO = 'o'
    else:
        gameDisplay.blit(oImg,(x,y))    
        XO = 'x'
    pygame.display.update()

def check():
    global loc_list, winnerP, moves
    winnerP = None
    print(loc_list)
    curr_len = len(loc_list)
    # ROW CHECK
    for check_row in range(0,3):
        if((loc_list[check_row][0] == loc_list[check_row][1] == loc_list[check_row][2]) and (loc_list[check_row][0] is not None)): 
            print(loc_list[check_row][0] + ' wins')
            winnerP = loc_list[check_row][0]
            break   

    # COLUMN CHECK
    for check_colm in range(0,3):
        if((loc_list[0][check_colm] == loc_list[1][check_colm] == loc_list[2][check_colm]) and (loc_list[0][check_colm] is not None)):
            print(loc_list[0][check_colm] + ' wins')
            winnerP = loc_list[0][check_colm]
            break    

    # DIAGONAL CHECK

    if ((loc_list[0][0] == loc_list[1][1] == loc_list[2][2]) and (loc_list[0][0] is not None)):
        print(loc_list[0][0] + ' wins')
        winnerP = loc_list[0][0]   

        
    elif ((loc_list[0][2] == loc_list[1][1] == loc_list[2][0]) and (loc_list[0][2] is not None)):
        print(loc_list[0][2] + ' wins')
        winnerP = loc_list[0][2]
    
    if winnerP is not None:
        winner(winnerP)
    moves += 1
    if moves == 9:
        winnerP = "No"
        winner(winnerP)
        game_reset()    
    
              
def userClick():
    x_curr ,y_curr = pygame.mouse.get_pos()
    varImageX = 0
    varImageY = 0
    global XO, loc_list, loc_row, loc_colm
    if x_curr >= 50 and x_curr < 115:
        varImageX = 58
        colm = 1
        if y_curr > 50 and y_curr < 115: 
            varImageY = 58
            row = 1
        elif y_curr >= 115 and y_curr < 180:
            varImageY = 123
            row = 2
        elif y_curr >= 180 and y_curr < 245:
            varImageY = 188  
            row = 3
    elif x_curr >= 115 and x_curr < 180:
        varImageX = 123
        colm = 2
        if y_curr > 50 and y_curr < 115: 
            varImageY = 58
            row = 1
        elif y_curr >= 115 and y_curr < 180:
            varImageY = 123
            row = 2
        elif y_curr >= 180 and y_curr < 245:
            varImageY = 188
            row = 3
    elif x_curr >= 180 and x_curr < 245:
        varImageX = 188
        colm = 3
        if y_curr > 50 and y_curr < 115: 
            varImageY = 58
            row = 1
        elif y_curr >= 115 and y_curr < 180:
            varImageY = 123
            row = 2
        elif y_curr >= 180 and y_curr < 245:
            varImageY = 188 
            row = 3
    loc_list[row-1][colm-1] = XO
    Varimage(varImageX,varImageY)  
    check()                    
    
def board():
    gameDisplay.blit(boxImg,(board_x,board_y))

def game_loop():
    gameExit = False
    gameDisplay.fill(background_color)   
    board()
    welcome()
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type is MOUSEBUTTONDOWN:
                userClick()   
        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()          