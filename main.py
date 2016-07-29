# -*- coding: utf-8 -*-

from pygame import image
from pygame.locals import *

from scripts import inputbox  #import the inputbox to change round number
from scripts.classes import * #import the game classes from script


#first, declaration of dimensions and colors

dimensions = [800,501]
WINDOWWIDTH = 800
WINDOWHEIGHT = 501
#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
YELLOW    = (255, 255,  51)
BGCOLOR=DARKGREEN

img_dir = path.join(path.dirname(__file__), 'images')
sound_folder = path.join(path.dirname(__file__), 'sounds')

def main():
    #Main screen before the actual game starts
    
    global FPSCLOCK, DISPLAYSURF, BASICFONT, PAUSEFONT, SMALLFONT, MINIFONT

    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode(dimensions)
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    SMALLFONT= pygame.font.Font('freesansbold.ttf', 14)
    MINIFONT= pygame.font.Font('freesansbold.ttf', 9)
    PAUSEFONT = pygame.font.SysFont("comicsansms",115)
    score=0
    total_score=0
    pygame.display.set_caption('VAN PIDGY, the vampire slayer')
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.mixer.music.load(path.join(sound_folder, "start.ogg"))
    pygame.mixer.music.play()
    showStartScreen()
    while True:
        pygame.mixer.music.stop()
        runGame()
        showGameOverScreen(score, total_score, round_number=1)

    
def terminate():
    #For killing the game
    pygame.quit()
    sys.exit()

def runGame(number_of_vampires=5, vampire_velocity=1, velocity=3, total_score=0, round_number=1,remaining_shits=0):
    #Velocity is actually the velocity of the pidgeon
    #The other variables explain themselves
    
    vampire_list= pygame.sprite.Group()
    all_sprite_list=pygame.sprite.Group()
    shit_list=pygame.sprite.Group()
    ufo_list=pygame.sprite.Group()
    pidgeon_list=pygame.sprite.Group()
    soul_list=pygame.sprite.Group()
    bullet_list=pygame.sprite.Group()
    drone_list=pygame.sprite.Group()
    
    #Shit counter and score
    number_of_shits=15+remaining_shits
    score=0
    
    
