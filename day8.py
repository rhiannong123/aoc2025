import advent_of_code as aoc
import math
import pandas as pd

## TODO 

day = 8

lines = aoc.input_readlines(day, test=True)
#lines = aoc.input_readlines(day)

DEBUG = True
#DEBUG = False

def process_lines(lines,debug):
    xs = []
    ys = []
    zs = []
    for line in lines:
        x,y,z = line.split(',')
        xs.append(int(x))
        ys.append(int(y))
        zs.append(int(z))
    return xs, ys, zs
        
    
def find_distances(xs,ys,zs,debug):
    points_only_list = [] # used for tracking
    rows_to_add = [] # used to build df
    icount = 0
    for ax,ay,az in zip(xs,ys,zs):
        #if ax != xs[0]:
        #    break
        for bx,by,bz in zip(xs,ys,zs):
            
        #    icount += 1
        #    if icount == 10:
        #        break
            
            row = []
            if (ax == bx) & (ay == by) & (az == bz):
                # same point, skip
                continue
            if [bx,by,bz,ax,ay,az] in points_only_list:
                # Distance already accounted for, skip
                continue
            row = [ax,ay,az,bx,by,bz]
            points_only_list.append(row.copy())
            
            distance = math.sqrt( ((ax-bx)**2) + ((ay-by)**2) + ((az-bz)**2) ) 
            row.append(distance)
            rows_to_add.append(row)

    df = pd.DataFrame(rows_to_add)
    df.columns = ['ax','ay','az','bx','by','bz','distance']
    
    df = df.sort_values(by="distance",ascending=True)    
    df = df.reset_index(drop=True)

    return df


def make_circuits(df,debug):
    
    # Make first circuit with first 2 points in row 0 of df
    # Track circuits in a list of lists
    ax,ay,az = df.loc[0,'ax'], df.loc[0,'ay'], df.loc[0,'az']
    bx,by,bz = df.loc[0,'bx'], df.loc[0,'by'], df.loc[0,'bz']
    
    idf = pd.DataFrame([
        [ax,ay,az], 
        [bx,by,bz]
        ])
    circuits = [idf]
    for idx in df.index[1:]:
        ax,ay,az = df.loc[idx,'ax'], df.loc[idx,'ay'], df.loc[idx,'az']
        point_a = [ax,ay,az]
        bx,by,bz = df.loc[idx,'bx'], df.loc[idx,'by'], df.loc[idx,'bz']
        point_b = [bx,by,bz]        
        
        for idf in circuits:
            if any((idf[[0,1,2]] == point_a).all(axis=1)):
                # Point exists in idf... it is already part of circuit 
                # (don't do anything with point a?), add point b though right?
                
                # this is slow, not sure if we should do this
                idf = idf.append(point_b)
                
            
            
        
        
        
        
    


def main(lines,debug=DEBUG):

    xs,ys,zs = process_lines(lines,debug)
    
    df = find_distances(xs,ys,zs,debug)

    if debug:
        print(df)
        
    make_circuits(df,debug)

    ## Part 1
    part1_answer = 1
    print(f'The answer to Part 1: {part1_answer}')
    # Correct answer for Day 7, Part 1: 1562
        
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
    