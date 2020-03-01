"""Domino Game."""
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
        turn = 'user'
        print('The user have:', [x, x])
        user_tokens.remove([x, x])
        tokens_in_game.append([x, x])
        break
    elif [x, x] in computer_tokens:
        turn = 'computer'
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
                    turn = 'user'
                    print('The user have:', [j, x])
                    loop = False
                    user_tokens.remove([j, x])
                    tokens_in_game.append([j, x])
                    break
                elif [j, x] in computer_tokens:
                    turn = 'computer'
                    print('The computer have:', [j, x])
                    loop = False
                    computer_tokens.remove([j, x])
                    tokens_in_game.append([j, x])
                    break
        x -= 1

print(user_tokens)
print(computer_tokens)
print(tokens_in_game)

game = True

while game:
    if turn == 'user':
        number = int(input('Select the number of token that you want to play'))
    elif turn == 'computer':
        pass
    else:
        pass