#Declaration of images and other sounds-------------------------------------------
    bg_forest=pygame.image.load(path.join(img_dir, "forest.jpg")).convert()
    tension=pygame.image.load(path.join(img_dir,"tension.png")).convert()
    bg_city=pygame.image.load(path.join(img_dir, "city.png")).convert()
    tram_tension=pygame.image.load(path.join(img_dir, "tram_tension.png")).convert()
    forest_frame=pygame.image.load(path.join(img_dir, "forest_frame.png")).convert()
    city_frame=pygame.image.load(path.join(img_dir, "city_frame.png")).convert()
    bg_ship=pygame.image.load(path.join(img_dir, "inside_ship.png")).convert()
    ship_frame=pygame.image.load(path.join(img_dir, "ship_frame.png")).convert()
    ship_tension=pygame.image.load(path.join(img_dir, "ship_tension.png")).convert()
    bg_alien_planet=pygame.image.load(path.join(img_dir, "alien_planet.png")).convert()
    planet_tension=pygame.image.load(path.join(img_dir, "planet_tension.png")).convert()
    alien_frame=pygame.image.load(path.join(img_dir, "alien_frame.png")).convert()
    wind_direction_left = pygame.image.load(path.join(img_dir, "wind_direction_left.png")).convert()
    wind_direction_right = pygame.image.load(path.join(img_dir, "wind_direction_right.png")).convert()
    wind_direction_left.set_colorkey((255, 255, 255))
    wind_direction_right.set_colorkey((255, 255, 255))
    bg_ship.set_colorkey((255, 255, 255))
    ship_frame.set_colorkey((255, 255, 255))
    tension.set_colorkey((255, 255, 255))
    tram_tension.set_colorkey((255, 255, 255))
    forest_frame.set_colorkey((255, 255, 255))
    city_frame.set_colorkey((255, 255, 255))
    ship_tension.set_colorkey((255, 255, 255))
    bg_alien_planet.set_colorkey((255, 255, 255))
    planet_tension.set_colorkey((255, 255, 255))
    alien_frame.set_colorkey((255, 255, 255))

    map_images_list=[]
    map_list= [
        'forest_map1.png',
        'forest_map2.png',
        'forest_map3.png',
        'forest_map4.png',
        'forest_map5.png',
        'forest_map6.png',
        'forest_map7.png',
        'forest_map8.png',
        'forest_map9.png',
        'forest_map10.png'

    ]
    for image in map_list:
        map_images_list.append(pygame.image.load(path.join(img_dir, image)).convert())


    pidgeon_shot_sound=pygame.mixer.Sound(path.join(sound_folder, "pidgeon_shot.ogg"))
    vampire_dies=pygame.mixer.Sound(path.join(sound_folder, "vampire_dies.ogg"))
    electrocute=pygame.mixer.Sound(path.join(sound_folder, "electrocute.ogg"))
    wind_sound=pygame.mixer.Sound(path.join(sound_folder, "wind_sound.ogg"))
    no_shit_fart=pygame.mixer.Sound(path.join(sound_folder, "no_shit_fart.ogg"))
    pidgeon_bump= pygame.mixer.Sound(path.join(sound_folder, "pidgeon_bump.ogg"))
    pause_sound=pygame.mixer.Sound(path.join(sound_folder, "pause_sound.ogg"))
    ufo_sound=pygame.mixer.Sound(path.join(sound_folder, "ufo_sound.ogg"))
    metalic_bump=pygame.mixer.Sound(path.join(sound_folder, "metalic_bump.ogg"))
    death_shot=pygame.mixer.Sound(path.join(sound_folder, "death_shot.ogg"))
    shot=pygame.mixer.Sound(path.join(sound_folder, "shot.ogg"))
    drone_sound=pygame.mixer.Sound(path.join(sound_folder, "drone.ogg"))
    #------------------------------------------------------------------------
    
    if round_number==1:
        while True:
            DISPLAYSURF.blit(map_images_list[round_number - 1], [0, 0])
            drawPressKeyMsg()
            pygame.display.flip()
            if checkForKeyPress():
                break

   
    
    
#Creation of the protagonist(pidgeon) and its atributtes
    pidgeon=Pidgeon()
    all_sprite_list.add(pidgeon)
    pidgeon_list.add(pidgeon)
    
    pidgeon.rect.x = 300
    pidgeon.rect.y = 150
    
    direction_x=0
    direction_y=0
    
    wind_direction=random.choice(["right", "left"])#Randomizing wind direction
    
    
#Generation of the vampires----------------------------------------


    for i in range(number_of_vampires):
        if round_number>20 and i%2==0:
            vampire_gun=Vampire_gun(random.choice([1,-1]))
            vampire_gun.rect.x=random.randint(40, 750)
            vampire_gun.rect.y=430
            vampire_list.add(vampire_gun)
            all_sprite_list.add(vampire_gun)    
        else:
            vampire=Vampire(random.choice([1,-1]))
            vampire.rect.x=random.randint(40, 750)
            vampire.rect.y=430
            vampire_list.add(vampire)
            all_sprite_list.add(vampire)

    #------------------------------------------------------------------
        
    #Music of the game    
    pygame.mixer.music.load(path.join(sound_folder, "main_game.ogg"))
    pygame.mixer.music.play(loops=100)

    while True:
    #Main event loop

        #Which background and pidgeon is declared
        if round_number <= 10:  
            DISPLAYSURF.blit(bg_forest,[0,0])
            DISPLAYSURF.blit(tension,[0, 400])
            DISPLAYSURF.blit(forest_frame,[0,0])
        elif 11 <= round_number <= 20:
            DISPLAYSURF.blit(bg_city,[0,0])
            DISPLAYSURF.blit(tram_tension,[0, 400])
            DISPLAYSURF.blit(city_frame,[0,0])
        elif 21 <= round_number <= 30:
            DISPLAYSURF.blit(bg_ship,[0,0])
            DISPLAYSURF.blit(ship_tension,[0, 400])
            DISPLAYSURF.blit(ship_frame,[0,0])
        else:
            DISPLAYSURF.blit(bg_alien_planet,[0,0])
            DISPLAYSURF.blit(planet_tension,[0, 400])
            DISPLAYSURF.blit(alien_frame,[0,0])

        pidgeon.rect.x=pidgeon.rect.x + direction_x
        pidgeon.rect.y=pidgeon.rect.y + direction_y

