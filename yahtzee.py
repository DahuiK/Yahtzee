import random
import pygame

pygame.init()

# Decalring Variable 
WIDTH = 600 
HEIGHT = 800 
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Yahtzee!')
timer = pygame.time.Clock()
fps = 60 
font = pygame.font.Font('freesansbold.ttf', 18)
background = (128,128,128)
white = (255,255,255) 
black = (0,0,0)
numbers = [0,0,0,0,0]
roll = False
rolls_left = 3
dice_selected = [False, False, False, False, False]
selected_choice = [False,False,False,False,False,False,False,False,False,False,False,False,False] 
possible = [False,False,False,False,False,False,False,False,False,False,False,False,False] 
done = [False,False,False,False,False,False,False,False,False,False,False,False,False] 
score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
totals = [0, 0, 0, 0, 0, 0, 0]
current_score = 0 
game_score = 0
high_score = 0 
clicked = -1
something_selected = False
bonus_time = False
game_over = False

#check score 
def check_scores(choice_list, numbers_list, possible_list, scores_list): 
    active = 0
    for index in range(len(choice_list)): 
        if choice_list[index]: 
            active = index
    if active == 0: 
        current_score = numbers_list.count(1) 
    elif active == 1: 
        current_score = numbers_list.count(2) *2
    elif active == 2: 
        current_score = numbers_list.count(3) *3
    elif active == 3: 
        current_score = numbers_list.count(4) *4
    elif active == 4: 
        current_score = numbers_list.count(5) *5
    elif active == 5: 
        current_score = numbers_list.count(6) *6
    elif active == 6 or active == 7: 
        if possible_list[active]: 
            current_score = sum(numbers_list) 
        else: 
            current_score = 0 
    elif active == 8: 
        if possible_list[active]:
            current_score = 25
        else: 
            current_score = 0
    elif active == 9: 
        if possible_list[active]:
            current_score = 30
        else: 
            current_score = 0
    elif active == 10: 
        if possible_list[active]:
            current_score = 40
        else: 
            current_score = 0    
    elif active == 11: 
        if possible_list[active]:
            current_score = 50
        else: 
            current_score = 0  
    elif active == 12: 
        current_score = sum(numbers_list)
    return current_score



# Formatting game sheet 
def draw_stuff():
    global game_score
    global game_over
    if game_over: 
        gg_text = font.render('Game Over: Click to Restart', True, white)
        screen.blit(gg_text, (280, 290))
    score_text = font.render('Score: ' + str(game_score), True, (255, 255, 255))
    screen.blit(score_text, (285, 340))
    high_score_text = font.render('High Score: ' + str(high_score), True, (255, 255, 255))
    screen.blit(high_score_text, (285, 370))
    roll_text = font.render('Click to Roll', True, white)
    screen.blit(roll_text, (98,165))
    accept_text = font.render('Accept Turn', True, white)
    screen.blit(accept_text, (388,165))
    rolls_text = font.render('Rolls Left this Turn:' + str(rolls_left), True, white)
    screen.blit(rolls_text, (15,15))
    inst_text = font.render('Click on a Die to it Keep or Release', True, white)
    screen.blit(inst_text, (280,15))
    pygame.draw.rect(screen, white, [0, 200, 280, HEIGHT - 200])
    pygame.draw.line(screen, black, (0, 40), (WIDTH, 40), 3)
    pygame.draw.line(screen, black, (0, 200), (WIDTH, 200), 3)
    pygame.draw.line(screen, black, (200, 200), (200, HEIGHT), 3)
    pygame.draw.line(screen, black, (280, 200), (280, HEIGHT),3)

