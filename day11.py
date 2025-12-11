import advent_of_code as aoc
import math
import pandas as pd

## TODO 

day = 11

lines = aoc.input_readlines(day, test=True)
lines = aoc.input_readlines(day)

DEBUG = True
DEBUG = False

def find_paths(devices, debug):
    paths_to_check = devices['you']
    paths_to_check = paths_to_check.copy()
    
    if debug:
        print(paths_to_check)
    count_paths = 0
    while paths_to_check != []:
        if debug:
            print(paths_to_check)
            
        path = paths_to_check.pop()
        paths_to_check.extend(devices[path])
        
        if debug:
            print(paths_to_check)
        
        old_paths = paths_to_check.copy()
        paths_to_check.clear()
        for path in old_paths:
            if path == 'out':
                count_paths +=1
            else:
                paths_to_check.append(path)
                
    return count_paths
            
        

def main(lines,debug=DEBUG):

    devices = {}
    for line in lines:
        device, paths_str = line.split(':')
        paths = paths_str.split(' ')
        devices[device] = paths[1:]

    count_paths = find_paths(devices, debug)

    ## Part 1
    part1_answer = count_paths
    print(f'The answer to Part 1: {part1_answer}')
    # Correct answer for Day 11, Part 1: 696
            
    '''
    ## Part 2
    smalldf = df[(df.index % 2 == 1)]
    count_timelines = (smalldf == '|').sum().sum() - 1
    
    part2_answer = count_timelines
    print(f'The answer to Part 2: {part2_answer}')         
    # Correct answer for Day 7, Part 2: 
    # Too low: 3135
    '''
    
    ## TEST AREA
    '''
    print('123'*3)
    '''
        
if __name__ == "__main__":
    main(lines,debug=DEBUG)
    