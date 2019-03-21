#首先输入行数列数
#esc退出
#r复位
#t提示

import numpy as np
import pygame
from pygame.locals import *
import random

class Labyrinth:

	def __init__(self, rows=30, cols=40):

		self.rows = rows
		self.cols = cols
		self.keep_going = 1
		#keep_going = 1代表生成继续进行
		self.M=np.zeros((rows,cols,3), dtype=np.uint8) 
		self.laby=np.ones((rows*2+1,cols*2+1),dtype=np.uint8)
		self.N=np.zeros((rows*2+1,cols*2+1,2), dtype=np.uint8)
		self.start=[1,0]
		self.end = [rows*2-1, cols*2]
		self.direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
		
	def createlaby(self):
		M = self.M 
		r = 0 #row
		c = 0 #column
		history = [(r,c)]
		rows=self.rows
		cols=self.cols
		while history: 	
			r,c = random.choice(history)
			#随机选个格子
			M[r,c,2] = 1
			history.remove((r,c))	
			check = []		
			if c > 0:
				if M[r,c-1,2]==1:			
					check.append('L')		
				elif M[r,c-1,2]==0:		
					history.append((r,c-1))			
					M[r,c-1,2]=2	
			if r > 0:
				if M[r-1,c,2]==1:
					check.append('U') 		
				elif M[r-1,c,2]==0:
					history.append((r-1,c))
					M[r-1,c,2]=2
			if c < cols-1:
				if M[r,c+1,2]==1:
					check.append('R')
				elif M[r,c+1,2]==0:
					history.append((r,c+1))
					M[r,c+1,2]=2
			if r < rows-1:
				if M[r+1,c,2]==1:
					check.append('D')
				elif  M[r+1,c,2]==0:
					history.append((r+1,c))
					M[r+1,c,2]=2
			#开墙
			#M(右，下，visited)	
			if len(check):
				move_direction=random.choice(check)
				if move_direction=='L':
					M[r,c-1,0]=1
				elif move_direction == 'U':
					M[r-1,c,1]=1
				elif move_direction == 'R':
					M[r,c,0]=1
				elif move_direction == 'D':
					M[r,c,1]=1
				else:
					print('Error:select one of wall')									 
		laby = self.laby
		#laby矩阵中0代表路，1代表墙
		for row in range(0,rows):
			for col in range(0,cols):
				cell_data = M[row,col]
				laby[2*row+1,2*col+1]=0
				if cell_data[0] == 1: 
					laby[2*row+1,2*col+2]=0
				if cell_data[1] == 1:
					laby[2*row+2,2*col+1]=0		
		laby[1][0]=0
		laby[-2][-1]=0
		N=self.N
		for i in range(0,2*rows):
			for j in range(0,2*cols):
				if laby[i,j]==1:
					N[i,j,0]=1
					N[i,j,1]=1
				elif laby[i,j]==0: 
					if laby[i,j+1]==1:
						N[i,j,0]=1
					if laby[i+1,j]==1:
						N[i,j,1]=1
		N[2*rows,:,0]=N[2*rows,:,1]=N[:,2*cols,0]=N[:,2*cols,1]=1
		
		return laby
		
	def solve_laby(self,i,j):
		#解迷宫
		self.start=[i,j]
		steps=self.walk()
		last =steps[len(self.laby) - 2][len(self.laby[0]) - 1]
		lookup_path = [[len(self.laby) - 2, len(self.laby[0]) - 1], ]		
		while last > 0:
			last -= 1
			index = lookup_path[-1]			
			for d in self.direction:
				move=[0,0]
				move[0]=index[0]+d[0]
				move[1]=index[1]+d[1]				
				val, err = self.at(steps, move)
				if val == last:
					lookup_path.append(move)
					break
		lookup_path.pop()
		lookup_path.reverse()
		lookup_path.pop()
		lookup_path.append([i,j])
		return lookup_path
	
	def at(self, grid, x):
		#解迷宫
		if x[0] < 0 or x[0] >= len(grid):
			return 0,False
		if x[1] < 0 or x[1] >= len(grid[0]):
			return 0,False
		return grid[x[0]][x[1]], True
		
	def walk(self):
		#解迷宫
		steps = [[i * 0 for i in range(len(self.laby[0]))] for j in range(len(self.laby))]
		Q = [self.start]
		while len(Q) > 0:
			index = Q[0]
			if index == self.end:
				break	
			Q = Q[1:]
			for d in self.direction:
				move=[0,0]
				move[0]=index[0]+d[0]
				move[1]=index[1]+d[1]
				val, ok = self.at(self.laby,move)
				if not ok or val == 1:
					continue
				val, ok = self.at(steps,move)
				if not ok or val != 0:
					continue
				if move == self.start:
					continue
				val, ok = self.at(steps, index)
				if ok:
					steps[move[0]][move[1]] = val + 1
				Q.append(move)
		return steps