#Pidgeon movement block and shit collisions           
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    if 5<=round_number<10 or 15<=round_number<=20 or 36<=round_number<=40:
                        if wind_direction=="left":
                            direction_x = -velocity*2
                            direction_y=0
                        elif wind_direction=="right":
                            direction_x = -velocity/2
                            direction_y=0
                    else:
                        direction_x = -velocity
                        direction_y=0 
                elif event.key == K_RIGHT:
                    if 5 <= round_number < 10 or 15 <= round_number <= 20 or 36<=round_number<=40:
                        if wind_direction == "left":
                            direction_x = +velocity/2
                            direction_y = 0
                        elif wind_direction == "right":
                            direction_x = +velocity*2
                            direction_y=0
                    else:
                        direction_x = +velocity
                        direction_y=0      
                elif event.key == K_UP:
                    direction_y = -velocity
                    direction_x=0
                elif event.key == K_DOWN:
                    direction_y = +velocity
                    direction_x=0
                elif event.key == K_RETURN:
                    #Allow to change level
                    go_to= int(inputbox.ask(DISPLAYSURF, 'Level'))
                    if 0< go_to < 11:
                        runGame(go_to*5, go_to*0.3, go_to*0.5, total_score, go_to, go_to*2)
                    elif 11<= go_to < 25:
                        runGame(go_to*4, go_to*0.15, go_to*0.3, total_score, go_to, go_to*2)
                    elif 25<= go_to:
                        runGame(go_to*3, go_to*0.1, go_to*0.2, total_score, go_to, go_to*2)
                    else:
                        continue   
                if event.key == K_SPACE and len(shit_list)==0 and number_of_shits>-1:
                    #Taking a shit
                    if pidgeon.rect.x == 300 and pidgeon.rect.y == 150:
                        drawMoveToShot()
                        pygame.display.flip()
                        pygame.time.wait(2000)
                    else:
                        if number_of_shits>0:
                            pidgeon_shot_sound.play()
                        number_of_shits -= 1
                        if 5<= round_number < 10 or 15<=round_number<=20 or 36<=round_number<=40:
                            if wind_direction=="left":
                                shit=Shit(-3)
                            elif wind_direction == "right":
                                shit=Shit(3)
                        else:
                            shit=Shit(0)
                        shit.rect.x=pidgeon.rect.x +50
                        shit.rect.y=pidgeon.rect.y +50
                        all_sprite_list.add(shit)
                        shit_list.add(shit)
                        
                elif event.key==K_p:
                    #Pausing of the game
                    pause_sound.play()
                    while True:
                        pygame.mixer.music.pause()
                        event=pygame.event.wait()
                        drawPauseInPause()
                        pygame.display.update()
                        FPSCLOCK.tick(60)
                        if event.type==pygame.KEYDOWN and event.key==pygame.K_p:
                            pygame.mixer.music.unpause()                
                            break
                        if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                            terminate()
                elif event.key == K_ESCAPE:
                    #terminating the game
                    terminate()
                    
        for shit in shit_list:
            shitted_vampires=pygame.sprite.spritecollide(shit, vampire_list, True)
            for vampire in shitted_vampires:
                if vampire.get_points()==50:
                    soul=Soul()
                    soul.rect.x=vampire.rect.x
                    soul.rect.y=vampire.rect.y
                    all_sprite_list.add(soul)
                    soul_list.add(soul)
                elif vampire.get_points()==150:
                    soul_gun=Soul_gun()
                    soul_gun.rect.x=vampire.rect.x
                    soul_gun.rect.y=vampire.rect.y
                    all_sprite_list.add(soul_gun)
                    soul_list.add(soul_gun)
                vampire_dies.play()
                shit_list.remove(shit)
                all_sprite_list.remove(shit)
                score += vampire.get_points()
                
            if shit.rect.y > 500:
                shit_list.remove(shit)
                all_sprite_list.remove(shit)
        for soul in soul_list:
            if soul.rect.y < 380:
                all_sprite_list.remove(soul)
                soul_list.remove(soul)
           
                
