# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 18:07:50 2018

@author: Antonio
"""

import pygame, sys
from pygame.locals import *

Color = pygame.Color(250,250,250)
ancho = 600
alto = 500

class Proyectil  (pygame.sprite.Sprite):
    def _init_(self, posx, posy):
        self.imagenProyectil = pygame.image.load("proyectil.jpg")
        
        self.velocidad = 5
        
        self.rect = self.imagenProyectil.get_rect()
        self.rect.top = posx
        #self.rect.left = posy
    def trayectoria(self):
        self.rect.top = self.rect.left - self.velocidad
    def dibujar(self, superficie):
        superficie.blit(self.imagenProyectil,self.rect)
class Personajes (pygame.sprite.Sprite): 

    def _init_(self):
       # pygame.sprite.Sprite._init_(self)
        self.imagen = pygame.image.load("personaje.jpg")
        
        self.rect = self.imagen.get_rect()
        self.rect.centerx = 50
        self.rect.centery = 368
    
    def disparar (self ):
        #self.imagen = pygame.image.load()
        #self.imagen1 = pygame.image.load()
        #self.imagen2 = pygame.image.load()
        self.imagen3 = pygame.image.load("personaje1.jpg")
        
        self.rect = self.imagen.get_rect()
        self.rect.centerx = 50
        self.rect.centery = 368
        
        
    def dibujar(self, Surface):
        Surface.blit(self.imagen, self.rect) 
        
    def dibujar1(self, Surface):
        Surface.blit(self.imagen3, self.rect)
        
    def teclado():
        validar = False
        teclado = pygame.key.get_pressed()
        if  teclado[K_q]:
            validar = True
        return validar
class Correr ():

    def animacion():
       
        pygame.init()
        ventana = pygame.display.set_mode((ancho,alto))
        pygame.display.set_caption("Personaje")
        clock = pygame.time.Clock()
            
        animacion1 = Personajes()
        animacion1._init_()
        
        disparo = Proyectil()
        disparo._init_(50,368)
        
        
        while True:  
            time = clock.tick(60)
            disparo.trayectoria()
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()
            ventana.fill(Color)
            animacion1.dibujar(ventana)
            time()
            animacion1.disparar()
            animacion1.dibujar1(ventana)
            #if animacion1.teclado() == True:
            disparo.dibujar(ventana)
            pygame.display.update()
               
                
        
    animacion()
    