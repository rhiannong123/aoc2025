import advent_of_code as aoc
import math
import pandas as pd

## TODO 

day = 7

lines = aoc.input_readlines(day, test=True)
#lines = aoc.input_readlines(day)

DEBUG = True
#DEBUG = False

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


def count_timelines(df, debug):

    # Add a column that is indeces with beams in it
    beam_idxs = []    
    for idx in df.index:
        current_row_list = df.iloc[idx,:].to_list()
        beam_idxs.append([i for i, val in enumerate(current_row_list) if val == '|'])
    
    df['beam_idxs'] = beam_idxs
    
    # Explore path from last row
    # starting in middle for more interesting case

    current_idx = 16
    paths_to_check = [[[current_idx,4]]]
    no_splits_path = []
    while current_idx > 0:
        current_idx -= 1
        # FOR ODD ROWS:
        if current_idx % 2 == 1:
            new_paths_to_check = []
            for path in paths_to_check:
                last_step = path[-1]
                current_col = last_step[1]
                if current_col - 1 in df.columns:
                    if df.iloc[current_idx,current_col - 1] == '|':
                        new_path = path.copy()
                        new_path.append([current_idx,current_col - 1])
                        if new_path not in new_paths_to_check:
                            new_paths_to_check.append(new_path)
                if current_col + 1 in df.columns:
                    if df.iloc[current_idx,current_col + 1] == '|':
                        new_path = path.copy()
                        new_path.append([current_idx,current_col + 1])
                        if new_path not in new_paths_to_check:
                            new_paths_to_check.append(new_path)

                if df.iloc[current_idx,current_col] == '|':
                    new_path = path.copy()
                    new_path.append([current_idx,current_col])
                    if new_path not in new_paths_to_check:
                        new_paths_to_check.append(new_path)
                    if new_path not in no_splits_path:
                        no_splits_path.append(new_path)
                    
            paths_to_check = new_paths_to_check.copy()


                    
                     
    
    
        
    last_row_list = df.iloc[-1,:].to_list()
    beams_in_last_row = [i for i, val in enumerate(last_row_list) if val == '|']

    idx = beams_in_last_row[0]
    


    return 1


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
    count_timelines = count_timelines(df, debug)
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
    