import advent_of_code as aoc
import pandas as pd


num = 2
lines = aoc.input_readlines(num, test=True)
#lines = aoc.input_readlines(num)

STARTING_POSITION = 50

            
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
    