LETTER_TO_HAND = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

HAND_TO_SCORE = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

def calculate_result(hand1, hand2):
    play_score = 0
    
    if hand1 == hand2:
        play_score = 3
    elif hand1 == 'rock' and hand2 == 'paper':
        play_score = 0
    elif hand1 == 'rock' and hand2 == 'scissors':
        play_score = 6
    elif hand1 == 'paper' and hand2 == 'scissors':
        play_score = 0
    elif hand1 == 'paper' and hand2 == 'rock':
        play_score = 6
    elif hand1 == 'scissors' and hand2 == 'rock':
        play_score = 0
    elif hand1 == 'scissors' and hand2 == 'paper':
        play_score = 6

    return play_score + HAND_TO_SCORE[hand1]

def read_strategy(filename='day2.txt'):
    strategy = []

    with open(filename, 'r') as f:
        for line in f:
            h2, h1 = line.strip().split(' ')
            strategy.append([LETTER_TO_HAND[h1], LETTER_TO_HAND[h2]])
    
    return strategy


def use_strategy(strategy):
    score = 0

    for [h1, h2] in strategy:
        score += calculate_result(h1, h2)

    return score


if __name__ == '__main__':
    strategy = read_strategy()
    score = use_strategy(strategy)
    print(score)
            