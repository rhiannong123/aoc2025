import advent_of_code as aoc

import pandas as pd


## PART 1
num = 1
#lines = aoc.input_readlines(num, test=True)
lines = aoc.input_readlines(num)

STARTING_POSITION = 50

def turn_dial(initial, line):
    '''
    initial - initial position
    line - example "L54", "R3"
    '''
    l_or_r = line[0]
    increment = int(line[1:])
    
    if initial == 0:
        start_at_zero = True
        first_time_in_while_flag = 1
    else:
        start_at_zero = False
        first_time_in_while_flag = 1

    count_num_of_zero_crossings = 0
        
    if l_or_r == 'L':
        end_actual = initial - increment 
        while end_actual < 0:
            end_actual += 100
            count_num_of_zero_crossings += 1
            if (start_at_zero == True) & (first_time_in_while_flag == 1):
                first_time_in_while_flag = 0
                count_num_of_zero_crossings -= 1
    else:
        end_actual = initial + increment
        while end_actual > 99:
            end_actual -= 100
            count_num_of_zero_crossings += 1
            
    if end_actual == 0:
        if l_or_r == 'L':
            count_num_of_zero_crossings += 1
        end_at_zero = True
    else:
        end_at_zero = False

    print(f"Initial position of {initial} with command {line} results in end position of {end_actual} and number of zero crossings of {count_num_of_zero_crossings}")
    
    return end_actual, end_at_zero, count_num_of_zero_crossings
            
def main(lines):
    
    ## Part 1
    position = STARTING_POSITION
    end_at_zero_sum = 0
    for line in lines:
        position, end_at_zero, _ = turn_dial(position, line)
        if end_at_zero:
            end_at_zero_sum += 1
            
    part1_answer = end_at_zero_sum
    print(f'The answer to Part 1: {part1_answer}')
        
    ## Part 2
    position = STARTING_POSITION
    nonzero_zero_crossings = []
    for line in lines:
        position, _, counts = turn_dial(position, line)
        if counts > 0:
            nonzero_zero_crossings.append(counts)
            
    part2_answer = sum(nonzero_zero_crossings)
    print(f'The answer to Part 2: {part2_answer}')         
    
    ## TEST AREA
    '''
    position, _, counts = turn_dial(50, "R1000") 
    print(position, counts)  
    '''
        
if __name__ == "__main__":
    main(lines)
    