import random


def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper , 's' for scissors: \n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Bas basa geldi ;)'

    if is_win(user, computer):
        return 'Qalib!'
    return 'Uduzdunuz!'


def is_win(player, rival):
    if (player == 'r' and rival == 's') or (player == 's' and rival == 'p') \
        or (player == 'p' and rival == 'r'):
        return True

print(play())