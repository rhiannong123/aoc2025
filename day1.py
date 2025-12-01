import advent_of_code as aoc

import pandas as pd


## PART 1
num = 1
#lines = aoc.input_readlines(num, test=True)
lines = aoc.input_readlines(num)

position = 50
print(lines)

def turn_dial(initial, line):
    '''
    initial - initial position
    line - example "L54", "R3"
    '''
    l_or_r = line[0]
    increment = int(line[1:])
    
    if l_or_r == 'L':
        end_actual = initial - increment 
        while end_actual < 0:
            end_actual += 100
    else:
        end_actual = initial + increment
        while end_actual > 99:
            end_actual -= 100
            
    if end_actual == 0:
        end_at_zero = True
    else:
        end_at_zero = False

            
    print(initial, line, end_actual, end_at_zero)
    return end_actual, end_at_zero
            
def main(lines, position):
    
    ## Part 1
    end_at_zero_sum = 0
    for line in lines:
        position, end_at_zero = turn_dial(position, line)
        if end_at_zero:
            end_at_zero_sum += 1
            
    part1_answer = end_at_zero_sum
    print(f'The answer to Part 1: {part1_answer}')
        
        
if __name__ == "__main__":
    main(lines, position)
    