from typing import Tuple


def get_total_calibration_digits():
    total = 0
    input_file = "Input_Day1.txt"

    with open(input_file, 'r') as fp:
        for line in fp:
            line = line.strip()
            not_left = not_right = False
            left, right = 0, len(line) - 1

            while left < len(line) and not line[left].isdigit():
                left += 1
            
            while right >= 0 and not line[right].isdigit():
                right -= 1
            
            left_str_idx, l_digit = get_number_string(line)
            right_str_idx, r_digit = get_number_string(line[::-1], True)

            if l_digit != -1 and left_str_idx < left:
                total += 10 * l_digit
                not_left = True
            
            if r_digit != -1 and right_str_idx > right:
                total += r_digit
                not_right = True
            
            if not not_left:
                total += 10 * int(line[left])
            
            if not not_right:
                total += int(line[right])
                
    print(f'Total calibration for the given input is: {total}')


def get_number_string(line: str, reverse: bool = False) -> Tuple[int]:
    left = len(line)
    num = -1
    string_map = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'zero': 0
    }

    for digit in string_map:
        if reverse:
            key = digit[::-1]
        else:
            key = digit
        
        try:
            l = line.index(key)

            if l < left:
                left = l
                num = string_map[key] if not reverse else string_map[key[::-1]]
        except ValueError:
            continue
    
    if reverse:
        left = len(line) - 1 - left
    
    return left, num


def main():
    get_total_calibration_digits()


if __name__ == '__main__':
    main()