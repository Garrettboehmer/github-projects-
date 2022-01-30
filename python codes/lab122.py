#Garrett Boehmer
#lab12
#pygame knight vs dragon and her brood

import pygame
import random
WIDTH, HEIGHT = 900, 550
STAGE = pygame.display.set_mode((WIDTH,HEIGHT))
CLOCK = pygame.time.Clock()
FPS = 60
#starting positions
STARTX = 25
STARTY = HEIGHT/2
DRAGON_STARTX = WIDTH - 25
DRAGON_STARTY = (HEIGHT/2)-25
#speeds
PLAYER_SPEED = 5
ENEMY_SPEED = 1
SPEAR_SPEED = 8
#loading in images and scaling them
#https://p1.pxfuel.com/preview/874/479/641/abstract-art-artificial-artistic.jpg
BG = pygame.image.load('background.jpg')
#https://cdn.pixabay.com/photo/2013/07/13/10/18/knight-156972_1280.png
KNIGHT = pygame.image.load('knight.png')
KNIGHT = pygame.transform.scale(KNIGHT, (45, 45))
#https://freesvg.org/img/DragonColour.png
DRAGON = pygame.image.load('dragon.png')
DRAGON = pygame.transform.scale(DRAGON, (400, 400))
#https://freesvg.org/1541708847
DRAGON_SPAWN = pygame.image.load('dragon spawn.png')
DRAGON_SPAWN = pygame.transform.scale(DRAGON_SPAWN, (32, 32))
#https://upload.wikimedia.org/wikipedia/commons/d/de/Coat_of_arms_of_the_medieval_commune_of_Terni_%28in_first_half_of_13th_century%29.png
#SHIELD = pygame.image.load('shield.png')
#SHIELD = pygame.transform.scale(SHIELD, (32, 32))
#https://freesvg.org/img/D4v1d_two-edged_sword.png
#SWORD = pygame.image.load('sword.png')
#SWORD = pygame.transform.scale(SWORD, (32, 32))
#i uhhh made it.. i know its hard to believe!
#ATTACK = pygame.image.load('ATTACK.png')
#ATTACK = pygame.transform.scale(ATTACK, (50, 50))
COOLDOWN1 = pygame.image.load('cooldown1.png')
COOLDOWN1 = pygame.transform.scale(COOLDOWN1, (50, 50))
COOLDOWN2 = pygame.image.load('cooldown2.png')
COOLDOWN2 = pygame.transform.scale(COOLDOWN2, (50, 50))
COOLDOWN3 = pygame.image.load('cooldown3.png')
COOLDOWN3 = pygame.transform.scale(COOLDOWN3, (50, 50))
#https://freesvg.org/img/Spear.png
SPEAR = pygame.image.load('spear.png')
SPEAR = pygame.transform.scale(SPEAR, (50, 50))
SPEAR_THROWN = pygame.image.load('spear.png')
SPEAR_THROWN = pygame.transform.scale(SPEAR_THROWN, (50, 50))
#i made these also
#SPEAR_AMMO = pygame.image.load('spear ammo.png')
#SPEAR_AMMO = pygame.transform.scale(SPEAR_AMMO, (200, 200))
BARRIER = pygame.image.load('barrier.png')
BARRIER = pygame.transform.scale(BARRIER, (50, HEIGHT))
#https://freesvg.org/fireball-arvin61r58
FIREBALL = pygame.image.load('fireball.png')
FIREBALL = pygame.transform.scale(FIREBALL, (75, 75))
TITLE = pygame.image.load('title.png')
TITLE = pygame.transform.scale(TITLE, (600, 450))



def boss_hit(BIG_BOSS):
    rany = random.randint(0,200)
    return DRAGON_SPAWN.get_rect(center=(BIG_BOSS.x, BIG_BOSS.y+rany))

def spear_maker():
    ranx_spear  = random.randint(10,WIDTH/2)
    rany_spear = random.randint(0, 500)
    return SPEAR.get_rect(center=(ranx_spear,rany_spear))

