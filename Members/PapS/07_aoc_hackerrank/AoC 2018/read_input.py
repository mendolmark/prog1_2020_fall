def read_input(name: str):
    '''
    Read Advent of Code 2018 input data. 
    
    Parameters:
    - TXT file name (string): Rows must conatin positive and negative integers.
    
    Return:
    - Input data (list of ints)
    '''
    with open(name, 'r') as input:
        data = [*map(lambda x: int(x.strip()), input.readlines())]
        
    return data