#--------------------------------------------------------------------------                
                    
#Vampires movement and shot block
                   
        for moving_vampire in vampire_list:
            moving_vampire.rect.x = moving_vampire.rect.x + vampire_velocity*moving_vampire.vampire_direction
            if moving_vampire.rect.x > 750:
                moving_vampire.vampire_direction = -1
            elif moving_vampire.rect.x < 40:
                moving_vampire.vampire_direction = 1
                
        
        for shoting_vampire in vampire_list:
            if shoting_vampire.get_points()==150:
                if shoting_vampire.get_shoting_number()==random.randint(1,2000):
                    shot.play()
                    bullet=Bullet()
                    bullet.rect.x=shoting_vampire.rect.x
                    bullet.rect.y=shoting_vampire.rect.y
                    all_sprite_list.add(bullet)
                    bullet_list.add(bullet)
               
        for bullet in bullet_list:
            targeted_shot=pygame.sprite.spritecollide(pidgeon, bullet_list, True,pygame.sprite.collide_rect_ratio(0.5))
            if targeted_shot:
                pidgeon.bumpHead()
                death_shot.play()
                pygame.mixer.music.stop()
                all_sprite_list.remove(bullet)
                bullet_list.remove(bullet)
                pygame.time.delay(2000)
                showGameOverScreen(score, total_score,round_number)
            elif bullet.rect.y<0:
                all_sprite_list.remove(bullet)
                bullet_list.remove(bullet)
        
                 
       
                
#--------------------------------------------------------------------------
                
#wind block         
        windBlock(round_number, wind_direction, wind_sound, all_sprite_list, wind_direction_left, wind_direction_right)
        
#ufo block
        ufo_direction=random.choice(["right", "left"])#Randomizing ufo direction
        ufoBlock(round_number, ufo_direction, ufo_sound, all_sprite_list,ufo_list)
        for ufo in ufo_list:
                        
                    if ufo.rect.collidepoint(pidgeon.rect.x+53, pidgeon.rect.y+26):
                        pidgeon.bumpHead()
                        metalic_bump.play()
                        pygame.mixer.music.stop()
                        ufo.kill()
                        pygame.time.delay(2000)
                        showGameOverScreen(score, total_score,round_number) 
                              
                    elif ufo.rect.x < -230 and ufo_direction=="left":
                        ufo.kill()
                    elif ufo.rect.x > 850 and ufo_direction=="right":
                        ufo.kill()
#drone block
        drone_direction=random.choice(["right", "left"])#Randomizing ufo direction
        droneBlock(round_number, drone_direction, drone_sound, all_sprite_list,drone_list)
        for drone in drone_list:
                        
                if drone.rect.collidepoint(pidgeon.rect.x+53, pidgeon.rect.y+26):
                    pidgeon.bumpHead()
                    metalic_bump.play()
                    pygame.mixer.music.stop()
                    drone.kill()
                    pygame.time.delay(2000)
                    showGameOverScreen(score, total_score, round_number)
                              
                elif drone.rect.x < -230 and drone_direction=="left":
                        drone.kill()
                elif drone.rect.x > 850 and drone_direction=="right":
                        drone.kill()              
                            
#----------------------------------------------------------------------------

