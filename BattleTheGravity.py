import pygame
import random # we want blocks falling from random positions in sky
import sys #cause we use sys.exit() for quitting the game
import time
pygame.init() #initialising pygame

width = 800 #width of our game screen
height = 600 #height of our game screen
background_color = (0,0,0)
black = (0,0,0)
white = (255,255,255)
pink = (210,180,190)

#we define the parameters for our player rectangle
RED = (255,17,29)
player_size = 50
player_pos = [width/2,height- 2*player_size]

#we define our paremeters for the blocks that falls
dark_blue = (36,20,148)
light_blue = (0,0,120)
BLUE = (0,0,255)
block_size = 50
block_pos = [random.randint(0,width-block_size),0]
#block_color = [(random.randit(1,200),random.randit(1,200),random.randit(1,200))]
block_list = [block_pos] #stores the position of all blocks
speed = 10

screen = pygame.display.set_mode((width,height)) #creating a screen for our game 
pygame.display.set_caption('Battle the Gravity') 

game_over = False

crash =False

score = 0

clock = pygame.time.Clock()

myfont = pygame.font.SysFont("monospace" , 35 )
myfont1 = pygame.font.SysFont("monospace" , 65 )
font1 = pygame.font.SysFont("comicsansms", 40)
font4 = pygame.font.SysFont("comicsansms", 60)
font5 = pygame.font.SysFont("comicsansms", 70)
font2 = pygame.font.SysFont("comicsansms", 80)
font3 = pygame.font.SysFont("comicsansms", 30)

# button_width = 200
# button_height = 70
# button_pos = [width/3 , height/2]
yellow =(255,255,0)


def collision(score, myfont,yellow,width,height,screen) :
	background_color = (0, 0, 0)
	screen.fill(background_color)
	text ="GAME OVER"
	label = font2.render(text,1,white)
	screen.blit(label,(width/5,height/5))
	text = "SCORE : " + str(score)
	label = font1.render(text,1,white)
	screen.blit(label ,(width-300,height-80))
	return screen

def set_level(score,speed):
	speed = score/10 + 4; 
	return speed

def drop_blocks(block_list): #function to create new blocks
	delay = random.random() #generates random decimal value between 0 and 1
	#if we dont use the delay then all the blocks are generated at the same time(in consecutive loops),
	# now by using delay we have added an additional condition that wont always be true, 
	#thus the blocks now will not all be generated at the same time and thus will be scattered on the screen
	if len(block_list) < 10 and delay <0.2: #if no of blocks is less than 10 then keep on adding blocks		
		x_pos = random.randint(0,width-block_size)
		y_pos = 0
		block_list.append([x_pos, y_pos])
		#block_color.append([(random.randit(1,200),random.randit(1,200),random.randit(1,200))])


def draw_blocks(block_list) : #function defines the block rectangle
	for block_pos in block_list:
		pygame.draw.rect(screen,BLUE,(block_pos[0],block_pos[1],block_size,block_size)) #we make the block rectangle

def update_block_position(block_list , score): #function to update block position and delete blocks
	for idx, block_pos in enumerate(block_list) :
		if block_pos[1] >=0 and block_pos[1] < height:
			block_pos[1] += speed
		else:
			block_list.pop(idx) #deleting old blocks
			score += 1 #for each block the player has escaped we increase the score
	return score

def detect_collision(player_pos, block_pos): #checks for collision of player with a block
	x = player_pos[0]
	y = player_pos[1]
	x1 = block_pos[0]
	y1 = block_pos[1]

	if (x1 >= x and x1 < (x + player_size)) or (x >= x1 and x < (x1 + block_size)): #detects x overlap

		if (y1 >= y and y1 < (y + player_size)) or (y >= y1 and y < (y1 + block_size)): #detects y overlap
			return True
	return False

def collision_check(block_list , player_pos): #runs detect_collision for each block
	for block_pos in block_list :
		if detect_collision(player_pos, block_pos):
			return  True
	return False		

def button (msg,x_coordinate,y_coordinate,width1,height1,inactive_color,active_color) :	
	mouse = pygame.mouse.get_pos()
	if x_coordinate + width1 > mouse[0] > x_coordinate and y_coordinate + height1 > mouse[1] > y_coordinate :
		pygame.draw.rect(screen,active_color,(x_coordinate,y_coordinate,width1,height1))
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONUP:
		  		return False

	else :
		pygame.draw.rect(screen,inactive_color,(x_coordinate,y_coordinate,width1,height1))		
										
	label = font1.render(msg,1,white)
	screen.blit(label ,(x_coordinate + 10 ,y_coordinate + 5))
	return True	

