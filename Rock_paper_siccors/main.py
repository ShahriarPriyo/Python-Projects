import random

def play():
    user=input("'r' for rock , 'p' for paper , 's' for siccors\n")
    computer=random.choice(['r','p','s'])

    if user == computer:
        return 'it is a tie'
     

    if is_win(user,computer):
        return 'you won!'
     

    return 'computer won' 
    #no need for logic , the only logic left

def is_win(player,opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())