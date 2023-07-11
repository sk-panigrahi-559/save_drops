import pygame as pyg
import random as rnd

# game initialisation
pyg.init()
screen = pyg.display.set_mode((760, 400))
pyg.display.set_caption("TIP TIP")
drop_pos_y = 300
drop_pos_x = 0
drop_fall = 7
tap_dic = {1: 55,
           2: 255,
           3: 455,
           4: 655}
points = 0
fails = 0
font_points = pyg.font.Font('freesansbold.ttf', 30)
font = pyg.font.Font('freesansbold.ttf', 70)
fonts_small = pyg.font.Font('freesansbold.ttf', 15)


# this function will make the drops to fall
def fall(tap):
    global drop_pos_y, drop_pos_x
    drop_pos_y = 55
    drop_pos_x = tap_dic[tap]


# initial variables
start = False
end = False
game_over = False
done = False
clock = pyg.time.Clock()
basket_x = 380
basket_y = 290

while not done:
    clock.tick(20)

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            done = True

    while not start:
        clock.tick(5)
        screen.fill([200, 200, 255])

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                start = True
                done = True
            if event.type == pyg.KEYDOWN and event.key == pyg.K_SPACE:
                start = True

        start_name = font.render('TIP TIP', True, 'blue', 'brown')
        start_instruction = fonts_small.render("press space to start", True, (200, 200, 255), 'black')
        name_frame = start_name.get_rect()
        name_frame.center = (350, 150)
        screen.blit(start_name, name_frame)
        start_frame = start_instruction.get_rect()
        start_frame.center = (350, 250)
        screen.blit(start_instruction, start_frame)
        pyg.display.flip()
    screen.fill([200, 200, 255])
    pyg.draw.rect(screen, (100, 255, 0), pyg.Rect(0, 300, 760, 100))
    pyg.draw.line(screen, 'black', (0, 300), (760, 300))

    # pipeline
    pyg.draw.rect(screen, 'dark grey', pyg.Rect(0, 30, 660, 10))

    # taps
    pyg.draw.rect(screen, 'dark grey', pyg.Rect(50, 40, 10, 10))
    pyg.draw.rect(screen, 'dark grey', pyg.Rect(250, 40, 10, 10))
    pyg.draw.rect(screen, 'dark grey', pyg.Rect(450, 40, 10, 10))
    pyg.draw.rect(screen, 'dark grey', pyg.Rect(650, 40, 10, 10))

    # mouse position
    mou_pos = pyg.mouse.get_pos()
    basket_x = mou_pos[0]
    pyg.mouse.set_visible(False)

    # drop logic
    tap_number = rnd.randint(1, 4)
    if drop_pos_y >= 300:
        fall(tap_number)
    pyg.draw.ellipse(screen, 'blue', pyg.Rect(drop_pos_x, drop_pos_y, 5, 10))
    drop_pos_y += drop_fall

    # pot
    pyg.draw.circle(screen, "brown", (basket_x, basket_y), 30, 30)
    pyg.draw.rect(screen, 'brown', pyg.Rect(basket_x - 12.5, basket_y - 50, 25, 30))

    # score logic
    if basket_y - 45 >= drop_pos_y >= basket_y - 50 and (basket_x - 12.5 <= drop_pos_x <= basket_x + 12.5):
        points += 1
    elif (basket_y - 45 >= drop_pos_y >= basket_y - 50) and not(basket_x - 12.5 <= drop_pos_x <= basket_x + 12.5):
        fails+=1
    print(fails)
    text = font_points.render('POINTS:' + str(points), True, 'red', 'black')
    text_frame = text.get_rect()
    text_frame.center = (680, 350)
    screen.blit(text, text_frame)
    if (fails >= 3):
        game_over = True
    
    while game_over:
        clock.tick(5)
        screen.fill([200, 200, 255])

        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                start = True
                done = True
            if event.type == pyg.KEYDOWN and event.key == pyg.K_SPACE:
                end = True
                break

        end_name = font.render('TIP TIP', True, 'blue', 'red')
        end_instruction = fonts_small.render("press space to exit", True, (200, 200, 255), 'black')
        name_frame = end_name.get_rect()
        name_frame.center = (350, 150)
        screen.blit(start_name, name_frame)
        end_frame = end_instruction.get_rect()
        end_frame.center = (350, 250)
        screen.blit(end_instruction, end_frame)
        pyg.display.flip()
        if end == True:
            break
    
    if end == True:
        done = True
    pyg.display.flip()
