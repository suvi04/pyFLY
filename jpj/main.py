import random
import sys
import pygame
import time
pygame.init()
screen=pygame.display.set_mode((1366,768))
pygame.display.set_caption("Py_FLY")
clock=pygame.time.Clock()
font_face=pygame.font.Font(None,50)
score=0
game_active=True
####    SURFACES     ####
sky_surf=pygame.image.load("Py_game/jpj/db/sky.jpg").convert_alpha()
ground_surf=pygame.image.load("Py_game/jpj/db/ground.png").convert_alpha()
ground_surf=pygame.transform.rotozoom(ground_surf,0,1.5)
player_surf=pygame.image.load("Py_game/jpj/db/player.png").convert_alpha()
player_surf_alt=pygame.image.load("Py_game/jpj/db/player.png").convert_alpha()
player_surf_alt=pygame.transform.rotozoom(player_surf_alt,0,0.2)
player_surf=pygame.transform.rotozoom(player_surf,0,0.08)
pipe1_surf=pygame.image.load("Py_game/jpj/db/p1.png").convert_alpha()
pipe1_surf=pygame.transform.rotozoom(pipe1_surf,0,0.6)
pipe2_surf=pygame.image.load("Py_game/jpj/db/p2.png").convert_alpha()
pipe2_surf=pygame.transform.rotozoom(pipe2_surf,0,0.3)
cloud_surf=pygame.image.load("Py_game/jpj/db/cloud.png").convert_alpha()
opp_pipe1_surf=pygame.transform.rotozoom(pipe1_surf,180,1)
opp_pipe2_surf=pygame.transform.rotozoom(pipe2_surf,180,1)
game_over_surf=font_face.render("Press LSHIFT to Restart",True,"white")
dev_info_surf=pygame.image.load("Py_game/jpj/db/endscr.png").convert_alpha()


####    RECTANGLES   ####
sky_rect=sky_surf.get_rect(topleft=(0,0))
ground_rect=ground_surf.get_rect(topleft=(-50,680))
ground_rect_bg=ground_surf.get_rect(topleft=(0,680))
ground_rect_bg2=ground_surf.get_rect(topleft=(20,680))
player_rect=player_surf.get_rect(bottomleft=(10,710))
player_rect_alt=player_surf_alt.get_rect(bottomleft=(20,300))
cloud_rect=cloud_surf.get_rect(center=(1200,300))
cloud_rect_1=cloud_surf.get_rect(center=(200,200))
game_over_rect=game_over_surf.get_rect(center=(683,200))
dev_info_rect=dev_info_surf.get_rect(center=(683,384))


bottom_pipe_a=pipe1_surf.get_rect(bottomleft=(654,725))
bottom_pipe_b=pipe2_surf.get_rect(bottomleft=(876,725))
bottom_pipe_c=pipe1_surf.get_rect(bottomleft=(900,725))
bottom_pipe_d=pipe2_surf.get_rect(bottomleft=(1080,725))
bottom_pipe_e=pipe1_surf.get_rect(bottomleft=(1100,725))
bottom_pipe_f=pipe1_surf.get_rect(bottomleft=(1190,725))
bottom_pipe_g=pipe1_surf.get_rect(bottomleft=(1300,725))
bottom_pipe_h=pipe2_surf.get_rect(bottomleft=(1400,725,))
bottom_pipe_i=pipe2_surf.get_rect(bottomleft=(1600,725))
bottom_pipe_j=pipe1_surf.get_rect(bottomleft=(1600,725))
bottom_pipe_k=pipe1_surf.get_rect(bottomleft=(1100,725))
bottom_pipe_l=pipe1_surf.get_rect(bottomleft=(1190,725))
bottom_pipe_m=pipe1_surf.get_rect(bottomleft=(1300,725))
bottom_pipe_n=pipe2_surf.get_rect(bottomleft=(1400,725,))
bottom_pipe_o=pipe2_surf.get_rect(bottomleft=(1600,725))
bottom_pipe_p=pipe1_surf.get_rect(bottomleft=(1600,725))


