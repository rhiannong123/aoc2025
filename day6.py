import advent_of_code as aoc
import math
import pandas as pd

## TODO 

day = 6

lines = aoc.input_readlines(day, test=True)
lines = aoc.input_readlines(day)

DEBUG = True
#DEBUG = False

def process_df(df,debug):
    
    solutions = []
    for icol in df.columns:
        if df.iloc[-1,icol] == '+':
            solution = df.iloc[:-1,icol].sum()
        else:
            solution = df.iloc[:-1,icol].product()
        if debug:
            print(solution)
        solutions.append(solution)
        
    return solutions

def main(lines,debug=DEBUG):

    rows = [s.split() for s in lines]
    df = pd.DataFrame(rows)
    for idx in df.index:
        if idx == df.shape[0]-1:
            continue
        df.loc[idx,:] = pd.to_numeric(df.loc[idx,:])

    ## Part 1
    solutions = process_df(df,debug)
                    
    part1_answer = sum(solutions)
    print(f'The answer to Part 1: {part1_answer}')
    # Correct answer for Day 6, Part 1: 4693159084994
        
        
    ## Part 2
    
    
    part2_answer = 2
    print(f'The answer to Part 2: {part2_answer}')         
    # Correct answer for Day 4, Part 2: 7922
    # Too low: 18687927624810 
    
    
    ## TEST AREA
    '''
    print('123'*3)
    '''
        
if __name__ == "__main__":
    main(lines,debug=DEBUG)
    