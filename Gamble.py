import random

def gamble():

    x = int(input('choose  1 or 2: '))

    money = int(5000)
    
    print('you have: ', money)

    bet = int(input('How much would you like to bet?, you have: '))

    y = int(random.randint(1,2))

    if x == y:
        print('you picked:', x, 'You win, Computer picked:',y)
        winnings = money + bet
        print('you won: ', winnings)

    else:
        print('you picked:', x, 'You lose, Computer picked:',y)
        winnings = money - bet
        print('you won: ', winnings)

    gamble()

gamble()