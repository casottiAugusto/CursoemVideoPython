'''
Faça um programa que abra e reproduza umm audui de arquivo mp3
'''
import pygame
pygame.init()
pygame.mixer.music.load('21.mp3' )
pygame.mixer.music.play()
input()
pygame.event.wait()