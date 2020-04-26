import pygame
import random
import sys
pygame.init()
screen = pygame.display.set_mode((500,500))
game_over = False
clock = pygame.time.Clock()
player_pos=[250,250]
food_pos=[250,200]
ch=0
myFont=pygame.font.SysFont("monospace",30) 
score=1
snake_List=[]

pygame.mixer.music.load("data/Cat-Burglars.mp3") 
pygame.mixer.music.play(-1,0.0)
BG= pygame.image.load("data/3.jpg")
BG=pygame.transform.scale(BG,(500,500))
apple=pygame.image.load("data/5.png")
apple=pygame.transform.scale(apple,(25,25))
snake=pygame.image.load("data/me.png")
snake=pygame.transform.scale(snake,(30,30))
head=pygame.image.load("data/1.png")
head=pygame.transform.scale(head,(50,50))
snake_point=pygame.image.load("data/3.png")
snake_point=pygame.transform.scale(snake_point,(300,300))
snake_lost=pygame.image.load("data/4.png")
snake_lost=pygame.transform.scale(snake_lost,(300,300))
point=pygame.mixer.Sound("data/11.wav")
out=pygame.mixer.Sound("data/22.wav")
def our_snake(snake_List):
        for x in snake_List:
                if x==snake_List[-1]:
                        screen.blit(head, [x[0]-20,x[1]-20])
                else:
                        screen.blit(snake, [x[0]-10,x[1]-10])
                        pygame.draw.circle(screen,(121,199,103),[x[0],x[1]],15)

        
def coll(player_pos,food_pos):
        p_x=player_pos[0]
        p_y=player_pos[1]
        e_x=food_pos[0]
        e_y=food_pos[1]
        if (e_x>=p_x and e_x<=(p_x+20)) or (p_x>=e_x and p_x<=(e_x+20)):
                if(e_y>=p_y and e_y<=(p_y+20)) or (p_y>=e_y and p_y<=(e_y+20)):
                        return True
        return False


while not game_over:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                                if ch==2:
                                        pass
                                else:
                                        ch=1
                                        if player_pos[0]<=0:
                                                player_pos[0]=490
                                        player_pos[0]-= 10
                        if event.key == pygame.K_RIGHT:
                                if ch==1:
                                        pass
                                else:
                                        ch=2
                                        if player_pos[0]>=490:
                                                player_pos[0]=0
                                        player_pos[0]+= 10
                        if event.key == pygame.K_UP:
                                if ch==4:
                                        pass
                                else:
                                        ch=3
                                        if player_pos[1]<=0:
                                                player_pos[1]=490
                                        player_pos[1]-=10
                        if event.key == pygame.K_DOWN:
                                if ch==3:
                                        pass
                                else:
                                        ch=4
                                        if player_pos[1]>=490:
                                                player_pos[1]=0
                                        player_pos[1]+=10
        screen.fill((0,0,0))
        screen.blit(BG, [0,0])
        screen.blit(apple, [food_pos[0],food_pos[1]])
        if coll(player_pos,food_pos):
                point.play()
                score+=1
                while(random.random()<0.01):
                        continue
                food_pos=[random.randrange(0,450,50),random.randrange(0,450,50)]
        if ch==1:
                if player_pos[0]<=0:
                        player_pos[0]=490
                player_pos[0]-= 10
        if ch==2:
                if player_pos[0]>=490:
                        player_pos[0]=0
                player_pos[0]+= 10
        if ch==3:
                if player_pos[1]<=0:
                        player_pos[1]=490
                player_pos[1]-= 10
        if ch==4:
                if player_pos[1]>=490:
                        player_pos[1]=0
                player_pos[1]+= 10
        snake_Head = []
        snake_Head.append(player_pos[0])
        snake_Head.append(player_pos[1])
        snake_List.append(snake_Head)
        if len(snake_List) > score:
                del snake_List[0]
        for x in snake_List[:-1]:
                if x == snake_Head:
                        screen.blit(snake_lost, [0,200])
                        screen.blit(label,(300,450))
                        out.play()
                        game_over= True
        our_snake(snake_List)
        text="Score:"+str(score) 
        label=myFont.render(text,1,(255,255,0))
        screen.blit(label,(300,450))
        if score==1:
                screen.blit(snake_point, [0,200])
        clock.tick(30)
        pygame.display.update()