# Dice class 
class Dice: 
    def __init__(self,x_pos, y_pos,num,key):
        global dice_selected
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.number = num 
        self.key = key 
        self.die = ''
        self.selected = dice_selected[key]
        
    def draw(self): 
        self.die = pygame.draw.rect(screen, white, [self.x_pos,self.y_pos, 100, 100], 0, 5)
        if self.number == 1: 
            pygame.draw.circle(screen, black, (self.x_pos + 50 , self.y_pos + 50), 10)
        if self.number == 2: 
            pygame.draw.circle(screen, black, (self.x_pos + 20 , self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80 , self.y_pos + 80), 10)
        if self.number == 3: 
            pygame.draw.circle(screen, black, (self.x_pos + 20 , self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 50 , self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80 , self.y_pos + 80), 10)
        if self.number == 4: 
            pygame.draw.circle(screen, black, (self.x_pos + 20 , self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20 , self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80 , self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80 , self.y_pos + 20), 10)
        if self.number == 5: 
            pygame.draw.circle(screen, black, (self.x_pos + 20 , self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20 , self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 50 , self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80 , self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80 , self.y_pos + 20), 10)
        if self.number == 6: 
            pygame.draw.circle(screen, black, (self.x_pos + 20 , self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20 , self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20 , self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80 , self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80 , self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80 , self.y_pos + 20), 10)
        if self.selected: 
            pygame.draw.rect(screen, (255,0,0), [self.x_pos,self.y_pos, 100, 100], 4, 5)
    
    def check_click(self, coordinates): 
        if self.die.collidepoint(coordinates): 
            if dice_selected[self.key]: 
                dice_selected[self.key] = False
            elif not dice_selected[self.key]: 
                dice_selected[self.key] = True

# score card 
class Choice: 
    def __init__(self, x_pos, y_pox, text, select, possible, done, score):   
        self.x_pos = x_pos
        self.y_pos = y_pox
        self.text = text
        self.select = select
        self.possible = possible
        self.done = done
        self.score = score
        
    def draw(self): 
        pygame.draw.line(screen, black, (self.x_pos, self.y_pos), (self.x_pos +280, self.y_pos), 2)
        pygame.draw.line(screen, black, (self.x_pos, self.y_pos + 30), (self.x_pos +280, self.y_pos +30), 2)
        if not self.done: 
            if self.possible: 
                my_text = font.render(self.text, True, (0,100,0))
            elif not self.possible: 
                my_text = font.render(self.text, True, (200,0,0))
        else: 
            my_text = font.render(self.text, True, black)
        if self.select: 
            pygame.draw.rect(screen, (20,35,30), [self.x_pos, self.y_pos, 200, 30])
        screen.blit(my_text, (self.x_pos + 5, self.y_pos + 10))
        score_text = font.render(str(self.score), True, (0,0,200))
        screen.blit(score_text, (self.x_pos + 210, self.y_pos + 10))
        
        
# Tracking the game sheet
def check_possibilities(possible_list, numbers_list): 
    possible_list[0] = True
    possible_list[1] = True
    possible_list[2] = True
    possible_list[3] = True
    possible_list[4] = True
    possible_list[5] = True
    possible_list[12] = True
    max_count = 0
    
    for index in range(1, 7): 
        if numbers_list.count(index) > max_count:
            max_count = numbers_list.count(index) 
    if max_count >= 3: 
        possible_list[6] = True
        if max_count >= 4:
            possible_list[7] = True
            if max_count >= 5: 
                possible_list[11] = True
    if max_count < 3: 
        possible_list[6] = False
        possible_list[7] = False
        possible_list[8] = False
        possible_list[11] = False
    elif max_count == 3: 
        possible_list[7] = False
        possible_list[11] = False
        checker = False
        for index in range(len(numbers_list)): 
            if numbers_list.count(numbers_list[index]) == 2: 
                possible_list[8] = True
                checker = True
        if not checker: 
            possible_list[8] = False
    elif max_count == 4: 
        possible_list[11] = False
    
    lowest = 10
    highest = 0
    for index in range(len(numbers_list)): 
        if numbers_list[index] < lowest: 
            lowest = numbers_list[index]
        if numbers_list[index] > highest: 
            highest = numbers_list[index]
    # lg.straight
    if (lowest + 1 in numbers_list) and (lowest + 2 in numbers_list) and (lowest + 3 in numbers_list) and (lowest + 4 in numbers_list): 
        possible_list[10] = True
    else: 
        possible_list[10] = False
    # sm.straight
    if (lowest + 1 in numbers_list) and (lowest + 2 in numbers_list) and (lowest + 3 in numbers_list) or \
        ((highest - 1 in numbers_list) and (highest - 2 in numbers_list) and (highest - 3 in numbers_list)): 
        possible_list[9] = True
    else: 
        possible_list[9] = False
    
    return possible_list

