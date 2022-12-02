

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
    move = {'A X': 'C',
            'A Y': 'A',
            'A Z': 'B',

            'B X': 'A',
            'B Y': 'B',
            'B Z': 'C',

            'C X': 'B',
            'C Y': 'C',
            'C Z': 'A',
            }
    win_loss = {'Z': 6,
                'Y': 3,
                'X': 0}

    translate = {'A': 'X',
                 'B': 'Y',
                 'C': 'Z'}

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
        action = move[game]

        # print(action, translate[action], points[translate[action]])
        action_points = points[translate[action]]
        win_loss_points = win_loss[game[-1]]

        # Sum the points
        game_points = action_points + win_loss_points

        score2 += game_points

        if debug:
            print(f'2: {game} - {game[-1]}  - {action} - Type: {action_points} - Game: {win_loss_points} - Score: {game_points}\n')

    # Part 2

    print(f'\tDay 02')
    print(f'\t\tPart 1: Tournament score {score}')
    print(f'\t\tPart 2: Tournament score {score2}\n')

    return score, score2
