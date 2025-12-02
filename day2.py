import advent_of_code as aoc
import pandas as pd


num = 2

lines = aoc.input_readlines(num, test=True)
lines = aoc.input_readlines(num)

DEBUG = True
DEBUG = False

def process_line(line, debug):
    start, end = line.split('-')
    
    ## PART 1
    
    # Iterate over range, keep track of sum of invalid IDs in count_invalid
    count_invalid = 0
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
                print(f'####### Found an invalid ID: {first_half}')
            count_invalid += int(istr)
            
    return count_invalid
            
    

def main(lines,debug=DEBUG):
    
    ## Part 1
    lines = lines[0].split(',')
    count_invalids = []
    for line in lines:
        #if line != '11-22':
        #    continue
        count_invalid = process_line(line,debug)
        if count_invalid != 0:
            count_invalids.append(count_invalid)
        
            
    part1_answer = sum(count_invalids)
    print(f'The answer to Part 1: {part1_answer}')
        
    ## Part 2

    part2_answer = 'TBD'
    print(f'The answer to Part 2: {part2_answer}')         
    
    ## TEST AREA
    '''
    position, _, counts = turn_dial(50, "R1000") 
    print(position, counts)  
    '''
        
if __name__ == "__main__":
    main(lines,debug=DEBUG)
    