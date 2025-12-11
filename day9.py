import advent_of_code as aoc
import math
import pandas as pd

## TODO 

day = 9

lines = aoc.input_readlines(day, test=True)
lines = aoc.input_readlines(day)

DEBUG = True
DEBUG = False

def process_lines(lines,debug):
    xs = []
    ys = []
    for line in lines:
        x,y = line.split(',')
        xs.append(int(x))
        ys.append(int(y))
    return xs, ys
        
    
def find_areas(xs,ys,debug):
    points_only_list = [] # used for tracking
    rows_to_add = [] # used to build df
    icount = 0
    for ax,ay in zip(xs,ys):
        #if ax != xs[0]:
        #    break
        for bx,by in zip(xs,ys):
            
        #    icount += 1
        #    if icount == 10:
        #        break
            
            row = []
            if (ax == bx) & (ay == by):
                # same point, skip
                continue
            if [bx,by,ax,ay] in points_only_list:
                # Distance already accounted for, skip
                continue
            row = [ax,ay,bx,by]
            points_only_list.append(row.copy())
            
            area = (abs(ax-bx) + 1) * (abs(ay-by) + 1) 
            row.append(area)
            rows_to_add.append(row)

    df = pd.DataFrame(rows_to_add)
    df.columns = ['ax','ay','bx','by','areas']
    
    df = df.sort_values(by="areas",ascending=False)    
    df = df.reset_index(drop=True)

    return df



def main(lines,debug=DEBUG):

    xs,ys = process_lines(lines,debug)
    df = find_areas(xs,ys,debug)
    if debug:
        print(df)

    ## Part 1
    part1_answer = df.loc[0,'areas']
    print(f'The answer to Part 1: {part1_answer}')
    # Correct answer for Day 9, Part 1: 4749672288
    # Day 9 too low: 4738183840
            
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
    