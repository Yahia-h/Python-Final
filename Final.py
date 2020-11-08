import pygame

from pygame.locals import *

pygame.init()
FPS = 30

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
window = pygame.display.set_mode((550, 550))
font = pygame.font.Font('freesansbold.ttf', 56)

pygame.display.set_caption("tic-tac-toe")

# print() equivalent
first = pygame.draw.rect(window, white, (25, 25, 150, 150))
second = pygame.draw.rect(window, white, (200, 25, 150, 150))
third = pygame.draw.rect(window, white, (375, 25, 150, 150))
forth = pygame.draw.rect(window, white, (25, 200, 150, 150))
fifth = pygame.draw.rect(window, white, (200, 200, 150, 150))
sixth = pygame.draw.rect(window, white, (375, 200, 150, 150))
seventh = pygame.draw.rect(window, white, (25, 375, 150, 150))
eighth = pygame.draw.rect(window, white, (200, 375, 150, 150))
ninth = pygame.draw.rect(window, white, (375, 375, 150, 150))

# insert() equivalent                                                          }main() equivalent
first_open = True
second_open = True
third_open = True
fourth_open = True
fifth_open = True
sixth_open = True
seventh_open = True
eighth_open = True
ninth_open = True

num = 0
won = False

run = True
shape = 1
winner = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def win_check(num):
    for row in winner:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            return True

    for column in range(3):
        for row in winner:
            if row[column] == num:
                continue
            else:
                break
        else:
            return True

    for tile in range(3):
        if winner[tile][tile] == num:
            continue
        else:
            break
    else:
        return True

    for tile in range(3):
        if winner[tile][2 - tile] == num:
            continue
        else:
            break
    else:
        return True


while run:
    pygame.time.delay(100)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(shape)
            if not won:
                if first.collidepoint(pos) and first_open:
                    if shape == 1:

                        pygame.draw.circle(window, (0, 0, 0), (100, 100), 50, 5)
                        shape = 0

                        winner[0][0] = 1
                    elif shape == 0:
                        pygame.draw.line(window, (0, 0, 0), (25, 25), (175, 175), 10)
                        pygame.draw.line(window, (0, 0, 0), (175, 25), (25, 175), 10)
                        shape = 1

                        winner[0][0] = 2
                    first_open = False
                elif second.collidepoint(pos) and second_open:
                    if shape == 1:
                        pygame.draw.circle(window, (0, 0, 0), (275, 100), 50, 5)

                        shape = 0
                        winner[0][1] = 1
                    elif shape == 0:
                        pygame.draw.line(window, (0, 0, 0,), (200, 25), (350, 175), 10)
                        pygame.draw.line(window, (0, 0, 0,), (350, 25), (200, 175), 10)
                        shape = 1
                        winner[0][1] = 2
                    second_open = False
                elif third.collidepoint(pos) and third_open:
                    if shape == 1:
                        pygame.draw.circle(window, (0, 0, 0), (450, 100), 50, 5)

                        shape = 0
                        winner[0][2] = 1
                    elif shape == 0:
                        pygame.draw.line(window, (0, 0, 0,), (375, 25), (525, 175), 10)
                        pygame.draw.line(window, (0, 0, 0,), (525, 25), (375, 175), 10)
                        shape = 1
                        winner[0][2] = 2
                    third_open = False
                elif forth.collidepoint(pos) and fourth_open:
                    if shape == 1:
                        pygame.draw.circle(window, (0, 0, 0), (100, 275), 50, 5)

                        shape = 0
                        winner[1][0] = 1
                    elif shape == 0:
                        pygame.draw.line(window, (0, 0, 0,), (25, 200), (175, 350), 10)
                        pygame.draw.line(window, (0, 0, 0,), (175, 200), (25, 350), 10)
                        shape = 1
                        winner[1][0] = 2
                    fourth_open = False
                elif fifth.collidepoint(pos) and fifth_open:
                    if shape == 1:
                        pygame.draw.circle(window, (0, 0, 0), (275, 275), 50, 5)
                        shape = 0
                        winner[1][1] = 1
                    elif shape == 0:
                        pygame.draw.line(window, (0, 0, 0,), (200, 200), (350, 350), 10)
                        pygame.draw.line(window, (0, 0, 0,), (350, 200), (200, 350), 10)
                        shape = 1
                        winner[1][1] = 2
                    fifth_open = False
                elif sixth.collidepoint(pos) and sixth_open:
                    if shape == 1:
                        pygame.draw.circle(window, (0, 0, 0), (450, 275), 50, 5)

                        shape = 0
                        winner[1][2] = 1
                    elif shape == 0:
                        pygame.draw.line(window, (0, 0, 0,), (375, 200), (525, 350), 10)
                        pygame.draw.line(window, (0, 0, 0,), (525, 200), (375, 350), 10)
                        shape = 1
                        winner[1][2] = 2
                    sixth_open = False
                elif seventh.collidepoint(pos) and seventh_open:
                    if shape == 1:
                        pygame.draw.circle(window, (0, 0, 0), (100, 450), 50, 5)
                        shape = 0
                        winner[2][0] = 1
                    elif shape == 0:
                        pygame.draw.line(window, (0, 0, 0,), (25, 375), (175, 525), 10)
                        pygame.draw.line(window, (0, 0, 0,), (175, 375), (25, 525), 10)
                        shape = 1
                        winner[2][0] = 2
                    seventh_open = False
                elif eighth.collidepoint(pos) and eighth_open:
                    if shape == 1:
                        pygame.draw.circle(window, (0, 0, 0), (275, 450), 50, 5)

                        shape = 0
                        winner[2][1] = 1
                    elif shape == 0:
                        pygame.draw.line(window, (0, 0, 0,), (200, 375), (350, 525), 10)
                        pygame.draw.line(window, (0, 0, 0,), (375, 350), (200, 525), 10)
                        shape = 1
                        winner[2][1] = 2

                    eighth_open = False


                elif ninth.collidepoint(pos) and ninth_open:

                    if shape == 1:

                        pygame.draw.circle(window, (0, 0, 0), (450, 450), 50, 5)

                        shape = 0

                        winner[2][1] = 1

                    elif shape == 0:

                        pygame.draw.line(window, (0, 0, 0,), (375, 375), (525, 525), 10)

                        pygame.draw.line(window, (0, 0, 0,), (525, 375), (375, 525), 10)

                        shape = 1

                        winner[2][1] = 2
                    ninth_open = False
# iswinning() equivalent
    if win_check(1):
        text = font.render('O Won', True, green, blue)
        textRect = text.get_rect()
        textRect.center = (275, 275)
        window.fill(white)
        window.blit(text, textRect)
        for event in pygame.event.get():
            won = True
    if win_check(2):
        text = font.render('X Won', True, green, blue)
        textRect = text.get_rect()
        textRect.center = (275, 275)
        window.fill(white)
        window.blit(text, textRect)
        for event in pygame.event.get():
            won = True

pygame.quit()