# tracking the click for the storing the scores 
def make_choice(clicked_num, selected, done_list): 
    for index in range(len(selected)):
        selected[index] = False
    if not done_list[clicked_num]: 
        selected[clicked_num] = True
    return selected

# tracking total numbers 
def check_total(totals_list, score_list, bonus): 
    totals_list[0] = score_list[0] +score_list[1] + score_list[2]+ score_list[3]+ score_list[4]+ score_list[5]
    if totals_list[0] >= 63: 
        totals_list[1] = 35 
    else: 
        totals_list[1] = 0 
    totals_list[2] = totals_list[1] +totals_list[0] 
    if bonus: 
        totals_list[3] += 100
        bonus = False
    totals_list[4] = score_list[7] +score_list[8] + score_list[9]+ score_list[10]+ score_list[11]+ score_list[12] + totals_list[3] 
    totals_list[5] = totals_list[2] 
    totals_list[6] = totals_list[4] + totals_list[5] 
    return totals_list, bonus

#restart function 
def restart_function(): 
    global numbers 
    global rolls_left
    global dice_selected
    global roll
    global score
    global selected_choice
    global possible
    global done
    global totals
    global clicked 
    global current_score
    global something_selected
    global bonus_time
    global game_score
    global high_score
    numbers = [0,0,0,0,0]
    roll = False
    rolls_left = 3
    dice_selected = [False, False, False, False, False]
    selected_choice = [False,False,False,False,False,False,False,False,False,False,False,False,False] 
    possible = [False,False,False,False,False,False,False,False,False,False,False,False,False] 
    done = [False,False,False,False,False,False,False,False,False,False,False,False,False] 
    score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    totals = [0, 0, 0, 0, 0, 0, 0]
    current_score = 0 
    clicked = -1
    something_selected = False
    bonus_time = False
    game_score = 0
    high_score = 0  