#Game Over/Win block 
          
        if pidgeon.rect.y >= 360:
            #change the pidgeon image to electrocuted
            pidgeon.electrocute()
            
        elif pidgeon.rect.y ==0:
            #change the pidgeon image to bumped in the head
            pidgeon.bumpHead()
        elif pidgeon.rect.x ==-15:
            #change the pidgeon image to bumped in the left
            pidgeon.bumpLeft()
            
        elif pidgeon.rect.x ==699:
            #change the pidgeon image to bumped in the right
            pidgeon.bumpRight()
            
        elif pidgeon.rect.y >360:
            round_number=1
            pygame.mixer.music.stop()
            electrocute.play()
            pygame.time.delay(2000)
            showGameOverScreen(score, total_score,round_number)
      
        elif pidgeon.rect.y <0 or pidgeon.rect.x <-15 or pidgeon.rect.x > 700:
            round_number=1
            pygame.mixer.music.stop()
            pidgeon_bump.play()
            pygame.time.delay(2000)
            showGameOverScreen(score, total_score,round_number)

             
        elif number_of_shits<0 and len(vampire_list)>0:
            pygame.mixer.music.stop()
            no_shit_fart.play()
            pygame.time.wait(2000)
            showGameOverScreen(score, total_score,round_number)
            round_number=1
        if number_of_shits >= 0 and len(vampire_list)<=0:
            round_number +=1
            total_score += score
            remaining_shits=number_of_shits
            if 0< round_number < 11:
                number_of_vampires = number_of_vampires+7
                vampire_velocity += 0.3
                velocity += 0.5          
            elif 11< round_number < 25:
                number_of_vampires = number_of_vampires+5
                vampire_velocity += 0.15
                velocity += 0.3         
            elif 25< round_number:
                number_of_vampires = number_of_vampires+3
                vampire_velocity += 0.1
                velocity += 0.2         

            showWinScreen(score, total_score)
            while True:
                if checkForKeyPress():
                    pygame.event.get()  # clear event queue
                    DISPLAYSURF.blit(map_images_list[round_number - 1], [0, 0])
                    drawPressKeyMsg()
                    pygame.display.flip()
                    while True:
                        if checkForKeyPress():
                            pygame.event.get()
                            runGame(number_of_vampires, vampire_velocity, velocity, total_score, round_number,remaining_shits)
                    
#----------------------------------------------------------------------------                    

#---------------------------------------------------------------------------
#All the draw methods and the flip 

        all_sprite_list.update() 
        drawAmountShit(number_of_shits, round_number)
        drawScore(score,round_number)
        drawPauseMainGame()
        
        drawRound(round_number)
        drawTotalScore(total_score,round_number)    
        all_sprite_list.draw(DISPLAYSURF)
        FPSCLOCK.tick(60)
        pygame.display.flip()
        
#--------------------------------------------------------------------------




#Wind movement block method  
def windBlock(round_number, wind_direction, wind_sound, all_sprite_list,wind_direction_left,wind_direction_right):
    if 5<= round_number < 10 or 15<=round_number<=20 or 36<=round_number<=40:
            drawCautionWind()
            if wind_direction=="left":
                DISPLAYSURF.blit(wind_direction_left, [0,0])
                random_wind=random.randint(1, 100)
                if random_wind==50:
                    wind_sound.play()
                    wind=Wind(-5)
                    wind.rect.x=700
                    wind.rect.y=random.randint(0,100)
                    all_sprite_list.add(wind)               
            elif wind_direction == "right":
                DISPLAYSURF.blit(wind_direction_right, [0,0])
                random_wind=random.randint(1,100)
                if random_wind==50:
                    wind_sound.play()
                    wind=Wind(5)
                    wind.change_direction()
                    wind.rect.x=-200
                    wind.rect.y=random.randint(0,100)-60
                    all_sprite_list.add(wind)

#UFO movement block
def ufoBlock(round_number, ufo_direction, ufo_sound, all_sprite_list, ufo_list):
    if 10<= round_number < 21:
            drawDangerUFO()
            
            if ufo_direction=="left" and len(ufo_list)<1:
                random_ufo=random.randint(1, 50)
                if random_ufo==15:
                    ufo_sound.play()
                    ufo=UFO(random.choice([-3, -4, -5, -6, -7]))
                    ufo.rect.x=700
                    ufo.rect.y=random.randint(50,300)
                    all_sprite_list.add(ufo)
                    ufo_list.add(ufo)
            
            elif ufo_direction == "right"and len(ufo_list)<1:
                random_ufo=random.randint(1,50)
                if random_ufo==15:
                    ufo_sound.play()
                    ufo=UFO(random.choice([3, 4, 5, 6, 7]))
                    ufo.change_direction()
                    ufo.rect.x=-200
                    ufo.rect.y=random.randint(50,300)
                    all_sprite_list.add(ufo)
                    ufo_list.add(ufo)

