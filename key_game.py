from random import randint
from math import sqrt

GAME_WIDTH = 10
GAME_HEIGHT = 10

key_x = randint(0, GAME_WIDTH)
key_y = randint(0, GAME_HEIGHT)

player_x = 0
player_y = 0
player_found_key = False
steps = 0

distance_before_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

while not player_found_key:
    steps += 1
    print()
    print('You can move in the directions specified as [W/S/A/D]: ')

    move = input("Where do you want to go? ")
    match move.lower():
        case 'w':
            player_y += 1
            if player_y > GAME_HEIGHT:
                print('Aughhh! You hit a wall!')
                player_y = GAME_HEIGHT
                
        case 's':
            player_y -= 1
            if player_y < 0:
                print('Aughhh! You hit a wall!')
                player_y = 0
                
        case 'a':
            player_x -= 1
            if player_x < 0:
                print('Aughhh! You hit a wall!')
                player_x = 0
                
        case 'd':
            player_x += 1
            if player_x > GAME_WIDTH:
                print('Aughhh! You hit a wall!')
                player_x = GAME_WIDTH
                
        case 'q':
            print('Game over!')
            quit()
            
        case '_':
            print(" I don't know where you're going...")
            continue
        
    if player_x == key_x and player_y == key_y:
        print(f'You have found the key in {steps} moves ! ! !')
        quit()
        
    distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)
    
    if distance_before_move > distance_after_move:
        print('Warmer')
    else:
        print('Colder')            

    distance_before_move = distance_after_move
    