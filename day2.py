import advent_of_code as aoc
import math
import pandas as pd


num = 2

lines = aoc.input_readlines(num, test=True)
lines = aoc.input_readlines(num)

DEBUG = True
DEBUG = False

def process_line(line, part, debug):
    '''
    Inputs
      line: entry to look at, form of 2 integers with a hyphen, example 11-22
      part: 1 or 2, of puzzle
      debug: True or False 
    
    '''
    
    start, end = line.split('-')
    invalid_ids = []
    
    ## PART 1
    if part == 1:
        # Iterate over range, keep track of invalid IDs (list: invalid_ids)
        for i in range(int(start), int(end)+1):
            istr = str(i)
            if len(istr) % 2 != 0:
                # length of istr is odd - can't be repeat sequence - don't care
                continue
            half_length = int(len(istr) / 2)
            first_half = istr[:half_length]
            second_half = istr[half_length:]
            if debug:
                print(f'ID of {istr}, has a first half of {first_half}, second half of {second_half}')
            # Check if first half of ID matches second, if yes, it's invalid, keep track of sum
            if first_half == second_half:
                if debug:
                    print(f'####### Found an invalid ID: {istr}')
                invalid_ids.append(i)
                
                
    ## PART 2
    if part == 2:
        # Iterate over range, keep track of invalid IDs (list: invalid_ids)
        for i in range(int(start), int(end)+1):
            # Define current_i_invalid - to use when j loop finds an invalid id
            current_i_invalid = False
            if debug:
                print(f'ID to check: {i}')
            if i in invalid_ids:
                # i is already known to be invalid, continue
                continue
            
            # Iterate over length of substring, starting with substring length 1 to half_length (rounded down)
            #  (substrings longer than half_length can't be repeated in length of string)
            istr = str(i)
            half_length = math.floor(float(len(istr) / 2))
            for j in range(1, half_length+1):
                if current_i_invalid:
                    # Current i already known to be invalid, skip the rest of this loop
                    continue
                if len(istr) % j != 0:
                    # If current substring length isn't a divisor of istr - can't have a repeat pattern, skip
                    continue
                
                num_of_repeats = int(len(istr) / j)
                pattern_to_check = istr[:j] * num_of_repeats
                
                if istr == pattern_to_check:
                    # Found an invalid ID
                    invalid_ids.append(i)
                    if debug:
                        print(f'####### Found an invalid ID: {istr}')
                    current_i_invalid = True
            
    return sum(invalid_ids)
            
    

def main(lines,debug=DEBUG):

    lines = lines[0].split(',')
    
    ## Part 1
    count_invalids = []
    part = 1
    
    for line in lines:
        count_invalid = process_line(line,part,debug)
        if count_invalid != 0:
            count_invalids.append(count_invalid)
        
    part1_answer = sum(count_invalids)
    print(f'The answer to Part 1: {part1_answer}')
    # Correct answer for Day 2, Part 1: 13108371860
    
    ## Part 2
    count_invalids = []
    part = 2
    
    for line in lines:
        #if line != '11-22':
        #    continue
        count_invalid = process_line(line,part,debug)
        if count_invalid != 0:
            count_invalids.append(count_invalid)

    part2_answer = sum(count_invalids)
    print(f'The answer to Part 2: {part2_answer}')         
    # Correct answer for Day 2, Part 2: 22471660255
    
    ## TEST AREA
    '''
    print('123'*3)
    '''
        
if __name__ == "__main__":
    main(lines,debug=DEBUG)
    