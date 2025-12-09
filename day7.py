import advent_of_code as aoc
import math
import pandas as pd

## TODO 

day = 7

lines = aoc.input_readlines(day, test=True)
lines = aoc.input_readlines(day)

DEBUG = True
DEBUG = False

def process_df(df,debug):
    
    # Find where S is in top row
    col_with_s = list(df.columns[df.loc[0,:] == 'S'])[0]
    
    # Propogate beam in next row:
    df.iloc[1,col_with_s] = '|'
    
    cols_with_beam = [col_with_s]
    count_beam_splits = 0
    for idx in df.index[2:]:
        if debug:
            print('Processing row: ', idx)
            
        if idx % 2 == 0:
            # row with splitter
            cols_with_splitter = list(df.columns[df.loc[idx,:] == '^'])
            if debug:
                print('cols_with_beam', cols_with_beam)
                print('cols_with_splitter: ', cols_with_splitter)
            
            # check if beam meets splitter
            splitter_found = []
            for ibeam in cols_with_beam:
                for icolsplit in cols_with_splitter:
                    if ibeam == icolsplit:
                        splitter_found.append(ibeam)
                        
            for splitter in splitter_found:
                # beam meets splitter, split it on either side 
                # Update cols_with_beam to exclude location at splitter, and add the locs on either side
                count_beam_splits +=1
                cols_with_beam.remove(splitter)
                if splitter-1 not in cols_with_beam:
                    cols_with_beam.append(splitter-1)
                if splitter+1 not in cols_with_beam:
                    cols_with_beam.append(splitter+1)

            df.loc[idx,cols_with_beam] = '|'
        else:
            # row w/o splitter - only .'s; propogate beam
            df.loc[idx,cols_with_beam] = '|'
            
        if debug:
            print(df)
        
    return df, count_beam_splits

def main(lines,debug=DEBUG):

    rows = [list(line) for line in lines]
    df = pd.DataFrame(rows)
    
    if debug:
        print(df)

    df, count_beam_splits = process_df(df, debug)


    ## Part 1
    part1_answer = count_beam_splits
    print(f'The answer to Part 1: {part1_answer}')
    # Correct answer for Day 7, Part 1: 1562
        
        
    ## Part 2
    smalldf = df[(df.index % 2 == 1)]
    count_timelines = (smalldf == '|').sum().sum() - 1
    
    part2_answer = count_timelines
    print(f'The answer to Part 2: {part2_answer}')         
    # Correct answer for Day 7, Part 2: 
    # Too low: 3135
    
    
    ## TEST AREA
    '''
    print('123'*3)
    '''
        
if __name__ == "__main__":
    main(lines,debug=DEBUG)
    