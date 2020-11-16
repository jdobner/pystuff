import pygame, sys, math

LEFT = 1
pos1x = 0
pos2x = 0
pos1y = 0
pos2y = 0

running = True
screen = pygame.display.set_mode((1200, 1000))


print(pygame.display.Info())
back_image = pygame.image.load("Monte_Alban.jpg")
screen.blit(back_image, [0,0])
while running:

 pygame.display.flip()
 event = pygame.event.poll()
 if event.type == pygame.QUIT:
     running = False
     pygame.quit()

 elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
     pos1x,pos1y = pygame.mouse.get_pos()
 elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
     pos2x,pos2y = pygame.mouse.get_pos()
     distx = abs(pos2x-pos1x)
     disty = abs(pos2y-pos1y)
     print ("Horizontal distane equals: %d" % distx)
     print ("Vertical distance equals: %d" % disty)