#By Austin Kumbera
#Freeware
#
#TODO
# -add in game score and game over displays
#

import math
import random

import pygame
from pygame.locals import *

class Game(object):
	def main(self, screen):
		clock = pygame.time.Clock()

		self.score = 0

		#sprites
		background = pygame.image.load('background.png')
		self.sprites = pygame.sprite.Group()

		self.ship = Ship(self.sprites)

		self.asteroids = pygame.sprite.Group()
		for i in range(10):
			Asteroid(self.asteroids)
		self.sprites.add(self.asteroids)

		#sounds
		self.shoot = pygame.mixer.Sound('laser.wav')
		self.explosion = pygame.mixer.Sound('explode.wav')

		while 1:
			dt = clock.tick(30)
			
			for event in pygame.event.get():
				if event.type == QUIT:
					print 'Your score was %s' %self.score
					return
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						print 'Your score was %s' %self.score
						return

			self.sprites.update(dt/1000., self)
			screen.blit(background, (0,0))
			self.sprites.draw(screen)
			pygame.display.flip()

			if self.ship.is_dead:
				print 'Game Over. Your score was %s' %self.score
				return


class Ship(pygame.sprite.Sprite):
	def __init__(self, *groups):
		super(Ship, self).__init__(*groups)
		self.original_image = pygame.image.load('ship.png')
		self.image = self.original_image
		self.rect = pygame.rect.Rect((320,240), self.image.get_size())
		self.angle = 0
		self.cooldown = 0
		self.radius = 5
		self.is_dead = False

	def update(self, dt, game):
		last = self.rect.copy()

		#get user input
		buttons = pygame.key.get_pressed()
		#movement
		if buttons[K_LEFT]:
			self.angle += 10
			self.image = pygame.transform.rotate(self.original_image, self.angle)
		if buttons[K_RIGHT]:
			self.angle -= 10
			self.image = pygame.transform.rotate(self.original_image, self.angle)
		if buttons[K_UP]:
			self.rect.x -= 10 * math.sin(math.radians(self.angle))
			self.rect.y -= 10 * math.cos(math.radians(self.angle))
		if buttons[K_DOWN]:
			self.rect.x += 10 * math.sin(math.radians(self.angle))
			self.rect.y += 10 * math.cos(math.radians(self.angle))

		#action
		if buttons[K_SPACE] and not self.cooldown:
			game.shoot.play()
			Bullet(self.rect.center, self.angle, game.sprites)
			self.cooldown = 1
		self.cooldown = max(0, self.cooldown - dt)

		#semi-torroidal behavior
		if last.centerx < 0:
			self.rect.centerx = 639
		if last.centerx > 640:
			self.rect.centerx = 1
		if last.centery < 0:
			self.rect.centery = 479
		if last.centery > 480:
			self.rect.centery = 1

class Asteroid(pygame.sprite.Sprite):
	def __init__(self, *groups):
		super(Asteroid,self).__init__(*groups)
		self.original_image = pygame.image.load('asteroid.png')
		self.image = self.original_image
		self.rect = pygame.rect.Rect((random.randint(0,480),0), self.image.get_size())
		#self.direction = random.randint(0,1)
		self.heading = random.randint(0,360)
		self.radius = 15

	def update(self, dt, game):
		last = self.rect.copy()

		#rotates in a random direction
		#if self.direction == 0:
		#	angle = -90
		#else:
		#	angle = 90
		#self.image = pygame.transform.rotate(self.original_image, angle)

		#moves in a random direction
		self.rect.x += 5 * math.sin(math.radians(self.heading))
		self.rect.y += 5 * math.cos(math.radians(self.heading))

		#semi-torroidal behavior
		if last.centerx < 0:
			self.rect.centerx = 639
		if last.centerx > 640:
			self.rect.centerx = 1
		if last.centery < 0:
			self.rect.centery = 479
		if last.centery > 480:
			self.rect.centery = 1

		#collision detection
		if pygame.sprite.collide_circle(self, game.ship) == True:
			game.ship.is_dead = True


class Bullet(pygame.sprite.Sprite):
	def __init__(self, location, heading, *groups):
		super(Bullet, self).__init__(*groups)
		self.image = pygame.image.load('bullet.png')
		self.rect = pygame.rect.Rect(location, self.image.get_size())
		self.heading = heading
		self.lifespan = 1
		self.radius = 4

	def update(self, dt, game):
		last = self.rect.copy()

		#time out
		self.lifespan -= dt
		if self.lifespan < 0:
			self.kill()
			return

		#movement
		self.rect.x -= 12 * math.sin(math.radians(self.heading))
		self.rect.y -= 12 * math.cos(math.radians(self.heading))

		#semi-torroidal behavior
		if last.centerx < 0:
			self.rect.centerx = 639
		if last.centerx > 640:
			self.rect.centerx = 1
		if last.centery < 0:
			self.rect.centery = 479
		if last.centery > 480:
			self.rect.centery = 1

		#collision detection
		if pygame.sprite.spritecollide(self, game.asteroids, True, pygame.sprite.collide_circle):
			game.explosion.play()
			Asteroid(game.asteroids)
			game.sprites.add(game.asteroids)
			game.score += 1
			self.kill()

if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((640,480))
	Game().main(screen)