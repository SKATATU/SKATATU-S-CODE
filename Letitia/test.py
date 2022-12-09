import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from pygame import mouse
import math
import random
from random import randint

class Settings():
    def __init__(self):
        '''basic screen settings'''
        self.screen_width = 700
        self.screen_height = 1000
        self.caption = 'BUILDING BLOCKS'

class Scoreboard1():
    def __init__(self, screen, player):
        '''basic background settings'''
        self.screen = screen
        self.image = pygame.image.load('images/0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.player = player
        self.endgamepos = (230, 500)
        self.rect.x = 40
        self.rect.y = 20

    def update(self):
        if self.player.score/10 < 1:
            self.image = pygame.image.load('images/0.png')
        elif self.player.score/10 < 2:
            self.image = pygame.image.load('images/1.png')
        elif self.player.score/10 < 3:
            self.image = pygame.image.load('images/0.png')
        elif self.player.score/10 < 4:
            self.image = pygame.image.load('images/0.png')
        elif self.player.score/10 < 5:
            self.image = pygame.image.load('images/0.png')
        elif self.player.score/10 < 6:
            self.image = pygame.image.load('images/0.png')
        elif self.player.score/10 < 7:
            self.image = pygame.image.load('images/0.png')
        elif self.player.score/10 < 8:
            self.image = pygame.image.load('images/0.png')
        elif self.player.score/10 < 9:
            self.image = pygame.image.load('images/0.png')
        if self.player.isendgame == True:
            self.rect = self.endgamepos
        self.screen.blit(self.image, self.rect) 

class Scoreboard2():
    def __init__(self, screen, player):
        '''basic background settings'''
        self.screen = screen
        self.image = pygame.image.load('images/0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.player = player
        self.endgamepos = (350, 500)
        self.rect.x = 150
        self.rect.y = 20

    def update(self):
        if self.player.score % 10 == 0:
            self.image = pygame.image.load('images/0.png')
        elif self.player.score % 10 == 1:
            self.image = pygame.image.load('images/1.png')
        elif self.player.score % 10 == 2:
            self.image = pygame.image.load('images/2.png')
        elif self.player.score % 10 == 3:
            self.image = pygame.image.load('images/3.png')
        elif self.player.score % 10 == 4:
            self.image = pygame.image.load('images/4.png')
        elif self.player.score % 10 == 5:
            self.image = pygame.image.load('images/5.png')
        elif self.player.score % 10 == 6:
            self.image = pygame.image.load('images/6.png')
        elif self.player.score % 10 == 7:
            self.image = pygame.image.load('images/7.png')
        elif self.player.score % 10 == 8:
            self.image = pygame.image.load('images/8.png')
        else:
            self.image = pygame.image.load('images/9.png')
        if self.player.isendgame == True:
            self.rect = self.endgamepos
        self.screen.blit(self.image, self.rect) 

class Background():
    def __init__(self, screen):
        '''basic background settings'''
        self.screen = screen
        self.image = pygame.image.load('images/background.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect) 

class Button():
    def __init__(self, screen, lose):
        self.screen = screen
        self.image = pygame.image.load('images/restart.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.lose = lose

        self.rect.x = lose.rect.x + 150
        self.rect.y = lose.rect.y + 300

    def blitme(self):
        self.screen.blit(self.image, self.rect) 

class Lose():
    def __init__(self, screen, player):
        '''basic background settings'''
        self.screen = screen
        self.image = pygame.image.load('images/lose.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.player = player

        self.rect.x = 100
        self.rect.y = 70

    def blitme(self):
        self.screen.blit(self.image, self.rect) 

    def winner(self):
        self.image = pygame.image.load('images/win.png')
        self.screen.blit(self.image, self.rect) 

class Player(Sprite):
    def __init__(self, screen, settings):
        '''basic character settings'''
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('images/player0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        '''set variable mass, velocity, F, and isjump for jumping'''
        self.mass = 2
        self.velocity = 3
        self.F = 0
        self.isjump = False
        '''set vatiable status for status showing'''
        self.status = 'stand'
        '''set rect.x and rect.y'''
        self.rect.y = 750
        self.rect.x = 500
        self.isendgame = False
        self.showheight = 0
        self.score = 0

    def jump(self):
        '''set isjump to be 1'''
        self.isjump = True

    def update(self):
        '''if isjump is 1, Calculate force (F)'''
        if self.isjump == True:
            '''if velocity is larger than 0, decrease rect.y by the force'''
            if self.velocity <= 0:
                self.F = -(0.5 * self.mass * (self.velocity * self.velocity))
            else:
                '''else, increase rect.y by the force'''
                self.F = (0.5 * self.mass * (self.velocity * self.velocity))

            self.rect.y = self.rect.y - self.F
            self.velocity -= 0.1

        if self.rect.y >= 900 or self.rect.y <= 0  :
                self.rect.y = 580
                self.isjump = False
                self.velocity = 3
                
        '''blit it on the screen'''
        
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

class Block(Sprite):
    def __init__(self, settings, screen, player, blocks, y, lose, button):
        '''basic character settings'''
        super(Block, self).__init__()
        self.settings = settings
        self.screen = screen
        self.player = player
        self.blocks = blocks
        self.player = player
        self.button = button
        self.lose = lose
        self.screen_rect = screen.get_rect()
        '''preapre 2 images, use random to select one'''
        self.img1 = pygame.image.load('images/block10.jpg')
        self.img2 = pygame.image.load('images/block20.jpg')
        self.image = random.randint(0, 2)
        if self.image == 1:
            self.image = self.img1
        else:
            self.image = self.img2
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = 0
        self.ismove = True
        self.isload = False
        self.score = self.player.score
        self.firstblock = False

    def check_player(self):
        '''if isload is False and collide with the player is detected'''
        if self.isload == False and pygame.sprite.collide_rect(self, self.player):
            print("collides")
            '''make isjump = 0 and reset the velocity for the player's jumping detection'''
            self.player.isjump = False
            self.player.velocity = 3
            '''change ismove to False, and change the image to the one without hands'''
            self.ismove = False
            '''check the direction of the player to the block'''
            if self.rect.y - self.player.rect.y <= 50:
                end_game(self.screen, self.lose, self.button)
                self.player.isendgame = True
            '''change the status of the player'''    
            if self.player.status == 'stand':
                '''if the status is right, change isload to True, increase the score by 1 and call reset_focus()'''
                self.isload = True
                if self.player.score == 1:
                    self.firstblock = True
                self.player.score += 1
                self.score = self.player.score
                reset_focus(self.settings, self.screen, self.player, self.blocks, self.lose, self.button)
    
    def update(self):
        '''if ismove is True, move towards right'''
        if self.ismove == True:
            if self.player.score <= 5:
                self.rect.x += 3
            elif self.player.score <= 15:
                self.rect.x += 5
            elif self.player.score <= 25:
                self.rect.x += random.randint(2, 5)
            elif self.player.score <= 28:
                self.rect.x += 7
            else:
                self.rect.x += random.randint(2, 8)
        if self.rect.x >+ self.settings.screen_width:
            end_game(self.screen, self.lose, self.button)
            self.player.isendgame = True
        '''blit it on the screen'''
        self.check_player()
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

def update_game(background, player, blocks):
    '''if the status of the player is not right, call end_game()'''
    background.blitme()
    if player.score >= 50:
        win_game(player)
    else:
        '''else, update game'''
        keyboard_test(player)
        player.update()
        blocks.update()
        pygame.display.flip()

def keyboard_test(player):
    '''check whether space is pressed'''
    keys = pygame.key.get_pressed() 
    '''if yes, call player_jump()'''
    if (keys[pygame.K_SPACE]) == 1:
        player.jump()
        print(1)

def reset_focus(settings, screen, player, blocks, lose, button):
    '''move all the object down until the player is in the middle'''
    '''sent in the new block'''
    if player.rect.y <= 400:
        movement = 50
        for blocking in blocks.sprites():         
            blocking.rect.y += movement
        player.rect.y += movement
    y = player.rect.y + 24
    create_block(settings, screen, player, blocks, y, lose, button)

def create_block(settings, screen, player, blocks, y, lose, button):  
    block = Block(settings, screen, player, blocks, y, lose, button)
    '''create a block and put it into the group'''
    block.add(blocks)
    print(player.score)

def jump_test(settings, screen, player, blocks):
    for blocking in blocks.sprites():
        if pygame.sprite.collide_rect(blocking, player):
            player.isjump = False
            player.velocity = 3

def end_game(screen, lose, button):
    lose.blitme()

def win_game(player, screen, lose):
    player.isendgame == True
    lose.winner()
    
def run_game():
    '''init. pygame, init. screen, create settings'''
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption(settings.caption)
    pygame.display.flip()

    '''create sprite and character'''
    background = Background(screen)
    player = Player(screen, settings)
    '''create a group of blocks'''
    blocks = Group()
    lose = Lose(screen, player)
    button = Button(screen, lose)
    scoreboard1 = Scoreboard1(screen, player)
    scoreboard2 = Scoreboard2(screen, player)
    create_block(settings, screen, player, blocks, 750, lose, button)

    '''control the status of the game'''
    isQuit = False 
    while isQuit != True:
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                isQuit = True     
            keyboard_test(player)
        background.blitme()
        if player.isendgame == False:
            player.update()
            blocks.update()
            jump_test(settings, screen, player, blocks)
        if player.isendgame == True:
            end_game(screen, lose, button)
            keys = pygame.key.get_pressed() 
            if (keys[pygame.K_SPACE]) == 1:
                player.isendgame = False
                player.score = 0
                pygame.sprite.Group.empty(blocks)
                player.rect.y = 750
                player.rect.x = 500
                player.isendgame = False
                player.showheight = 0
                create_block(settings, screen, player, blocks, 750, lose, button)
        scoreboard1.update()
        scoreboard2.update()
        pygame.display.flip()
    pygame.quit()

# only direct excuted code to run the game
run_game()

# photograph a robotic hand to grab the block