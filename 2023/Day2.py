

from typing import Dict, Tuple


def get_possible_games_sum():
    total = 0
    max_balls = {'red': 12, 'green': 13, 'blue': 14}

    with open('Input_Day2.txt', 'r') as fp:
        for line in fp:
            balls_in_game = {}
            line = line.strip()
            is_invalid_game = False
            game_id, Idx = get_game_id(line)
            sets = line[Idx + 2:].split('; ')

            for itr in sets:
                balls = itr.split(', ')

                for ball in balls:
                    count, color = ball.split(' ')
                    count = int(count)

                    if color not in balls_in_game:
                        balls_in_game[color] = count
                    else:
                        balls_in_game[color] = max(balls_in_game[color], count)
            
            total += get_total_power(balls_in_game)
    
    print(f'Total power from playing given games is {total}')


def get_total_power(balls: Dict[str, int]) -> int:
    power = 1
    
    for val in balls.values():
        power *= val
    
    return power


def get_game_id(s: str) -> Tuple[int]:
    num = ''

    for i in range(5, len(s)):
        if s[i] == ':':
            break

        num += s[i]

    return int(num), i


def main():
    get_possible_games_sum()


if __name__ == '__main__':
    main()
