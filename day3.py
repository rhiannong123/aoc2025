import advent_of_code as aoc
import math
import pandas as pd


num = 3

lines = aoc.input_readlines(num, test=True)
lines = aoc.input_readlines(num)

DEBUG = True
DEBUG = False

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
        print("\n\n")
        print('Line to start: ', line)

    
    # Loop over indeces 13 to last
    #   Add the next digit to the end of current_best (test_line)
    #   build a list (possibles) that has strings with removing a digit at each index of test_line
    #   convert that list of strings to ints
    #   is the max of that list greater than current best? set to current best
    current_best = line[:12]
    if debug:
        print('')   
        print(current_best)
    for test_idx in range(12,len(line)):
        
        test_line = current_best + line[test_idx]
        possibles = []
        if debug:
            print('')
            print(test_line)
        for idx in range(0,len(line[:12])):
            s = test_line[:idx] + test_line[idx+1:]
            if debug:
                print(s)
            possibles.append(s)
        
        possibles_ints = list(map(int, possibles))
        
        current_best = str(max(int(current_best), max(possibles_ints)))
        
        
    max_joltage = int(current_best)
    
    if debug:
        print('###  ', max_joltage)

    return int(max_joltage)



def main(lines,debug=DEBUG):

    ## Part 1

    max_joltages = []
    for line in lines:
        max_joltages.append(process_line_part1(line,debug))
        
    part1_answer = sum(max_joltages)
    print(f'The answer to Part 1: {part1_answer}')
    # Correct answer for Day 3, Part 1: 17196
    
    
    ## Part 2

    max_joltages = []
    for line in lines:
        max_joltages.append(process_line_part2(line,debug))
        
    part2_answer = sum(max_joltages)
    print(f'The answer to Part 2: {part2_answer}')
    # Correct answer for Day 3, Part 2: 171039099596062
    # too low: 159618812449192 
    
    ## TEST AREA
    '''
    print('123'*3)
    '''
        
if __name__ == "__main__":
    main(lines,debug=DEBUG)
    