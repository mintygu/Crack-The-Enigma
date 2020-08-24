import pygame
import pygame_menu
import random
import string

pygame.init()


background_color = (255, 255, 255)
(width, height) = (800, 600)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Crack The Enigma')
screen.fill(background_color)


pygame.display.flip()

def get_random_code(length):
    letter = string.ascii_letters
    result_str = ' '.join(random.choice(letter)for i in range(length))
    print(result_str)
    pass

def set_difficulty(value, difficulty):
    if set_difficulty == 'Easy':
        length = 5
        return length
    pass

def start_the_game():
    get_random_code(length)
    pass

menu = pygame_menu.Menu(512, 384, 'Welcome, Captain',
                       theme=pygame_menu.themes.THEME_DARK)

menu.add_text_input('Name: ', default='Collins')
menu.add_selector('Difficulty: ', [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=set_difficulty)
menu.add_button('Set Sail', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False