def main():
    pygame.init()
    spear_count = 0
    enemies = []
    spear_list = []
    pygame.display.set_caption('Knights Vengence')
    player = KNIGHT.get_rect(center=(STARTX,STARTY))
    BIG_BOSS = DRAGON.get_rect(center=(DRAGON_STARTX,DRAGON_STARTY))
    barrier = BARRIER.get_rect(center=(WIDTH/2,0))
    #spawn = DRAGON_SPAWN.get_rect()
    #spear_thrown = SPEAR.get_rect(center=(player.x,player.y))
    boss_health = 100
    BOSS_HEALTH = pygame.image.load('boss health.png')
    BOSS_HEALTH = pygame.transform.scale(BOSS_HEALTH, (300, 50))
    thrown_spear = []
    #player = KNIGHT.get_rect(center=(player.x+5,player.y+10))
    keep_playing = True
    spawn_count = 0
    #health marks for boolean
    count_90 = 0
    count_80 = 0
    count_70 = 0
    count_60 = 0
    count_50 = 0
    count_40 = 0
    count_30 = 0
    count_20 = 0
    count_10 = 0
    spear_have = False
    spear_cooldown = 0
    fireball_list = []
    title = True
    
    while title: #title screen where directions should be


        #myfont = pygame.font.SysFont('couriernew', 30, bold = True)
        #game_text = myfont.render('Welcome to knight vs dragon!', True, (255,0,0))

        keys_pressed = pygame.key.get_pressed()
        STAGE.blit(BG, (0,0))
        #STAGE.blit(game_text, ((WIDTH/2)-game_text.get_width()/2, (HEIGHT/2)-game_text.get_height()/2))
        STAGE.blit(TITLE, (WIDTH/2-290, HEIGHT/2-200))
        if keys_pressed[pygame.K_SPACE]:
            title = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                title=keep_playing = False
        pygame.display.update()



    while keep_playing:  #Main loop
        STAGE.blit(BG, (0,0))
        STAGE.blit(BARRIER,(WIDTH/2 ,0))
        STAGE.blit(BOSS_HEALTH,(WIDTH-250,400))
        CLOCK.tick(FPS)
        keys_pressed = pygame.key.get_pressed()
        #grabs a random number to see if a fireball will be thrown
        #catch the time each loop
        big_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_playing = False
        
        #boss health bar depleting and spawning of the dragonlings
        #test_damage = 10
        #if big_time % 10 == 0:
            #boss_health -= test_damage
        if boss_health == 90 and count_90 == 0:
            count_90 += 1
            BOSS_HEALTH = pygame.transform.scale(BOSS_HEALTH, (250, 50))
            while spawn_count != 5:
                spawn_count += 1
                new_spawn = boss_hit(BIG_BOSS)
                STAGE.blit(DRAGON_SPAWN,(new_spawn.x,new_spawn.y))
                enemies.append(new_spawn)
            spawn_count = 0
        if boss_health == 80 and count_80 == 0:
            BOSS_HEALTH = pygame.transform.scale(BOSS_HEALTH, (200, 50))
            count_80 += 1
            while spawn_count != 5:
                spawn_count += 1
                new_spawn = boss_hit(BIG_BOSS)
                STAGE.blit(DRAGON_SPAWN,(new_spawn.x,new_spawn.y))
                enemies.append(new_spawn)
            spawn_count = 0
        if boss_health == 70 and count_70 == 0:
            BOSS_HEALTH = pygame.transform.scale(BOSS_HEALTH, (150, 50))
            count_70 += 1
            while spawn_count != 5:
                spawn_count += 1
                new_spawn = boss_hit(BIG_BOSS)
                STAGE.blit(DRAGON_SPAWN,(new_spawn.x,new_spawn.y))
                enemies.append(new_spawn)
            spawn_count = 0
        if boss_health == 60 and count_60 == 0:
            count_60 += 1
            BOSS_HEALTH = pygame.transform.scale(BOSS_HEALTH, (100, 50))
            while spawn_count != 5:
                spawn_count += 1
                new_spawn = boss_hit(BIG_BOSS)
                STAGE.blit(DRAGON_SPAWN,(new_spawn.x,new_spawn.y))
                enemies.append(new_spawn)
            spawn_count = 0
        if boss_health == 50 and count_50 == 0:
            BOSS_HEALTH = pygame.transform.scale(BOSS_HEALTH, (50, 50))
            count_50 += 1
            while spawn_count != 5:
                spawn_count += 1
                new_spawn = boss_hit(BIG_BOSS)
                STAGE.blit(DRAGON_SPAWN,(new_spawn.x,new_spawn.y))
                enemies.append(new_spawn)
            spawn_count = 0
        if boss_health == 40 and count_40 == 0:
            BOSS_HEALTH = pygame.transform.scale(BOSS_HEALTH, (40, 50))
            count_40 += 1
            while spawn_count != 5:
                spawn_count += 1
                new_spawn = boss_hit(BIG_BOSS)
                STAGE.blit(DRAGON_SPAWN,(new_spawn.x,new_spawn.y))
                enemies.append(new_spawn)
            spawn_count = 0
        if boss_health == 30 and count_30 == 0:
            BOSS_HEALTH = pygame.transform.scale(BOSS_HEALTH, (30, 50))
            count_30 += 1
            while spawn_count != 5:
                spawn_count += 1
                new_spawn = boss_hit(BIG_BOSS)
                STAGE.blit(DRAGON_SPAWN,(new_spawn.x,new_spawn.y))
                enemies.append(new_spawn)
            spawn_count = 0
        if boss_health == 20 and count_20 == 0:
            BOSS_HEALTH = pygame.transform.scale(BOSS_HEALTH, (20, 50))
            count_20 += 1
            while spawn_count != 5:
                spawn_count += 1
                new_spawn = boss_hit(BIG_BOSS)
                STAGE.blit(DRAGON_SPAWN,(new_spawn.x,new_spawn.y))
                enemies.append(new_spawn)
            spawn_count = 0
        if boss_health == 10 and count_10 == 0:
            BOSS_HEALTH = pygame.transform.scale(BOSS_HEALTH, (10, 50))
            count_10 += 1
            while spawn_count != 5:
                spawn_count += 1
                new_spawn = boss_hit(BIG_BOSS)
                STAGE.blit(DRAGON_SPAWN,(new_spawn.x,new_spawn.y))
                enemies.append(new_spawn)
            spawn_count = 0
        if boss_health ==0:
            myfont = pygame.font.SysFont('couriernew', 45, bold = True)
            game_text = myfont.render(' WINNER!!! ', True, (255,0,0))
            STAGE.blit(game_text, ((WIDTH/2)-game_text.get_width()/2, (HEIGHT/2)-game_text.get_height()/2))
            pygame.display.update()
            keep_playing =False
            pygame.time.delay(5000)
        #Enemies follow player ENEMIES MOVEMENT IS HERE!!!!!!!!!!!!!
        #GOOD LORD THIS TOOK LONGER THAN IT SHOULD OF BURN IT WITH FIRE!!
        for i in enemies:
            if i.x > player.x and i.y < player.y:
                i.x -= ENEMY_SPEED
                i.y += ENEMY_SPEED
            if i.x > player.x and i.y > player.y:
                i.x -= ENEMY_SPEED
                i.y -= ENEMY_SPEED
            if i.x < player.x and i.y < player.y:
                i.x += ENEMY_SPEED
                i.y += ENEMY_SPEED
            if i.x < player.x and i.y > player.y:
                i.x += ENEMY_SPEED
                i.y -= ENEMY_SPEED
            if i.x == player.x and i.y > player.y:
                i.y -= ENEMY_SPEED
            if i.x == player.x and i.y < player.y:
                i.y += ENEMY_SPEED
            if i.x > player.x and i.y == player.y:
                i.x -= ENEMY_SPEED
            if i.x < player.x and i.y == player.y:
                i.x += ENEMY_SPEED

        #fireball should be aimed at the player
        if (pygame.time.get_ticks() %100) == 0 and len(fireball_list)<3:
            fire_ball = FIREBALL.get_rect(center=(WIDTH-50, HEIGHT/2))
            fireball_list.append(fire_ball)
            print(fireball_list)
        

        for i in fireball_list:
            STAGE.blit(FIREBALL,(i.x,i.y))
            if i.x > 0:
                i.x -=ENEMY_SPEED
            else:
                fireball_list.remove(i)

        for i in fireball_list:
            if i.colliderect(player):
                myfont = pygame.font.SysFont('couriernew', 45, bold = True)
                game_text = myfont.render(' BURNED UP ', True, (255,0,0))
                STAGE.blit(game_text, ((WIDTH/2)-game_text.get_width()/2, (HEIGHT/2)-game_text.get_height()/2))
                pygame.display.update()
                keep_playing =False
                pygame.time.delay(5000)
       
        #spear ammo
        #if spear_count == 1:
            #SPEAR.blit(SPEAR_AMMO,(50,10))
        #spear spawning
        if ((pygame.time.get_ticks() %23) == 0) and len(spear_list) <= 2:
                new_spear = spear_maker()
                SPEAR.blit(SPEAR,(new_spear.x,new_spear.y))
                spear_list.append(new_spear)

        #list of spear on ground
        for i in spear_list:
            if i.colliderect(player) and spear_count != 3:
                spear_list.remove(i)
                spear_have = True
                spear_count += 1
        #small enemies spawning
        if ((pygame.time.get_ticks() %120) == 0):
            if len(enemies) <=2:
                new_spawn = DRAGON_SPAWN.get_rect(center=(BIG_BOSS.x, BIG_BOSS.y))
                STAGE.blit(DRAGON_SPAWN,(new_spawn.x,new_spawn.y))
                enemies.append(new_spawn)

        #keys being pushed
        
        if keys_pressed[pygame.K_w]:
            player.y -= PLAYER_SPEED
        if keys_pressed[pygame.K_s]:
            player.y += PLAYER_SPEED
        if keys_pressed[pygame.K_d]:
            player.x += PLAYER_SPEED
        if keys_pressed[pygame.K_a]:
            player.x -= PLAYER_SPEED
        #throw the spear
        #making the attack/setting a cooldown/and making an animation for it... that looks like crap but i mean if i could animate well i wouldnt be doing this
        #borrowed the cooldown idea from this video https://www.youtube.com/watch?v=YOCt8nsQqEo
        spear_CD = (big_time - spear_cooldown)
        if spear_have and keys_pressed[pygame.K_r] and spear_CD > 500:
            spear_cooldown = pygame.time.get_ticks()
            spear_count -= 1
            spear_thrown = SPEAR_THROWN.get_rect(center=(player.x, player.y))
            if spear_count == 0:
                spear_have = False
            thrown_spear.append(spear_thrown)

        #spear thrown hits boss and does damage or spawn
        for i in thrown_spear:
            STAGE.blit(SPEAR_THROWN,(i.x, i.y))
            i.x += SPEAR_SPEED
            if i.colliderect(BIG_BOSS):
                thrown_spear.remove(i)
                boss_health -= 10
        
        #real_CD = (big_time - melee_cooldown)
        #if keys_pressed[pygame.K_SPACE] and real_CD > 2000:
            #melee_cooldown = pygame.time.get_ticks()
            #STAGE.blit(ATTACK,(player.x+40 ,player.y))
            #STAGE.blit(COOLDOWN1,(10,10))
        
        #collision of screen
        if player.y < 0:
            player.y = 0
        if player.y > HEIGHT:
            player.y = (HEIGHT - player.height)
        if player.x < 0:
            player.x = 0
        if player.x > WIDTH:
            player.x = (WIDTH - player.width)
        #collision of barrier
        if player.x > barrier.x:
            player.x = barrier.x

        #blits
        #set background image on stage
        STAGE.blit(KNIGHT,(player.x ,player.y))
        STAGE.blit(DRAGON,(BIG_BOSS.x ,BIG_BOSS.y))
        for i in spear_list:
            STAGE.blit(SPEAR,(i.x,i.y))
        #spawn the enemies and mak'em get hit by spears
        for x in enemies:
            STAGE.blit(DRAGON_SPAWN,(x.x,x.y))
            if x.colliderect(player):
                myfont = pygame.font.SysFont('couriernew', 45, bold = True)
                game_text = myfont.render(' Dragon Food! ', True, (255,0,0))
                STAGE.blit(game_text, ((WIDTH/2)-game_text.get_width()/2, (HEIGHT/2)-game_text.get_height()/2))
                pygame.display.update()
                keep_playing =False
                pygame.time.delay(5000)
            if len(thrown_spear)>=1:
                for i in thrown_spear:
                    if i.colliderect(x):
                        thrown_spear.remove(i)
                        enemies.remove(x)

        #ammo count and animation for such
        if spear_count == 1:
            if spear_CD >= 100:
                STAGE.blit(COOLDOWN2,(10,10))
            if spear_CD >=250:
                STAGE.blit(COOLDOWN3,(10,10))
            if spear_CD >= 500:
                STAGE.blit(COOLDOWN1,(10,10))
        if spear_count == 2:
            if spear_CD >= 100:
                STAGE.blit(COOLDOWN2,(10,10))
                STAGE.blit(COOLDOWN2,(100,10))
            if spear_CD >=250:
                STAGE.blit(COOLDOWN3,(10,10))
                STAGE.blit(COOLDOWN3,(100,10))
            if spear_CD >= 500:
                STAGE.blit(COOLDOWN1,(10,10))
                STAGE.blit(COOLDOWN1,(100,10))
        if spear_count == 3:
            if spear_CD >= 100:
                STAGE.blit(COOLDOWN2,(10,10))
                STAGE.blit(COOLDOWN2,(100,10))
                STAGE.blit(COOLDOWN2,(200,10))
            if spear_CD >=250:
                STAGE.blit(COOLDOWN3,(10,10))
                STAGE.blit(COOLDOWN3,(100,10))
                STAGE.blit(COOLDOWN3,(200,10))
            if spear_CD >= 500:
                STAGE.blit(COOLDOWN1,(10,10))
                STAGE.blit(COOLDOWN1,(100,10))
                STAGE.blit(COOLDOWN1,(200,10))
        
        pygame.display.update()
    pygame.quit()
main()