upper_pipe_a=opp_pipe1_surf.get_rect(topleft=(654,-20))
upper_pipe_b=opp_pipe2_surf.get_rect(topleft=(876,-20))
upper_pipe_c=opp_pipe1_surf.get_rect(topleft=(900,-20))
upper_pipe_d=opp_pipe2_surf.get_rect(topleft=(1080,-20))
upper_pipe_e=opp_pipe1_surf.get_rect(topleft=(1100,-20))
upper_pipe_f=opp_pipe1_surf.get_rect(topleft=(1190,-20))
upper_pipe_g=opp_pipe1_surf.get_rect(topleft=(1300,-20))
upper_pipe_h=opp_pipe2_surf.get_rect(topleft=(1400,-20))
upper_pipe_i=opp_pipe2_surf.get_rect(topleft=(1600,-20))
upper_pipe_j=opp_pipe1_surf.get_rect(topleft=(1600,-20))
upper_pipe_k=opp_pipe1_surf.get_rect(topleft=(1100,-20))
upper_pipe_l=opp_pipe1_surf.get_rect(topleft=(1190,-20))
upper_pipe_m=opp_pipe1_surf.get_rect(topleft=(1300,-20))
upper_pipe_n=opp_pipe2_surf.get_rect(topleft=(1400,-20))
upper_pipe_o=opp_pipe2_surf.get_rect(topleft=(1600,-20))
upper_pipe_p=opp_pipe1_surf.get_rect(topleft=(1600,-20))










