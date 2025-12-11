import advent_of_code as aoc
import math
import pandas as pd

## TODO 


INPUT_PATH = "./input/"
INPUT_TEMPLATE = "day{num}.txt"
TEST_INPUT_TEMPLATE = "day{num}_test.txt"

day = 6

lines = aoc.input_readlines(day, test=True)
lines = aoc.input_readlines(day)

DEBUG = True
DEBUG = False

TEST = True
TEST = False

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

def process_lines(lines,debug):

    # Build a list of operations, reverse order (going to process numbers from right to left)
    operations = lines[-1].split()
    operations.reverse()

    # Build a dataframe where each row is a line, and each character of line is in a different column
    #  note: list(line) example line = 'abc' list(line) = ['a','b','c']
    rows_to_add = []    
    for line in lines[:-1]:
        rows_to_add.append(list(line))
    df = pd.DataFrame(rows_to_add)
    
    # Reverse order - go through columns backwards
    dfcols = df.columns.to_list()
    dfcols.reverse()
    
    # Go through dataframe columns backwards
    #  Build up list of numbers to perform operation on (nums_to_process)
    #  Once you hit a column of all spaces, perform operation and reset nums_to_process
    #    Store result of operations slug_math
    oper_idx = 0
    nums_to_process = []
    slug_math = []
    for icol in dfcols:
        col_str_cat = ''.join(df.iloc[:,icol])
        if all(char == ' ' for char in list(col_str_cat)):
            
            # break in slug numbers found, do operation
            if operations[oper_idx] == '+':
                if debug:
                    print('Summing: ', nums_to_process)
                slug_math.append(sum(nums_to_process))
            else:
                if debug:
                    print('Product of: ', nums_to_process)
                slug_math.append(math.prod(nums_to_process))
            nums_to_process = []
            oper_idx += 1
            
        else:
            nums_to_process.append(int(col_str_cat))
            if debug:
                print(nums_to_process)
            
    # Above code does not catch last operation, perform last one
    if operations[oper_idx] == '+':
        if debug:
            print('Summing: ', nums_to_process)
        slug_math.append(sum(nums_to_process))
    else:
        if debug:
            print('Product of: ', nums_to_process)
        slug_math.append(math.prod(nums_to_process))

    return slug_math
    

def main(lines,debug=DEBUG,test=TEST):

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
    # Read in input differently than normal - keep white spaces at beginning and end
    if test:
        file_name = f'{INPUT_PATH}/{TEST_INPUT_TEMPLATE.format(num=day)}'
    else:
        file_name = f'{INPUT_PATH}/{INPUT_TEMPLATE.format(num=day)}'
    with open(file_name,'r') as f:
        lines = f.readlines()
        lines = [s.replace('\n','') for s in lines]
    
    slug_math = process_lines(lines,debug)
    if debug:
        print(slug_math)
    
    part2_answer = sum(slug_math)
    print(f'The answer to Part 2: {part2_answer}')         
    # Correct answer for Day 6, Part 2: 11643736116335
    
    
    ## TEST AREA
    '''
    print('123'*3)
    '''
        
if __name__ == "__main__":
    main(lines)
    