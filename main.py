import pygame
import sys
import random
# import winsound


# ball animation 
def ball_animation():
    global ball_speed_x, ball_speed_y, opponent_score, player_score
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # collisions at the 4-sides 
    if ball.left <= 0:
        player_score+= 1
        ball_restart()   

    if ball.right >= screen_width:
        opponent_score += 1
        ball_restart()   
        
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # collisions between ball and players
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


def player_animation():
    # to keep player below top and above bottom
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():
    if opponent.top < ball.y:
        opponent.top  += (opponent_speed +4)
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
        
def ball_restart():
    global ball_speed_y, ball_speed_x
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))

# General setup
pygame.init()
clock = pygame.time.Clock()
FPS = 60

# setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')

# pygame.display.set_caption("Pong Game")


# Game Rectangles
ball = pygame.Rect(screen_width//2 - 15, screen_height//2 - 15, 30, 30)
player = pygame.Rect(screen_width-20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)


# colors
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)


# speed variables
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed =  7

# text variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)






# Main loop
while True:
    
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
                
            if event.key == pygame.K_DOWN:
                player_speed += 7
                
            if event.key == pygame.K_UP:
                player_speed -= 7
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
                
            if event.key == pygame.K_UP:
                player_speed += 7
                
            
    
    ball_animation()
    player.y += player_speed
    player_animation()
    opponent_ai()
    

    
    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))
    
    player_text = game_font.render(str(player_score), False, light_grey)
    opponent_text = game_font.render(str(opponent_score), False, light_grey) 
    screen.blit(player_text, (660, 470))
    screen.blit(opponent_text, (600, 470))
             
    pygame.display.flip()
    clock.tick(FPS)
    
    