"""Domino Game."""
import time
import random as rd

tokens = [
    # Zeros
    [0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6],
    # Ones
    [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
    # Twos
    [2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
    # Threes
    [3, 3], [3, 4], [3, 5], [3, 6],
    # Fours
    [4, 4], [4, 5], [4, 6],
    # Fives
    [5, 5], [5, 6],
    # Sixs
    [6, 6],
]

tokens_in_game = []

user_tokens = []
computer_tokens = []

tie = [0, 0]

for x in range(7):
    # Give a token to the user
    token_index = int(rd.random() * len(tokens))
    user_tokens.append(tokens[token_index])
    tokens.remove(tokens[token_index])

    # Give a token to the computer
    token_index = int(rd.random() * len(tokens))
    computer_tokens.append(tokens[token_index])
    tokens.remove(tokens[token_index])

print('The user´s tokens:', user_tokens)
print('The computer´s tokens:', computer_tokens)

# Look from who is the first turn
for x in reversed(range(7)):
    if [x, x] in user_tokens:
        turn = 'computer'
        print('The user have:', [x, x])
        user_tokens.remove([x, x])
        tokens_in_game.append([x, x])
        break
    elif [x, x] in computer_tokens:
        turn = 'user'
        print('The computer have:', [x, x])
        computer_tokens.remove([x, x])
        tokens_in_game.append([x, x])
        break
else:
    loop = True
    x = 6
    while loop:
        for j in reversed(range(x)):
            if x != j:
                if [j, x] in user_tokens:
                    turn = 'computer'
                    print('The user have:', [j, x])
                    loop = False
                    user_tokens.remove([j, x])
                    tokens_in_game.append([j, x])
                    break
                elif [j, x] in computer_tokens:
                    turn = 'user'
                    print('The computer have:', [j, x])
                    loop = False
                    computer_tokens.remove([j, x])
                    tokens_in_game.append([j, x])
                    break
        x -= 1

game = True

while game:

    print(tokens_in_game, '\n')

    # Check the numbers in the limits
    start_number = tokens_in_game[0][0]
    final_number = tokens_in_game[-1][-1]

    time.sleep(3)

    if tie == [1, 1]:
        game = False
        print('Juego empatado')
    elif turn == 'user':

        # Validate that the user have a token to play.
        for user_token in user_tokens:
            if (start_number in user_token) or (final_number in user_token):
                user_loop = True
                break
        else:
            print('Your tokens:', user_tokens)
            print('You don´t have tokens to play')
            while (start_number not in user_token) and (final_number not in user_token):
                try:
                    token_index = int(rd.random() * len(tokens))
                    user_token = tokens[token_index]
                    user_tokens.append(tokens[token_index])
                    tokens.remove(tokens[token_index])
                    print('Your new token:', user_token)
                    time.sleep(1)
                    user_loop = True
                except:
                    tie[0] = 1
                    user_loop = False
                    break

        while user_loop:
            print('Your tokens:', user_tokens)
            number = int(input('Select the number of token that you want to play: '))
            user_token = user_tokens[number]
            if (start_number in user_token) or (final_number in user_token):
                user_loop = False
                if start_number in user_token:
                    print('Start', user_token)
                    user_tokens.remove(user_token)
                    if user_token[0] == start_number:
                        tokens_in_game.insert(0, [user_token[1], user_token[0]])
                    else:
                        tokens_in_game.insert(0, user_token)
                    tie[0] = 0
                elif final_number in user_token:
                    print('Final', user_token)
                    user_tokens.remove(user_token)
                    if user_token[0] == final_number:
                        tokens_in_game.append(user_token)
                    else:
                        tokens_in_game.append([user_token[1], user_token[0]])
                    tie[0] = 0
            else:
                print('Please select another token that you can play')

        if len(user_tokens) == 0:
            game = False
            print('User wins')

        turn = 'computer'

    elif turn == 'computer':
        print('The computer´s tokens:', computer_tokens)

        time.sleep(3)

        for computer_token in computer_tokens:
            if start_number in computer_token:
                print('Start', computer_token)
                computer_tokens.remove(computer_token)
                if computer_token[0] == start_number:
                    tokens_in_game.insert(0, [computer_token[1], computer_token[0]])
                else:
                    tokens_in_game.insert(0, computer_token)
                tie[1] = 0
                break
            elif final_number in computer_token:
                print('Final', computer_token)
                computer_tokens.remove(computer_token)
                if computer_token[0] == final_number:
                    tokens_in_game.append(computer_token)
                else:
                    tokens_in_game.append([computer_token[1], computer_token[0]])
                tie[1] = 0
                break
        else:
            try:
                while (start_number not in computer_token) or (final_number not in computer_token):
                    # Give a token to the computer
                    token_index = int(rd.random() * len(tokens))
                    computer_token = tokens[token_index]
                    computer_tokens.append(tokens[token_index])
                    tokens.remove(tokens[token_index])
                    print('Computer new token:', computer_token)
                    time.sleep(1)
                    if start_number in computer_token:
                        print('Start', computer_token)
                        computer_tokens.remove(computer_token)
                        if computer_token[0] == start_number:
                            tokens_in_game.insert(0, [computer_token[1], computer_token[0]])
                        else:
                            tokens_in_game.insert(0, computer_token)
                        tie[1] = 0
                        break
                    elif final_number in computer_token:
                        print('Final', computer_token)
                        computer_tokens.remove(computer_token)
                        if computer_token[0] == final_number:
                            tokens_in_game.append(computer_token)
                        else:
                            tokens_in_game.append([computer_token[1], computer_token[0]])
                        tie[1] = 0
                        break
            except:
                tie[1] = 1

        if len(computer_tokens) == 0:
            game = False
            print('Computer wins')

        turn = 'user'