#funtion for the start screen of game
def start_game():

	start = True
	while start :
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		screen.fill(black)
		text = "Battle The Gravity"
		label = font4.render(text,1,white)
		screen.blit(label ,(width/4 - 40,height/4))
				
		text = "START"
		start = button(text,width/3 + 60,height/2 + 20,160,70,light_blue,BLUE)
		pygame.display.update()


def game_pause() :
	game_pause = True

	while game_pause :
		for event in pygame.event.get() : #the events here refers to the input given		
			if event.type == pygame.QUIT: #if we press the close option on game window then quit game
				sys.exit()	

		#screen.set_alpha(0)		
		#s= pygame.Surface((800,600), pygame.SRCALPHA)
		# s.set_alpha(128)
		#s.fill((255,255,255,0))
		#screen.blit(s , (0,0))
		#screen.fill((255,255,255,0))
		text = "GAME PAUSED"
		label = font5.render(text,1,white)
		screen.blit(label ,(width/4 - 55 ,height/4))

		text = "CONTINUE"
		game_pause = button(text,180,height/2,250,70,light_blue,BLUE)
		
		#sys exit if the user presses the quit button
		text = "QUIT"
		quit = button(text,width/2 + 60 ,height/2  ,135,70,light_blue,BLUE)

		# text = "SCORE : " + str(score)
		# label = font3.render(text,1,white)
		# screen.blit(label ,(width-300,height-80))
		
		if not quit :
			sys.exit()
		
		pygame.display.update()
		

	return False			

#funtion for the game over screen with restart and quit options
def game_over_fun(score ,myfont,yellow,width,height,screen) :
	
	game_over = True

	while game_over :
		for event in pygame.event.get() : #the events here refers to the input given		
			if event.type == pygame.QUIT: #if we press the close option on game window then quit game
				sys.exit()	

		screen = collision(score, myfont,yellow,width,height,screen)
		
		#the game_over function will return if replay is pressed
		text = "REPLAY"
		game_over = button(text,200,height/2,170,70,light_blue,BLUE)
		
		#sys exit if the user presses the quit button
		text = "QUIT"
		quit = button(text,width/2 + 60 ,height/2  ,135,70,light_blue,BLUE)
		
		if not quit :
			sys.exit()
		
		pygame.display.update()
		

	return False
				
start_game()

while not game_over :
	
	for event in pygame.event.get() : #the events here refers to the input given
		
		if event.type == pygame.QUIT: #if we press the close option on game window then quit game
			sys.exit()

		if event.type == pygame.KEYDOWN: #keydown refers to the pressing of a key
					
			if event.key == pygame.K_LEFT:
		 		player_pos[0] -= player_size
			elif event.key == pygame.K_RIGHT:
				player_pos[0] += player_size
			elif event.key == pygame.K_UP:
				player_pos[1] -= player_size
			elif event.key == pygame.K_DOWN:
				player_pos[1] += player_size
			elif event.key ==  pygame.K_SPACE:
					game_pause()	

	screen.fill(background_color) #when the rectangle moves we need to fill the previous position of rectangle  as black	
	
	drop_blocks(block_list)
	score = update_block_position(block_list , score)	
	speed = set_level(score,speed)

	text = "Score:" + str(score)
	label = myfont.render(text,1,yellow)
	screen.blit(label ,(width-200,height-40))

	if collision_check(block_list,player_pos) or player_pos[0] < 0 or (player_pos[0] > (width- player_size)) or player_pos[1]<0 or (player_pos[1] > (height - player_size) ) :
		game_over = game_over_fun(score, myfont,yellow,width,height,screen)
		#the game_over_fun will return only when user chooses to replay , so we assign the initial values to following parameters
		score = 0
		block_pos = [random.randint(0,width-block_size),0]
		block_list = [block_pos] #stores the position of all blocks
		player_pos = [width/2,height- 2*player_size]

	
	else :	
		draw_blocks(block_list)
	
		pygame.draw.rect(screen,RED,(player_pos[0],player_pos[1],player_size,player_size))#we make the player rectangle

		clock.tick(30); #this means that we want 3o frames per sec

	pygame.display.update() #updates the screen everytime the while loop runs