#drone movement block
def droneBlock(round_number, drone_direction, drone_sound, all_sprite_list, drone_list):
    if 25<= round_number < 31:
            drawDangerDrone()
            
            if drone_direction=="left" and len(drone_list)<1:
                random_drone=random.randint(1, 50)
                if random_drone==15:
                    drone_sound.play()
                    drone=Drone(random.choice([-3, -4, -5, -6, -7]))
                    drone.rect.x=700
                    drone.rect.y=random.randint(50,300)
                    all_sprite_list.add(drone)
                    drone_list.add(drone)
            
            elif drone_direction == "right"and len(drone_list)<1:
                random_drone=random.randint(1,50)
                if random_drone==15:
                    drone_sound.play()
                    drone=Drone(random.choice([3, 4, 5, 6, 7]))
                    drone.change_direction()
                    drone.rect.x=-200
                    drone.rect.y=random.randint(50,300)
                    all_sprite_list.add(drone)
                    drone_list.add(drone)

#Block with all the drawing methods                    
def drawScore(score,round_number):
    if round_number<=10 or round_number >20:
        scoreSurf = BASICFONT.render('Score: %s' % (score), True, BLACK)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 120, 30)
        DISPLAYSURF.blit(scoreSurf, scoreRect)
    else:
        scoreSurf = BASICFONT.render('Score: %s' % (score), True, YELLOW)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 120, 30)
        DISPLAYSURF.blit(scoreSurf, scoreRect)
def drawRound(round_number):
    if round_number<10:
        scoreSurf = BASICFONT.render('ROUND: %s' % (round_number), True, BLACK)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH/2-50, 45)
        DISPLAYSURF.blit(scoreSurf, scoreRect)
    else:
        scoreSurf = BASICFONT.render('ROUND: %s' % (round_number), True, YELLOW)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH/2-50, 45)
        DISPLAYSURF.blit(scoreSurf, scoreRect)

def drawPauseMainGame():
    scoreSurf = SMALLFONT.render('P for Pause', True, BLACK)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH/2-60, 485)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def drawPauseInPause():
    pauseSurf=PAUSEFONT.render("PAUSE", True, DARKGRAY)
    pauseRect=pauseSurf.get_rect()
    pauseRect.midtop=(WINDOWWIDTH/2, 150)
    DISPLAYSURF.blit(pauseSurf, pauseRect)

def drawCautionWind():
    scoreSurf = BASICFONT.render('CAUTION: STRONG WIND', True, RED)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH/2-120, 60)
    DISPLAYSURF.blit(scoreSurf, scoreRect) 
    
def drawDangerUFO():
    scoreSurf = BASICFONT.render('DANGER:UFO in the airspace', True, RED)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH/2-130, 75)
    DISPLAYSURF.blit(scoreSurf, scoreRect)
    
def drawDangerDrone():
    scoreSurf1 = SMALLFONT.render("01100100 01100001 01101110 01100111 01100101 01110010"  , True, RED)
    scoreSurf2= SMALLFONT.render("01100100 01110010 01101111 01101110 01100101", True, RED)
    scoreRect1 = scoreSurf1.get_rect()
    scoreRect2 = scoreSurf2.get_rect()
    scoreRect1.topleft = (WINDOWWIDTH/2-185, 65)
    scoreRect2.topleft = (WINDOWWIDTH/2-150, 80)
    DISPLAYSURF.blit(scoreSurf1, scoreRect1)  
    DISPLAYSURF.blit(scoreSurf2, scoreRect2) 
    
def drawMoveToShot():
    scoreSurf = BASICFONT.render('YOU HAVE TO BE MOVING TO SHOOT!!', True, RED)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH/2-170, 60)
    DISPLAYSURF.blit(scoreSurf, scoreRect)    
 
