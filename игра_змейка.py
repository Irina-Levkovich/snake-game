import pygame
import  time
import random

pygame.init()
yellow = (255,255,102)
white =(255, 255, 255)
black = (0,0,0)
green = (0,255,0)
blue = (0, 0, 255)
red = (255, 0, 0)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font_style_1=pygame.font.SysFont(None,30)
font_style = pygame.font.SysFont('bahnschrift',25)
score_font = pygame.font.SysFont('comicsansms',35)
game_over = False
game_close = False
y1 = 400
x1 = 300
x1_change = 0
y1_change = 0
snake_List = []
Length_of_snake = 1
food_x = ((random.randint(0,dis_width-10)/10)*10)
food_y = ((random.randint(0,dis_width-10)/10)*10)
snake_block = 10
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,yellow,[x[0],x[1],10,10])
def messege(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg,[dis_width/3,dis_height/3])
def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0
    y1_change = 0
    snake_List =[]
    Length_of_snake = 1
    food_x = round((random.randint(0,dis_width-10)/10)*10)
    food_y = round((random.randint(0,dis_width-10)/10)*10)

while not game_over:
    while game_close == True:
        dis.fill(white)
        message = ("Вы проиграли!",True,black)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                        gameLoop()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over= True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 10
    if x1 >=800 or x1<0 or y1>=600 or y1<0:
        game_over = True
    x1 += x1_change
    y1 += y1_change
    dis.fill (white)
    pygame.draw.rect(dis, blue, [x1, y1, 10, 10])
    pygame.draw.rect(dis, green, [food_x, food_y, 10, 10])
    snake_Head =[]
    snake_Head.append(x1)
    snake_Head.append(y1)
    if len(snake_List)>Length_of_snake:
        del snake_List[0]
    for x in snake_List[:-1]:
        if x == snake_Head:
            game_close = True
    our_snake(snake_block,snake_List)
    pygame.display.update()
    if x1 == food_x and y1 == food_y:
       # food_x = ((random.randint(0, dis_width - 10) / 10) * 10)
        #food_y = ((random.randint(0, dis_width - 10) / 10) * 10)
        Length_of_snake+=1
    pygame.display.update()
    clock.tick(25)
pygame= quit()
quit()
gameLoop()