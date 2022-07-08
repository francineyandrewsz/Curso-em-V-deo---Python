#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.


print('=>'*20, 'DESAFIO 021', '<='*20)

#importar a biblioteca pygame
import pygame

#iniciar pygame
pygame.init()
pygame.mixer.music.load('Iron.mp3')
pygame.mixer.music.play()
pygame.event.wait()
