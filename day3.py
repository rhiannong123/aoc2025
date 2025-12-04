import advent_of_code as aoc
import math
import pandas as pd


num = 3

lines = aoc.input_readlines(num, test=True)
#lines = aoc.input_readlines(num)

DEBUG = True
#DEBUG = False

NUM_OF_BATTERIES = 12

def process_line_part1(line, debug):
    
    sort_descend = sorted(line,reverse=True)
    max_digit_str = sort_descend[0]
    idx_max = line.find(max_digit_str)
    
    if idx_max == 0:
        # largest number is first digit, combine it with the next largest digit, done
        max_joltage = int(sort_descend[0] + sort_descend[1])
        if debug:
            print('Largest digit is first digit, found largest jolt')
            print(f'### max joltage for {line} is {max_joltage}. ')
    else:
        digits_to_check = list(range(9, 0, -1))
        
        found_max_joltage = False
        for idigit in digits_to_check:
            if found_max_joltage:
                continue
            
            idx_max_test = line.find(str(idigit))
            if idx_max_test == -1:
                # digit not found in remaining string
                continue
            if idx_max_test == len(line) - 1:
                # largest digit is last digit, this is not going to make max joltage
                continue
            else:
                # found max largest digit, it is not the first or last. Get the largest digit after max largest digit
                substring = line[idx_max_test+1:]
                substring_sort_descend = sorted(substring,reverse=True)
                max_joltage = int(str(idigit) + substring_sort_descend[0])
                if debug:
                    print(f'### max joltage for {line} is {max_joltage}. ')
                found_max_joltage = True

    return max_joltage
    


def process_line_part2(line, debug):
    
    digits = range(1,10)
    continue_on = True
    
    if debug: 
        print("")
        print('1: ', line)
    
    for idigit in digits:
        if continue_on == 0:
            continue
        substring = line.replace(str(idigit),"")
        if debug:
            print('substring: ', substring)
        
        if len(substring) > 12:
            # Keep going, Remove idigit and keep testing
            if debug:
                print(line)
            line = substring
        else:
            continue_on = 0
            lowest_idigit = idigit
            substring_length = len(substring)
                
    print('post for loop:', line)
    print(lowest_idigit)
    print(substring_length)
    number_to_keep = NUM_OF_BATTERIES - substring_length
    positions = [idx for idx, c in enumerate(line) if c == str(lowest_idigit)]

    # Keep only last 5 zeros
    keep = set(positions[-number_to_keep:])

    # Build new string keeping non-zeros + last 5 zeros
    max_joltage = "".join(c for i, c in enumerate(line) if c != str(lowest_idigit) or i in keep)
    
    if debug:
        print('###  ', max_joltage)

    return int(max_joltage)



def main(lines,debug=DEBUG):

    ## Part 1

    '''
    max_joltages = []
    for line in lines:
        max_joltages.append(process_line_part1(line,debug))
        
    part1_answer = sum(max_joltages)
    print(f'The answer to Part 1: {part1_answer}')
    # Correct answer for Day 3, Part 1: 17196
    '''
    
    ## Part 2

    max_joltages = []
    for line in lines:
        max_joltages.append(process_line_part2(line,debug))
        
    part2_answer = sum(max_joltages)
    print(f'The answer to Part 2: {part2_answer}')
    # Correct answer for Day 3, Part 2: 17196
    
    ## TEST AREA
    '''
    print('123'*3)
    '''
        
if __name__ == "__main__":
    main(lines,debug=DEBUG)
    