# Main game loop
running = True
while running: 
    # displays 
    timer.tick(fps)
    screen.fill(background)
    if game_over: 
        restart_button = pygame.draw.rect(screen, black, [275,275,300,30])
    roll_button = pygame.draw.rect(screen, black, [10,160,280,30])
    accept_button = pygame.draw.rect(screen, black, [310, 160, 280, 30])
    draw_stuff()
    
    die1 = Dice(10, 50, numbers[0], 0)
    die2 = Dice(130, 50, numbers[1], 1)
    die3 = Dice(250, 50, numbers[2], 2)
    die4 = Dice(370, 50, numbers[3], 3)
    die5 = Dice(490, 50, numbers[4], 4)  
    ones = Choice(0, 200, 'Aces', selected_choice[0], possible[0], done[0], score[0])
    twos = Choice(0, 230, 'Twos', selected_choice[1], possible[1], done[1], score[1])
    Threes = Choice(0, 260, 'Threes', selected_choice[2], possible[2], done[2], score[2])
    fours = Choice(0, 290, 'Fours', selected_choice[3], possible[3], done[3], score[3])
    fives = Choice(0, 320, 'Fives', selected_choice[4], possible[4], done[4], score[4])
    sixes = Choice(0, 350, 'Sixes', selected_choice[5], possible[5], done[5], score[5])
    upper_total1 = Choice(0, 380, 'Upper Score', False, False, True, totals[0])
    upper_bonus = Choice(0, 410, 'Bonus if >= 63', False, False, True, totals[1])
    upper_total2 = Choice(0, 440, 'Upper Total', False, False, True, totals[2])
    three_kind = Choice(0, 470, '3 of a kind', selected_choice[6], possible[6], done[6], score[6])
    four_kind = Choice(0, 500, '4 of a kind', selected_choice[7], possible[7], done[7], score[7])
    full_house = Choice(0, 530, 'Full House', selected_choice[8], possible[8], done[8], score[8])
    sm_straight = Choice(0, 560, 'Sm.Straight (seq of 4)', selected_choice[9], possible[9], done[9], score[9])
    lg_straight = Choice(0, 590, 'Lg.stragith (seq of 5)', selected_choice[10], possible[10], done[10], score[10])
    yahtzee = Choice(0, 620, 'YAHTZEE', selected_choice[11], possible[11], done[11], score[11])
    chance = Choice(0, 650, 'Chance', selected_choice[12], possible[12], done[12], score[12])
    bonus = Choice(0, 680, 'Yahtzee Bonus', False, False, True, totals[3])
    lower_total1= Choice(0, 710, 'Lower Score', False, False, True, totals[4])
    lower_total2 = Choice(0, 740, 'Upper Total', False, False, True, totals[5])
    grand_total = Choice(0, 770, 'Grand Total', False, False, True, totals[6])
    game_score = totals[6] 
    
    possible = check_possibilities(possible, numbers)
    current_score = check_scores(selected_choice, numbers, possible, score)
    totals, bonus_time = check_total(totals, score, bonus_time)
    if True in selected_choice: 
        something_selected = True
    
    die1.draw()
    die2.draw()
    die3.draw()
    die4.draw()
    die5.draw()
    ones.draw()
    twos.draw()
    Threes.draw()
    fours.draw()
    fives.draw()
    sixes.draw()
    upper_total1.draw()
    upper_bonus.draw()
    upper_total2.draw()
    three_kind.draw() 
    four_kind.draw()
    full_house.draw()
    sm_straight.draw()
    lg_straight.draw()
    yahtzee.draw() 
    chance.draw() 
    bonus.draw() 
    lower_total1.draw() 
    lower_total2.draw()
    grand_total.draw()
    
    # Event handling 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if game_over and restart_button.collidepoint(event.pos): 
                restart_function()
                game_over = False
            die1.check_click(event.pos)
            die2.check_click(event.pos)
            die3.check_click(event.pos)
            die4.check_click(event.pos)
            die5.check_click(event.pos)
            if 0 <= event.pos[0] <= 155:
                if 200 < event.pos[1] < 381 or 470 < event.pos[1] < 681:
                    if 200 < event.pos[1] < 230:
                        clicked = 0
                    elif 230 < event.pos[1] < 260:
                        clicked = 1
                    elif 260 < event.pos[1] < 290:
                        clicked = 2
                    elif 290 < event.pos[1] < 320:
                        clicked = 3
                    elif 320 < event.pos[1] < 350:
                        clicked = 4
                    elif 350 < event.pos[1] < 380:
                        clicked = 5
                    elif 470 < event.pos[1] < 500:
                        clicked = 6
                    elif 500 < event.pos[1] < 530:
                        clicked = 7
                    elif 530 < event.pos[1] < 560:
                        clicked = 8
                    elif 560 < event.pos[1] < 590:
                        clicked = 9
                    elif 590 < event.pos[1] < 620:
                        clicked = 10
                    elif 620 < event.pos[1] < 650:
                        clicked = 11
                    elif 650 < event.pos[1] < 680:
                        clicked = 12
                    selected_choice = make_choice(clicked, selected_choice, done)
            if roll_button.collidepoint(event.pos) and rolls_left >0: 
                roll = True
                rolls_left -= 1
            if accept_button.collidepoint(event.pos) and something_selected and rolls_left <3: 
                if score[11] == 50 and done[11] and possible[11]: 
                    bonus_time = True
                for i in range(len(selected_choice)): 
                    if selected_choice[i]: 
                        done[i] = True
                        score[i] = current_score
                        selected_choice[i] = False
                for i in range(len(dice_selected)): 
                    dice_selected[i] = False
                numbers = [7, 8, 18, 33, 39]
                something_selected = False
                rolls_left = 3
    
    if roll:
        for number in range(len(numbers)):
            if not dice_selected[number]:
                numbers[number] = random.randint(1, 6)
        roll = False
    
    for i in range(len(possible)):
        if selected_choice[i] and not possible[i]:
            click_text = font.render('Choosing that option will give you a zero!', True, (155, 34, 34))
            screen.blit(click_text, (230, 205))
        if selected_choice[i]:
            something_selected = True
    
    if game_over:
        if game_score > high_score:
            high_score = game_score

    if False not in done: 
        game_over = True
        
    pygame.display.flip()
pygame.quit