while True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys=pygame.key.get_pressed()
    gravity=3
    gravity+=4 
    pipe_speed=int(4)





    score_surf=font_face.render("Score : "+str(int(round(score,0))),True,"white")
    score_rect=score_surf.get_rect(center=((1366/2),300))
    ####    BLIT    ####
    if game_active==True:

        screen.blit(sky_surf,sky_rect)
        screen.blit(ground_surf,ground_rect)
        screen.blit(ground_surf,ground_rect_bg)
        screen.blit(ground_surf,ground_rect_bg)
        screen.blit(player_surf,player_rect)
        screen.blit(cloud_surf,cloud_rect)
        screen.blit(cloud_surf,cloud_rect_1)
        screen.blit(score_surf,score_rect)

        screen.blit(pipe1_surf,bottom_pipe_a)
        screen.blit(pipe2_surf,bottom_pipe_b)
        screen.blit(pipe1_surf,bottom_pipe_c)
        screen.blit(pipe2_surf,bottom_pipe_d)
        screen.blit(pipe1_surf,bottom_pipe_e)
        screen.blit(pipe1_surf,bottom_pipe_f)
        screen.blit(pipe1_surf,bottom_pipe_g)
        screen.blit(pipe2_surf,bottom_pipe_h)
        screen.blit(pipe2_surf,bottom_pipe_i)
        screen.blit(pipe1_surf,bottom_pipe_j)
        screen.blit(pipe1_surf,bottom_pipe_k)
        screen.blit(pipe1_surf,bottom_pipe_l)
        screen.blit(pipe1_surf,bottom_pipe_m)
        screen.blit(pipe2_surf,bottom_pipe_n)
        screen.blit(pipe2_surf,bottom_pipe_o)
        screen.blit(pipe1_surf,bottom_pipe_p)


        screen.blit(opp_pipe1_surf,upper_pipe_a)
        screen.blit(opp_pipe2_surf,upper_pipe_b)
        screen.blit(opp_pipe1_surf,upper_pipe_c)
        screen.blit(opp_pipe2_surf,upper_pipe_d)
        screen.blit(opp_pipe1_surf,upper_pipe_e)
        screen.blit(opp_pipe1_surf,upper_pipe_f)
        screen.blit(opp_pipe1_surf,upper_pipe_g)
        screen.blit(opp_pipe2_surf,upper_pipe_h)
        screen.blit(opp_pipe2_surf,upper_pipe_i)
        screen.blit(opp_pipe1_surf,upper_pipe_j)
        screen.blit(opp_pipe1_surf,upper_pipe_k)
        screen.blit(opp_pipe1_surf,upper_pipe_l)
        screen.blit(opp_pipe1_surf,upper_pipe_m)
        screen.blit(opp_pipe2_surf,upper_pipe_n)
        screen.blit(opp_pipe2_surf,upper_pipe_o)
        screen.blit(opp_pipe1_surf,upper_pipe_p)



        ####    MOVEMENT    ####
            ####PLAYER####
        if keys[pygame.K_SPACE]:
            gravity-=12
        player_rect.y+=gravity
        if player_rect.y>620:
            player_rect.y=620
        #####CLOUDS####
        cloud_rect.x+=8
        if cloud_rect.x>1300:
            cloud_rect.x=-800
        cloud_rect_1.x+=9
        if cloud_rect_1.x>1300:
            cloud_rect_1.x=-600
        ####GROUND####
        ground_rect.x+=1
        if ground_rect.x>1366:
            ground_rect.x=0
        ground_rect_bg2.x-=1
        ####PIPES####
        bottom_pipe_a.x-=pipe_speed
        bottom_pipe_b.x-=pipe_speed
        bottom_pipe_c.x-=pipe_speed
        bottom_pipe_d.x-=pipe_speed
        bottom_pipe_e.x-=pipe_speed
        bottom_pipe_f.x-=pipe_speed
        bottom_pipe_g.x-=pipe_speed
        bottom_pipe_h.x-=pipe_speed
        bottom_pipe_i.x-=pipe_speed
        bottom_pipe_j.x-=pipe_speed
        bottom_pipe_k.x-=pipe_speed
        bottom_pipe_l.x-=pipe_speed
        bottom_pipe_m.x-=pipe_speed
        bottom_pipe_n.x-=pipe_speed
        bottom_pipe_o.x-=pipe_speed
        bottom_pipe_p.x-=pipe_speed

        upper_pipe_a.x-=pipe_speed
        upper_pipe_b.x-=pipe_speed
        upper_pipe_c.x-=pipe_speed
        upper_pipe_d.x-=pipe_speed
        upper_pipe_e.x-=pipe_speed
        upper_pipe_f.x-=pipe_speed
        upper_pipe_g.x-=pipe_speed
        upper_pipe_h.x-=pipe_speed
        upper_pipe_i.x-=pipe_speed
        upper_pipe_j.x-=pipe_speed
        upper_pipe_k.x-=pipe_speed
        upper_pipe_l.x-=pipe_speed
        upper_pipe_m.x-=pipe_speed
        upper_pipe_n.x-=pipe_speed
        upper_pipe_o.x-=pipe_speed
        upper_pipe_p.x-=pipe_speed

        posn=random.randint(-90,-30)
        if bottom_pipe_a.x<posn:
            bottom_pipe_a.x=1200
        posn=random.randint(-90,-30)


        if bottom_pipe_b.x<posn:
            bottom_pipe_b.x=1400
        posn=random.randint(-90,-30)

        if bottom_pipe_c.x<posn:
            bottom_pipe_c.x=1300
        posn=random.randint(-90,-30)

        if bottom_pipe_d.x<posn:
            bottom_pipe_d.x=1400
        posn=random.randint(-90,-30)

        if bottom_pipe_e.x<posn:
            bottom_pipe_e.x=1300
        posn=random.randint(-90,-30)

        if bottom_pipe_f.x<posn:
            bottom_pipe_f.x=1600
        posn=random.randint(-90,-30)

        if bottom_pipe_g.x<posn:
            bottom_pipe_g.x=1400
        posn=random.randint(-90,-30)

        if bottom_pipe_h.x<posn:
            bottom_pipe_h.x=1200
        posn=random.randint(-90,-30)

        if bottom_pipe_i.x<posn:
            bottom_pipe_i.x=1100
        posn=random.randint(-90,-30)

        if bottom_pipe_j.x<posn:
            bottom_pipe_j.x=1200
        posn=random.randint(-90,-30)

        if bottom_pipe_k.x<posn:
            bottom_pipe_k.x=1400
        posn=random.randint(-90,-30)

        if bottom_pipe_l.x<posn:
            bottom_pipe_l.x=1300
        posn=random.randint(-90,-30)

        if bottom_pipe_m.x<posn:
            bottom_pipe_m.x=1400
        posn=random.randint(-90,-30)

        if bottom_pipe_n.x<posn:
            bottom_pipe_n.x=1300
        posn=random.randint(-90,-30)

        if bottom_pipe_o.x<posn:
            bottom_pipe_o.x=1600
        posn=random.randint(-90,-30)

        if bottom_pipe_p.x<posn:
            bottom_pipe_p.x=1400
        posn=random.randint(-90,-30)



        posn=random.randint(-90,-30)
        if upper_pipe_a.x<posn:
            upper_pipe_a.x=1200
        posn=random.randint(-90,-30)


        if upper_pipe_b.x<posn:
            upper_pipe_b.x=1400
        posn=random.randint(-90,-30)

        if upper_pipe_c.x<posn:
            upper_pipe_c.x=1300
        posn=random.randint(-90,-30)

        if upper_pipe_d.x<posn:
            upper_pipe_d.x=1400
        posn=random.randint(-90,-30)

        if upper_pipe_e.x<posn:
            upper_pipe_e.x=1300
        posn=random.randint(-90,-30)

        if upper_pipe_f.x<posn:
            upper_pipe_f.x=1600
        posn=random.randint(-90,-30)

        if upper_pipe_g.x<posn:
            upper_pipe_g.x=1400
        posn=random.randint(-90,-30)

        if upper_pipe_h.x<posn:
            upper_pipe_h.x=1200
        posn=random.randint(-90,-30)

        if upper_pipe_i.x<posn:
            upper_pipe_i.x=1100
        posn=random.randint(-90,-30)

        if upper_pipe_j.x<posn:
            upper_pipe_j.x=1200
        posn=random.randint(-90,-30)

        if upper_pipe_k.x<posn:
            upper_pipe_k.x=1400
        posn=random.randint(-90,-30)

        if upper_pipe_l.x<posn:
            upper_pipe_l.x=1300
        posn=random.randint(-90,-30)

        if upper_pipe_m.x<posn:
            upper_pipe_m.x=1400
        posn=random.randint(-90,-30)

        if upper_pipe_n.x<posn:
            upper_pipe_n.x=1300
        posn=random.randint(-90,-30)

        if upper_pipe_o.x<posn:
            upper_pipe_o.x=1600
        posn=random.randint(-90,-30)

        if upper_pipe_p.x<posn:
            upper_pipe_p.x=1400
        posn=random.randint(-90,-30)

        if player_rect.colliderect(bottom_pipe_a):
            game_active=False
        if player_rect.colliderect(bottom_pipe_b):
            game_active=False
        if player_rect.colliderect(bottom_pipe_c):
            game_active=False
        if player_rect.colliderect(bottom_pipe_d):
            game_active=False
        if player_rect.colliderect(bottom_pipe_e):
            game_active=False
        if player_rect.colliderect(bottom_pipe_f):
            game_active=False
        if player_rect.colliderect(bottom_pipe_g):
            game_active=False
        if player_rect.colliderect(bottom_pipe_h):
            game_active=False
        if player_rect.colliderect(bottom_pipe_i):
            game_active=False
        if player_rect.colliderect(bottom_pipe_j):
            game_active=False
        if player_rect.colliderect(bottom_pipe_k):
            game_active=False
        if player_rect.colliderect(bottom_pipe_l):
            game_active=False
        if player_rect.colliderect(bottom_pipe_m):
            game_active=False
        if player_rect.colliderect(bottom_pipe_n):
            game_active=False
        if player_rect.colliderect(bottom_pipe_o):
            game_active=False
        if player_rect.colliderect(bottom_pipe_p):
            game_active=False

    
    
    
    if game_active==False:
        screen.fill((201,148,227))
        screen.blit(game_over_surf,game_over_rect)
        screen.blit(dev_info_surf,dev_info_rect)
        screen.blit(player_surf_alt,player_rect_alt)
        pygame.display.update()
        score=0
        upper_pipe_p.x=1400
        upper_pipe_o.x=1600
        upper_pipe_n.x=1300
        upper_pipe_m.x=1400
        upper_pipe_l.x=1300
        upper_pipe_k.x=1400
        upper_pipe_j.x=1200
        upper_pipe_i.x=1100
        upper_pipe_h.x=1200
        upper_pipe_g.x=1400
        upper_pipe_f.x=1600
        upper_pipe_e.x=1300
        upper_pipe_d.x=1400
        upper_pipe_c.x=1300
        upper_pipe_b.x=1400
        upper_pipe_a.x=1200

        bottom_pipe_p.x=1400
        bottom_pipe_o.x=1600
        bottom_pipe_n.x=1300
        bottom_pipe_m.x=1400
        bottom_pipe_l.x=1300
        bottom_pipe_k.x=1400
        bottom_pipe_j.x=1200
        bottom_pipe_i.x=1100
        bottom_pipe_h.x=1200
        bottom_pipe_g.x=1400
        bottom_pipe_f.x=1600
        bottom_pipe_e.x=1300
        bottom_pipe_d.x=1400
        bottom_pipe_c.x=1300
        bottom_pipe_b.x=1400
        bottom_pipe_a.x=1200




        if keys[pygame.K_LSHIFT]:
                game_active=True

        




    score+=0.049 
    pipe_speed+=0.004
    pygame.display.update()
    clock.tick(60)