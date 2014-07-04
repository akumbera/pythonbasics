import os, sys
import pygame
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

#################
#global variables
#################
cellheight = 10
cellwidth = 10
margin = 3

#colors
whiteColor = pygame.Color(255,255,255)
blackColor = pygame.Color(  0,  0,  0)
greenColor = pygame.Color(  0,255,  0)

#display
gameDisplay = pygame.display.set_mode([653,653])
pygame.display.set_caption('Conway\'s game of life.')


########
#Logic
########

def create_celllist(M):
	celllist = [[False for j in range(M)] for i in range(M)]
	return celllist

def check_neighbors(celllist,x,y):
	count = 0
	neighbors = [
			celllist[(x-1)%len(celllist)][(y-1)%len(celllist)], 
			celllist[(x-1)%len(celllist)][y], 
			celllist[(x-1)%len(celllist)][(y+1)%len(celllist)], 
			celllist[x][(y-1)%len(celllist)], 
			celllist[x][(y+1)%len(celllist)], 
			celllist[(x+1)%len(celllist)][(y-1)%len(celllist)], 
			celllist[(x+1)%len(celllist)][y], 
			celllist[(x+1)%len(celllist)][(y+1)%len(celllist)] ]
	for i in range(len(neighbors)):
		if neighbors[i-1] == True:
			count += 1
	return count

def update_board(celllist,storageList):
	for i in range(len(celllist)):
		for j in range(len(celllist[i])):
			if check_neighbors(celllist,i,j) < 2:
				cell_off(storageList,i,j)
			elif check_neighbors(celllist,i,j) == 2 and celllist[i][j] == True:
				cell_on(storageList,i,j)
			elif check_neighbors(celllist,i,j) == 3:
				cell_on(storageList,i,j)
			elif check_neighbors(celllist,i,j) >= 4:
				cell_off(storageList,i,j)


def cell_on(celllist,x,y):
	celllist[x][y]=True

def cell_off(celllist,x,y):
	celllist[x][y]=False

###############
#draw functions
###############

def color_rectangle(celllist,x,y):
	if celllist[x][y] == True:
		return blackColor
	else:
		return whiteColor

def draw_board(celllist):
	for x in range(50):
		for y in range(50):
			pygame.draw.rect(gameDisplay, color_rectangle(celllist,x,y), ((x+1)*margin + x*cellwidth,(y+1)*margin + y*cellwidth , cellheight, cellwidth))


##########
#game loop
##########
def gameLoop():
	livearray = create_celllist(50)

	livearray[0][4]=True
	livearray[0][5]=True
	livearray[1][4]=True
	livearray[1][5]=True

	livearray[10][4]=True
	livearray[10][5]=True
	livearray[10][6]=True
	livearray[11][3]=True

	livearray[11][7]=True
	livearray[12][2]=True
	livearray[12][8]=True
	livearray[13][2]=True

	livearray[13][8]=True
	livearray[14][5]=True
	livearray[15][3]=True
	livearray[15][7]=True

	livearray[16][4]=True
	livearray[16][5]=True
	livearray[16][6]=True
	livearray[17][5]=True

	livearray[20][2]=True
	livearray[20][3]=True
	livearray[20][4]=True
	livearray[21][2]=True

	livearray[21][3]=True
	livearray[21][4]=True
	livearray[22][1]=True
	livearray[22][5]=True

	livearray[24][0]=True
	livearray[24][1]=True
	livearray[24][5]=True
	livearray[24][6]=True

	livearray[34][2]=True
	livearray[34][3]=True
	livearray[35][2]=True
	livearray[35][3]=True

	while True:
		storagearray = create_celllist(50)

		gameDisplay.fill(whiteColor)

		draw_board(livearray)
		update_board(livearray,storagearray)
		livearray = storagearray[:][:]

		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()
		fpsClock.tick(10)


gameLoop()