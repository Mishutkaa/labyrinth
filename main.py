from pygame import *
import pygame


mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()


money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')









pygame.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height):
        self.speed = 10
        
        super().__init__(player_image, player_x, player_y, player_width, player_height, self.speed)

    def move(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed



class Wall(sprite.Sprite):
    def __init__(self, color, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color = color
        self.width = wall_width
        self.height = wall_height
        # картинка стіни - прямокутник потрібних розмірів та кольору
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        # кожен спрайт повинен зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
 
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

w1 = Wall('yellow', 100, 100, 10, 450)
w2 = Wall('yellow', 240, 100, 350, 10)
w3 = Wall('yellow', 100, 100, 380, 10)
w4 = Wall('yellow', 580, 100, 10, 300)
w5 = Wall('yellow', 480, 200, 10, 380)
w6 = Wall('yellow', 380, 100, 10, 300)


class Cyborg(GameSprite):
    def __init__(self, player_image, start_x, end_x, player_y, player_width, player_height):
        super().__init__(player_image, start_x, player_y, player_width, player_height, 2)

        self.start_x = start_x
        self.end_x = end_x
    
    def move(self):
        if self.rect.x < self.start_x or self.rect.x > self.end_x:
            self.speed *= -1
        self.rect.x += self.speed


    def colliderect(self, rect):
        return self.rect.colliderect(rect)



        

window = display.set_mode((700, 500))
display.set_caption("Доганялки")
background = transform.scale(image.load("background.jpg"), (700, 500))



hero = Player('hero.png', 0, 470, 65, 65)
oluh = Cyborg("cyborg.png", 80,  350, 300, 65, 65)
skarb = GameSprite("Treasure.png", 200, 200, 65, 65, 0)
#ігровий цикл
run = True
finish = False
clock = time.Clock()

FPS = 60



font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

while run:

    if finish == False:
        window.blit(background,(0, 0))
        hero.reset()
        oluh.reset()
        oluh.move()
        hero.move()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        skarb.reset()
        if hero.rect.colliderect(oluh.rect) or hero.rect.colliderect(w1.rect) or hero.rect.colliderect(w2.rect) or hero.rect.colliderect(w3.rect) or hero.rect.colliderect(w4.rect) or hero.rect.colliderect(w5.rect) or hero.rect.colliderect(w6.rect):
            kick.play()
            finish = True
            window.blit(lose, (200, 200))
        if hero.rect.colliderect(skarb.rect):
            money.play()
            finish = True
            window.blit(win, (200, 200))



    for e in event.get():
        if e.type == QUIT:
            run = False





    display.update()
    clock.tick(FPS)