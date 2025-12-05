import advent_of_code as aoc
import math
import pandas as pd

## TODO 
## If I had more time - I would use find_forkliftable_count in remove_forkliftable function
## I would only check positions that contain a '@' - use the power of dataframes 

day = 4

lines = aoc.input_readlines(day, test=True)
lines = aoc.input_readlines(day)

DEBUG = True
DEBUG = False

def get_spaces_around(df,irow,icol):
    # get 3 in column before icol
    # get 3 in column after icol
    # get 1 above
    # get 1 below
    around = df.iloc[irow-1:irow+2, icol-1].to_list()
    around.extend(df.iloc[irow-1:irow+2, icol+1].to_list())
    around.append(df.iloc[irow-1,icol])
    around.append(df.iloc[irow+1,icol])
    
    return around

def is_it_forkliftable(around):
    return around.count('@') < 4
    

def find_forkliftable_count(df, debug):
    '''
    Part 1
    Inputs
    
    Outputs:
    '''
    
    forkliftable_count = 0
    # Iterate over every position in df
    #  if position is not a @, skip - it's not a roll
    #  count number of @'s around that position, add 1 to count if forkliftable (# of rolls around < 4)
    for irow in df.index[1:]:
        for icol in range(len(df.columns[1:])):
            
            if df.iloc[irow,icol] != '@':
                # not a roll, don't care
                continue
            
            # Check spaces all around
            around = get_spaces_around(df,irow,icol)
            
            # if count around is less than 4, it's forkliftable!
            if is_it_forkliftable(around):
                if debug:
                    print('###  ', irow, icol)
                forkliftable_count += 1
                
    return forkliftable_count
            
def remove_forkliftable(df, debug):
    '''
    Part 2
    Inputs
    
    Outputs:
    '''

    # Each round iterate over each position in df
    # Each round determine which positions are forkliftable
    #  then at the end of each round, switch forkliftable ones to an 'x'
    # Once there is a round where nothing gets removed, exit while loop
    continue_on = True
    while continue_on:
    
        forkliftable_count = 0
        list_of_tuples = []
        for irow in df.index[1:]:
            for icol in range(len(df.columns[1:])):
                
                if df.iloc[irow,icol] != '@':
                    # not a roll, don't care
                    continue
                
                # Check spaces all around
                around = get_spaces_around(df,irow,icol)
                
                #if debug:
                #    print(irow, icol, around)
                    
                # if count around is less than 4, it's forkliftable!
                if is_it_forkliftable(around):
                    #if debug:
                    #    print('###  ', irow, icol)
                    forkliftable_count += 1
                    list_of_tuples.append((irow, icol))
                    
        for ituple in list_of_tuples:
            df.iloc[ituple[0], ituple[1]] = 'x' 
                
        if debug:
            print(f'This iteration we removed this many rolls: ', forkliftable_count)
        if debug:
            print(df)
            
        if forkliftable_count == 0:
            continue_on = False
                    
                    
                    
    return df

def main(lines,debug=DEBUG):

    rows = [list(line) for line in lines]
    df = pd.DataFrame(rows)
    
    # Padding df with a border - adds computation time but makes logic easier
    ncols = df.shape[1]
    top_bottom = pd.DataFrame([["!"] * ncols])
    df = pd.concat([top_bottom, df, top_bottom], ignore_index=True)
    df.insert(0, "left", "!")
    df["right"] = "!"
    df.columns = range(0,len(df.columns))
    
    
    ## Part 1
    forkliftable_count = find_forkliftable_count(df, debug)     

    part1_answer = forkliftable_count
    print(f'The answer to Part 1: {part1_answer}')
    # Correct answer for Day 4, Part 1: 1372
        
        
    ## Part 2
    # Turn all forkliftable '@' into 'x's
    dfnew = remove_forkliftable(df, debug)     

    # Count number of x's
    rolls_removed = (dfnew == "x").sum().sum()

    part2_answer = rolls_removed
    print(f'The answer to Part 2: {part2_answer}')         
    # Correct answer for Day 4, Part 2: 7922
    
    ## TEST AREA
    '''
    print('123'*3)
    '''
        
if __name__ == "__main__":
    main(lines,debug=DEBUG)
    