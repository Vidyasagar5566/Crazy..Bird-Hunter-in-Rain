import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("new_game")
score = 0

# back ground
back_ground = pygame.image.load("summer-landscape-countryside-with-river-forest-clouds.jpg")

# text
font = pygame.font.Font("freesansbold.ttf", 32)
tx, ty = 0, 0
def text(x, y):
    ll = font.render("score :" + str(score), True, (0, 0, 5))
    screen.blit(ll, (x, y))


# gun man
man = pygame.image.load("criminal-with-gun-covered-with-coat-and-hat.png")
blast = pygame.image.load("blast.png")
mx = 380
my = 500
def gun_man(x, y):
    screen.blit(blast, (x + 20, y + 50))
    screen.blit(man, (x, y))


# bullet
bullet_ = pygame.image.load("bullet.png")
by = 500
def bullet(x, y):
    screen.blit(bullet_, (x, y))

# drops
rock_ = pygame.image.load("water-drop.png")
def drops(x, y):
    screen.blit(rock_, (x, y))


# birds
birdy = random.randint(0, 30)
birdx = 800
bird_blast = 1000
bird_ = pygame.image.load("bird.png")
def bird(x, y):
    screen.blit(bird_, (x, y*10))

count, b_count ,count_UPD = 0, 0, 0
b_list = []
running = True
column_enemy_list = []
row_enemy_list = []
stop, bird_count = 0, 0
for i in range(6):
    a = random.randint(1, 12)
    b = 0
    row_enemy_list.append([a*64, b])
column_enemy_list.append(row_enemy_list)
while running:

    screen.fill((0,25 ,255))
    # back ground
    screen.blit(back_ground, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                count = -1
            if event.key == pygame.K_RIGHT:
                count = 1
            if event.key == pygame.K_UP:
                count_UPD = -1
            if event.key == pygame.K_DOWN:
                count_UPD = 1
            if event.key == pygame.K_SPACE:
                b_count = 1
                b_list.append([mx, my])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                count = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                count_UPD = 0
            if event.key == pygame.K_SPACE:
                b_count = 0

    # gun man display left-right
    mx += count
    if mx <= 0:
        mx = 0
    if mx >= 740:
        mx = 740

    # gun man display up down
    my += count_UPD
    if my >= 500:
        my = 500
    if my <= 0:
        my = 0
    gun_man(mx, my)


    # bullet display
    if b_count > 0:
        if b_list[-1][1] <= my-64:
            b_list.append([mx, my])

    i, a = 0, len(b_list)
    while i < a:
        bullet(b_list[i][0], b_list[i][1])
        b_list[i][1] -= 1.2

        # collision of bullet with bird
        if birdy*10 <= b_list[i][1] <= birdy*10 + 64:
            if birdx <= b_list[i][0] <= birdx + 64:
                bird_blast_x, bird_blast_y = b_list[i][0], b_list[i][1]
                bird_count, bird_blast = 0, 0
                birdx = 800
                score += 10


        if b_list[i][1] <= 0:
            b_list.pop(i)
            a -= 1
        i += 1


    # water drops display
    if column_enemy_list[-1][0][1] >= 150:
        row_enemy_list = []
        for i in range(6):
            a = random.randint(0, 11)
            b = 0
            row_enemy_list.append([a*64, b])
        column_enemy_list.append(row_enemy_list)

    i, a = 0, len(column_enemy_list)
    while i < a:
        for j in range(6):
            if stop == 1:
                drops(column_enemy_list[i][j-1][0], column_enemy_list[i][j-1][1])
                continue
            drops(column_enemy_list[i][j][0], column_enemy_list[i][j][1])
            column_enemy_list[i][j][1] += 0.5

            # collision of gun with water drops
            if column_enemy_list[i][j][1] <= my <= column_enemy_list[i][j][1]+55:
                if column_enemy_list[i][j][0]-5 <= mx <= column_enemy_list[i][j][0]+40:
                    stop = 1
        if column_enemy_list[i][0][1] >= 500:
            column_enemy_list.pop(i)
            bird_count += 1
            a -= 1
        i += 1

    # bird display
    if bird_count == 1:
        birdy = random.randint(0, 46)
    if bird_count >= 2:
        bird(birdx, birdy)
        birdx -= 0.5
        if birdx <= 0:
            bird_count = 0
            birdx = 800

    # score display
    if stop == 1:
        text(350, 80)
    else:
        text(tx, ty)

    # blast at bird collission
    if bird_blast <= 100:
        screen.blit(blast, (bird_blast_x, bird_blast_y))
    bird_blast+=1

    pygame.display.update()
