import pygame
from sys import exit
from random import randint
def display_score():
    text_font = pygame.font.Font(None, 50) 
    current_time = pygame.time.get_ticks()//1000 - start_time
    score_surf= text_font.render(f'Score:{current_time}', False, (0, 0, 0))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time
def obstacle_movement(obstacle_list):
    obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > - 100]
    if obstacle_list:
        for obstacles_rect in obstacle_list:
            obstacles_rect.x -= 5
            if obstacles_rect.bottom == 410:
             screen.blit(snail_surface, obstacles_rect)
            else:
                screen.blit(fly_surface, obstacles_rect)
    return obstacle_list
def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                
                return False
    return True
pygame.init()
current_time = pygame.time.get_ticks()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Basic Pygame Scene")
clock = pygame.time.Clock()
ground_surface = pygame.image.load('ground.jpeg').convert()
ground_surface = pygame.transform.scale(ground_surface, (800, 600))# Color of it
snail_surface = pygame.image.load('snail.png').convert_alpha()
snail_surface =pygame.transform.scale(snail_surface,(60, 70))
player_surface = pygame.image.load('player.png').convert_alpha()
player_surface = pygame.transform.scale(player_surface,(60, 150))
player_rect = player_surface.get_rect(topleft = (40, 280))
snail_rect = snail_surface.get_rect(bottomright = (800, 410))
home_boy = pygame.image.load('homescreen.png').convert_alpha()
home_boy = pygame.transform.scale(home_boy, (300,300))
home_boy_rect = home_boy.get_rect(center = (400, 300))
test_font = pygame.font.Font(None, 50)
game_name = test_font.render('Software Runners', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 100))
game_command = test_font.render('Press the space bar to continue', False, (111, 196, 169))
game_command_rect = game_command.get_rect(center = (400, 500))
score = 0
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)
player_gravity = -20
game_active = False
x_position = 800
start_time = 0
obstacle_rect_list = []
fly_surface = pygame.image.load('fly.png').convert_alpha()
fly_surface= pygame.transform.scale(fly_surface, (60, 70))
with open('gamestats.txt', 'r') as high_score_file:
    high_score_val = int(high_score_file.readline())
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                       
            pygame.quit()
            exit() 
    # if event.type == pygame.MOUSEMOTION: # This is to check the coordinates
    #     print(event.pos)
        if game_active:
            if event.type == pygame.KEYDOWN and player_rect.bottom >= 410:
              if event.key == pygame.K_SPACE and player_rect.bottom >= 410:
                player_gravity = -25
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800
        if event.type == obstacle_timer and game_active:
            if randint(0, 2):
             obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100), 410)))
            else:
                obstacle_rect_list.append(fly_surface.get_rect(bottomright = (randint(900, 1100), 300)))
    if game_active:
        screen.blit(ground_surface, (0, 0)) 
        display_score()
        # snail_rect.left -= 4
        # if snail_rect.right <= 0:
        #     snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 410:
            player_rect.bottom = 410
            player_gravity = 0
        screen.blit(player_surface,player_rect)
        obstacle_movement(obstacle_rect_list)
        # if snail_rect.colliderect(player_rect):
            
        #     game_active = False
        game_active = collisions(player_rect, obstacle_rect_list)   
        if game_active == False:
            score = display_score()
            high_score_val = max(score, high_score_val)
            with open('gamestats.txt', 'w') as high_score_file:
              high_score_file.write(str(high_score_val))
    else:
        obstacle_rect_list.clear()
        player_rect.topleft = (40, 280)
        player_gravity = 0
        score_message = test_font.render(f'Your score:{score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 500))
        high_score = test_font.render(f'High score :{high_score_val}',False, (111, 196, 169) )
        high_score_rect = high_score.get_rect(topleft = (10, 25)) 
        start_time = (pygame.time.get_ticks())//1000 # See what it does is start_time is pygame.time.get_ticks but it tells till how much time 
        # our program has run initially both are at same position but slowly it changes and we get this
        screen.fill((94, 129, 162))
        screen.blit(home_boy, home_boy_rect)
        screen.blit(game_name, game_name_rect)
        screen.blit(high_score, high_score_rect)
        if score == 0:
         screen.blit(game_command, game_command_rect)
        else:
            screen.blit(score_message, score_message_rect)
    pygame.display.update()
    clock.tick(60)
    
  
    # keys = pygame.key.get_pressed()
   
    # # if keys[pygame.K_SPACE]:
    # #     print('Jump')
    # # if player_rect.colliderect(snail_rect):
    # #     mouse_pos = pygame.mouse.get_pressed()
    # #     print("Collision")
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #    print( pygame.mouse.get_pressed())
    #    print('collision')
   # pygame.draw.line(screen, 'Gold', (0,0),pygame.mouse.get_pos(), 10) This will help us to create a line that follows 
   # Further I have to add various difficulties and also increasing difficulty and add different characters if possible and various buttons
   
