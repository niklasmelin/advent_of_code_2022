

def day_02(data, debug=False):

    # A X - Rock
    # B Y - Paper
    # C Z - Scissors
    outcomes = {'A X': 'D',
                'A Y': 'W',
                'A Z': 'L',

                'B X': 'L',
                'B Y': 'D',
                'B Z': 'W',

                'C X': 'W',
                'C Y': 'L',
                'C Z': 'D',
                }

    # A - Rock
    # B - Paper
    # C - Scissors
    # X - Lose
    # Y - Draw
    # Z - Win
    move = {'A X': 'Z',
            'A Y': 'X',
            'A Z': 'Y',

            'B X': 'X',
            'B Y': 'Y',
            'B Z': 'Z',

            'C X': 'Y',
            'C Y': 'Z',
            'C Z': 'X',
            }

    points = {'X': 1,
              'Y': 2,
              'Z': 3,

              'W': 6,
              'D': 3,
              'L': 0}

    score = 0
    score2 = 0
    for line in data:
        # Part 1
        game = line.strip()
        choice = game[-1]

        # Get winner
        outcome = outcomes[game]

        # Sum the points
        game_points = points[choice] + points[outcome]
        score += game_points

        if debug:
            print(f'1: {game} - {outcome} - Type: {points[choice]} - Game: {points[outcome]} - Score: {game_points}')

        # Part 2
        # Get require selection
        selection = move[game]
        outcome = outcomes[f'{game[0]} {selection}']

        # Sum the points
        game_points = points[selection] + points[outcome]
        score2 += game_points

    # Part 2

    print(f'\tDay 02')
    print(f'\t\tPart 1: Tournament score {score}')
    print(f'\t\tPart 2: Tournament score {score2}\n')

    return score, score2