def drawTotalScore(total_score, round_number):
    if round_number <10 or round_number >20:
        scoreSurf = BASICFONT.render('Total Score: %s' % (total_score), True, BLACK)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 780, 35)
        DISPLAYSURF.blit(scoreSurf, scoreRect) 
    else:
        scoreSurf = BASICFONT.render('Total Score: %s' % (total_score), True, YELLOW)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 780, 35)
        DISPLAYSURF.blit(scoreSurf, scoreRect)

def drawAmountShit(number_of_shits, round_number):
    if round_number < 31:
        scoreSurf = BASICFONT.render('Shits: %s' % (number_of_shits), True, DARKGREEN)
    else:
        scoreSurf = BASICFONT.render('Shits: %s' % (number_of_shits), True, DARKGRAY)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 50)
    DISPLAYSURF.blit(scoreSurf, scoreRect) 
    
def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press any key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

def drawTutorialKey():
    pressKeySurf = BASICFONT.render("Use the direction keys to control the pidgeon", True, WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH -790 , WINDOWHEIGHT-30 )
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
    
def drawTutorialKey2():
    pressKeySurf = BASICFONT.render("Use the space bar keys to take a shit and destroy vampires", True, WHITE)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH -790 , WINDOWHEIGHT-50 )
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
    
#---------------------------------------------------------------------------------

#-------------------------------------------------------------------------------- 
#Block with all the posibles screens to show
  
def showWinScreen(score, total_score):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(path.join(sound_folder, "you_win.ogg"))
    pygame.mixer.music.play()
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('YOU', True, GREEN)
    overSurf = gameOverFont.render('WIN', True, GREEN)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)
    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    
    scoreWinOverFont= pygame.font.Font('freesansbold.ttf', 20) 
    totalScoreSurf = scoreWinOverFont.render('Total Score: %s' % (total_score), True, YELLOW)  
    scoreSurf = scoreWinOverFont.render('Score: %s' % (score), True, YELLOW)
    totalScoreRect = totalScoreSurf.get_rect()
    scoreRect = scoreSurf.get_rect()
    totalScoreRect.midbottom = (WINDOWWIDTH / 2, 450)
    scoreRect.midbottom=(WINDOWWIDTH / 2, totalScoreRect.height + 455)
    DISPLAYSURF.blit(totalScoreSurf, totalScoreRect)
    DISPLAYSURF.blit(scoreSurf, scoreRect)
    
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue

    
       
def showStartScreen():

    title=pygame.image.load(path.join(img_dir,"title.png")).convert()
    title.set_alpha(None)

    for x in range(255):
        title.set_alpha(x)
        DISPLAYSURF.blit(title,[0,0])
        pygame.display.flip()
        #pygame.time.delay(20)
    while True:
        drawPressKeyMsg()
        drawTutorialKey2()
        drawTutorialKey()
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(60)

def showGameOverScreen(score, total_score,round_number):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(path.join(sound_folder, "game_over.ogg"))
    pygame.mixer.music.play()
    
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    
    gameSurf = gameOverFont.render('Game', True, DARKGRAY)
    overSurf = gameOverFont.render('Over', True, DARKGRAY)

    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)
    
    scoreWinOverFont= pygame.font.Font('freesansbold.ttf', 20) 
    totalScoreSurf = scoreWinOverFont.render('Total Score: %s' % (total_score), True, YELLOW)  
    scoreSurf = scoreWinOverFont.render('Score: %s' % (score), True, YELLOW)
    totalScoreRect = totalScoreSurf.get_rect()
    scoreRect = scoreSurf.get_rect()
    totalScoreRect.midbottom = (WINDOWWIDTH / 2, 450)
    scoreRect.midbottom=(WINDOWWIDTH / 2, totalScoreRect.height + 455)
    DISPLAYSURF.blit(totalScoreSurf, totalScoreRect)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue


    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            runGame()
            
#-------------------------------------------------------------------------

def checkForKeyPress():
    #Check if any key is pressed to change screen
    
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key
                                    
if __name__ == '__main__':
    main()