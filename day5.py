import advent_of_code as aoc
import math
import pandas as pd

## TODO 

day = 5

lines = aoc.input_readlines(day, test=True)
lines = aoc.input_readlines(day)

DEBUG = True
DEBUG = False


def process_lines(lines, debug):
    ranges = []
    ids = []
    for line in lines:
        if line == '':
            continue    
    
        if '-' in line:
            start,end = line.split('-')
            start = int(start)
            end = int(end)
            ranges.append([start,end])
        else:
            ids.append(int(line))
            
    return ranges, ids
        
def check_if_id_fresh(test_id, ranges, debug):
    
    if debug:
        print()
        print(f'Fresh ID to check: {test_id}')
    
    for irange in ranges:
        if debug:
            print(f'Checking if {test_id} in {irange}. ')
        start = irange[0]
        end = irange[1]
        if (test_id <= end) & (test_id >= start):
            if debug:
                print('  True')
            return True
        else:
            if debug:
                print('  False')
            
    return False
    
    
def count_all_fresh_ids(ranges, debug):
    
    #ranges=[[3,5],[10,14],[16,20],[12,18]]
    
    starts = []
    ends = []
    for irange in ranges:
        current_start = irange[0]
        current_end = irange[1]
        
        if starts == []:
            starts.append(current_start)
            ends.append(current_end)
            continue
        
        if all(current_end < x for x in starts):
            # current end is less than all intervals, save this interval and continue
            starts.append(current_start)
            ends.append(current_end)
            continue
        
        if all(current_start > x for x in ends):
            # current start is > than all intervals, save this one and continue
            starts.append(current_start)
            ends.append(current_end)
            continue
        
        idx = -1
        for x,y in zip(starts,ends):
            idx += 1
            if (current_start >= x) & (current_start < y) & (current_end > y):
                ends[idx] = current_end
            if (current_start < x) & (current_end >= x) & (current_end < y):
                starts[idx] = current_start
    print(starts)
    print(ends)
    print('next')
    
    # Intervals likely overlap. Need to fix
    for idxi in range(len(starts)):
        idx_to_drop = []
        for start,end in zip(starts,ends):
            if (starts[idxi] < end) & (starts[idxi] > start):
                print( start, end,  starts[idxi])
                starts[idxi] = end+1
                if starts[idxi] > ends[idxi]:
                    idx_to_drop.append(idxi)
    starts = [x for i, x in enumerate(starts) if i not in idx_to_drop]
    ends = [x for i, x in enumerate(ends) if i not in idx_to_drop]
    
    print(starts)
    print(ends)
    
    counts = []
    for idxi in range(len(starts)):
        counts.append(len(range(starts[idxi],ends[idxi])) + 1)
                    
    return counts
        

            
            
            
            
                



def main(lines,debug=DEBUG):

    ranges, ids = process_lines(lines, debug)
    
    '''
    ## Part 1
    count_fresh = 0
    for test_id in ids:
        if check_if_id_fresh(test_id, ranges, debug):
            count_fresh += 1
                    
    part1_answer = count_fresh
    print(f'The answer to Part 1: {part1_answer}')
    # Correct answer for Day 5, Part 1: 862
        
    '''        
    ## Part 2
    
    counts = count_all_fresh_ids(ranges, debug)
    
    part2_answer = sum(counts)
    print(f'The answer to Part 2: {part2_answer}')         
    # Correct answer for Day 4, Part 2: 7922
    # Too low: 18687927624810 
    
    
    ## TEST AREA
    '''
    print('123'*3)
    '''
        
if __name__ == "__main__":
    main(lines,debug=DEBUG)
    