class Game:

	def __init__(self,num_rows,num_cols):
		self.size = (600,600)
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption('Labyrinth')
		font = pygame.font.SysFont(pygame.font.get_default_font(), 55)
		text = font.render("Generating...", 1, (255,255,255))
		rect = text.get_rect()
		rect.center = self.size[0]/2, self.size[1]/2
		self.screen.blit(text, rect)
		pygame.display.update(rect)
		self.rows=num_rows
		self.cols=num_cols
		self.solve_laby=False

	def start(self):
		if True:
			self.laby_obj = Labyrinth(self.rows,self.cols)
		else:
			self.laby_obj = Labyrinth(10,10)
		self.laby_obj.createlaby()
		self.draw_laby()
		self.reset_player()
		self.loop()

	def draw_laby(self):
		self.screen.fill((255,255,255))
		self.cell_width = self.size[0]/(self.cols*2+1)
		self.cell_height = self.size[1]/(self.rows*2+1)
		cols=self.cols
		rows=self.rows
		for i in range(rows*2+1):
			for j in range(cols*2+1):
				if self.laby_obj.laby[i,j]==1:
					pygame.draw.rect(self.screen,(0,0,0),(j*self.cell_width,\
					i*self.cell_height,self.cell_width+1,self.cell_height+1))
		pygame.display.update()

	def reset_player(self):
		# Make the sprites for the player.
		rect = 0, 0,self.cell_width, self.cell_height
		rows=self.rows
		cols=self.cols

		base = pygame.Surface((self.cell_width, self.cell_height))
		base.fill((255,255,255))
		self.red = base.copy()
		self.green = base.copy()
		self.blue_p = base.copy()
		self.white = base.copy()
		r = (255,0,0)
		g = (0,255,0)
		b = (0,0,255)
		white=(255,255,255)
		pygame.draw.ellipse(self.blue_p, b, rect)
		pygame.draw.ellipse(self.green, g, rect)
		pygame.draw.ellipse(self.white, white, rect)
		pygame.draw.ellipse(self.red, r, rect)
		
		#player_laby矩阵，实时储存经过地点
		self.player_laby =np.zeros((2*rows+1,2*cols+1), dtype=np.uint8)
		for i in range(rows*2+1):
			for j in range(cols*2+1):
				if self.laby_obj.laby[i,j]==0:
					self.screen.blit(base, (j*self.cell_width, i*self.cell_height))
		self.screen.blit(self.green, (cols*2*self.cell_width, (rows*2-1)*self.cell_height))
		self.cx =0
		self.cy =1
		self.last_move = None # For last move fun
		self.solve_laby=False

	def loop(self):
		self.clock = pygame.time.Clock()
		self.keep_going = 1

		while self.keep_going:
			moved = 0
			self.clock.tick(10)
			for event in pygame.event.get():
				if event.type == QUIT:
					self.keep_going = 0
				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						self.keep_going = 0
					if event.key == K_r:
						self.reset_player()
					if event.key==K_t:
						self.solve_laby=True
						self.pathes=self.laby_obj.solve_laby(self.cy, self.cx)
					if event.key == K_DOWN:
						self.move_player('d')
						moved = 1
					if event.key == K_UP:
						self.move_player('u')
						moved = 1
					if event.key == K_LEFT:
						self.move_player('l')
						moved = 1
					if event.key == K_RIGHT:
						self.move_player('r')
						moved = 1
			keys = pygame.key.get_pressed()
			if not moved:
				if keys[K_DOWN]:
					self.move_player('d')
				if keys[K_UP]:
					self.move_player('u')
				if keys[K_LEFT]:
					self.move_player('l')
				if keys[K_RIGHT]:
					self.move_player('r')

			self.draw_player()
			pygame.display.update()
		
	def move_player(self, dir):
		#M(右，下，visited)
		no_move = 0
		try:
			if dir == 'u':
				if not self.laby_obj.N[self.cy-1,self.cx,1]:
					self.player_laby[self.cy, self.cx]+= 1
					self.cy -= 1 
				else: no_move = 1
			elif dir == 'd':
				if not self.laby_obj.N[self.cy,self.cx,1]:
					self.player_laby[self.cy, self.cx]+= 1
					self.cy += 1
				else: no_move = 1
			elif dir == 'l':
				if not self.laby_obj.N[self.cy,self.cx-1,0]:
					self.player_laby[self.cy, self.cx]+= 1
					self.cx -= 1
				else: no_move = 1
			elif dir == 'r':
				if not self.laby_obj.N[self.cy,self.cx,0]:
					self.player_laby[self.cy, self.cx]+= 1
					self.cx += 1
				else: no_move = 1
			else:
				no_move = 1
		except KeyError: # Tried to move outside screen
			no_move = 1


		if ((dir == 'u' and self.last_move == 'd') or \
				(dir == 'd' and self.last_move == 'u') or \
				(dir == 'l' and self.last_move == 'r') or \
				(dir == 'r' and self.last_move == 'l')) and \
				not no_move:
			self.player_laby[self.cy, self.cx]+= 1

		if not no_move:
			self.last_move = dir

		if self.cx  == 2*self.cols and self.cy+1  == 2*self.rows:
			self.keep_going = 0

	def draw_player(self):
		for i in range(self.rows*2+1):
			for j in range(self.cols*2+1):
				if self.player_laby[i,j] > 0:
						self.screen.blit(self.white, (j*self.cell_width, i*self.cell_height))
		if self.solve_laby:
			for path in self.pathes:
				self.screen.blit(self.red, (path[1]*self.cell_width, path[0]*self.cell_height))
		self.screen.blit(self.blue_p, (self.cx*self.cell_width, \
			self.cy*self.cell_height))

num_rows = int(input("Rows: ")) # 行数
num_cols = int(input("Columns: ")) # 列数
pygame.init()
g = Game(num_rows,num_cols)
g.start()
