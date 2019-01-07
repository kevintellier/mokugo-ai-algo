import pygame
pygame.init()

size = width, height = 720,720
N = 8
BACKGROUND_IMAGE = "board_mokugo.jpg"
WHITE_IMAGE = "white_mokugo.png"
BLACK_IMAGE = "black_mokugo.png"
BLACK = 0,0,0
screen = pygame.display.set_mode(size)

class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(BACKGROUND_IMAGE)
        self.image = pygame.transform.scale(self.image, (300,300))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = 0,0

BackGround = Background()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		screen.blit(BackGround.image, BackGround.rect)
		pygame.display.flip()