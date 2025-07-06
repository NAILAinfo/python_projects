import random

playing = True
count = 0
while playing:
    r = input('Roll the dice ? (y/n) : ').lower() 
    if r == 'y': 
        e = int(input('hom muche dice you want to roll ? :'))
        if e < 0 : 
            print('Please enter a positive number of dice.')
            continue
        results = [random.randint(1, 6) for _ in range(e)]
        print(f'You rolled: {results}')
        count += 1
        print(f'Total rolls so far: {count}')
    elif r == 'n':
        print('Thanks for playing!')
        print(f'Total rolls made: {count}')
        playing = False
    else:
        print('Invalid input, please enter y or n.')
