import random


def rock_paper_scissors():
    game = ['R', 'P', 'S']
    pick = random.choice(game)
    prompt = input('R, P or S ?? \n')
    print('I Guessed:', pick)
    win = 'I WIN'
    lose = 'YOU WIN'
    if prompt == "R":
        if pick == 'R':
            print('we have a draw')
        elif pick == 'P':
            return win
        elif pick == 'S':
            return lose
    elif prompt == 'P':
        if pick == 'R':
            return lose
        elif pick == 'P':
            print('we have a draw')
        elif pick == 'S':
            return win
    elif prompt == 'S':
        if pick == 'R':
            return win
        elif pick == 'P':
            return lose
        elif pick == 'S':
            print('we have a draw')
    while prompt not in game:
        print('R, P or S Please!!!')
        return rock_paper_scissors()
    if prompt == pick:
        return rock_paper_scissors()


print(rock_paper_scissors())
