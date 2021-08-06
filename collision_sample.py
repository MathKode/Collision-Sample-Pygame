import pygame

class Cube:
    def __init__(self,x,y,widht,height):
        self.x = int(x)
        self.y = int(y)
        self.w = int(widht)
        self.h = int(height)
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
    def Move(self,move_ls):
        if self.rect.x + move_ls[0] >= 0 and self.rect.x + move_ls[0] + self.w <= 400:
            self.rect.x += move_ls[0]
        if self.rect.y + move_ls[1] >= 0 and self.rect.y + move_ls[1] + self.h <= 400:
            self.rect.y += move_ls[1]
    def Show(self,screen):
        pygame.draw.rect(screen,(255,255,255),self.rect)

def rect_to_rect(rect1,rect2):
    r1_top = rect1.rect.topleft
    r1_bot = rect1.rect.bottomright
    r2_top = rect2.rect.topleft
    r2_bot = rect2.rect.bottomright
    #print(r1_top,r1_bot,r2_top,r2_bot,end='\r')
    c1 = False; c2 = False
    if r1_top[0] >= r2_top[0] and r1_top[0] <= r2_bot[0] or r1_bot[0] >= r2_top[0] and r1_bot[0] <= r2_bot[0]:
        print('Touch in axe x',end='\r')
        c1 = True
    if r1_top[1] >= r2_top[1] and r1_top[1] <= r2_bot[1] or r1_bot[1] >= r2_top[1] and r1_bot[1] <= r2_bot[1]:
        print('Touch in axe y',end='\r')
        c2 =True
    if c1 or c2:
        if c1 and c2:
            print('Touch the cube',end='\r')
    else:
        print('--------------',end='\r')

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Collisions Sample")

clock = pygame.time.Clock()
FPS = 55

Player = Cube(0,0,30,30)
Enemi = Cube(175,175,50,50)
vitesse = 5

Game_loop = True
move_ls = [0,0]
while Game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_ls[0] = 1 * vitesse
            if event.key == pygame.K_LEFT:
                move_ls[0] = -1 * vitesse
            if event.key == pygame.K_UP:
                move_ls[1] = -1 * vitesse
            if event.key == pygame.K_DOWN:
                move_ls[1] = 1 * vitesse
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and move_ls[0] == 1 * vitesse:
                move_ls[0] = 0
            if event.key == pygame.K_LEFT and move_ls[0] == -1 * vitesse :
                move_ls[0] = 0
            if event.key == pygame.K_UP and move_ls[1] == -1 * vitesse:
                move_ls[1] = 0
            if event.key == pygame.K_DOWN and move_ls[1] == 1 * vitesse:
                move_ls[1] = 0
    
    rect_to_rect(Player,Enemi)

    #Illustration :
    pygame.draw.rect(screen,(50,50,50),pygame.Rect(0,175,400,50))
    pygame.draw.rect(screen,(50,50,50),pygame.Rect(175,0,50,400))

    Player.Move(move_ls)
    Player.Show(screen)
    
    Enemi.Show(screen)
    pygame.display.flip()
    screen.fill((0,0,0))

    #fixer le nombre de fps
    clock.tick(FPS)

pygame.quit()
quit()