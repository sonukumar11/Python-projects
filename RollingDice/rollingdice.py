import random
from termcolor import colored,cprint

def main():
    player1 = 0
    player2 = 0
    rounds = 1
    while rounds != 11:
        cprint("Round : " + str(rounds),'magenta')
        player1Wins = 0
        player2Wins = 0
        player1 = rollDice()
        player2 = rollDice()
        cprint("Player 1 Roll"+ " " + str(player1),'cyan')
        cprint("Player 2 Roll" + " " + str(player2), 'cyan')

        if player1 == player2:
            cprint("Round Drawn..",'red')
        elif player1 > player2:
            cprint("Player 1 Wins the Round..",'red')
            player1Wins += 1
        else:
            cprint("Player 2 wins this Round..",'red')
            player2Wins += 1
        rounds += 1
        print('\n')
    print("\n")
    cprint("********Result of this 10 Round Game is *********",'yellow')
    if player1Wins > player2Wins :
        text = colored("         Player 1 Wins The Game..        ".upper(), 'cyan', attrs=['reverse', 'blink'])
        cprint(text,'red')
    elif player1Wins < player2Wins:
        text = colored("         Player 2 Wins The Game..        ".upper(), 'cyan', attrs=['reverse', 'blink'])
        cprint(text,'red')
    else:
        text = colored("          Game Drawn...          ".upper(), 'cyan', attrs=['reverse', 'blink'])
        cprint(text,'red')


def rollDice():
    roll = random.randint(1,6)
    return roll

text = colored("                  welcome to the Rolling Dice Simulator Game                       ".upper(), 'magenta', attrs=['reverse', 'blink'])
cprint(text)
main()

