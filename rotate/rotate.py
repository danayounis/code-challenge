def split_line(line): 
    return [char for char in line]

def get_file_content(file_name:str):
    input_file = open(file_name, 'r')
    lines = [] 
    for line in input_file: 
        lines.append(split_line(line[:-1]))
    return lines

def get_max_column_length(matrix):
    max = 0
    for row in matrix:
        if max < len(row):
            max = len(row)
    return max

def rotate(matrix):
    max = get_max_column_length(matrix)
    output = [0] * max
    for i in range(max):
        output[i] = [''] * max
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            output[j][i] = matrix[i][j]
    return output

def print_matrix(matrix):    
    for line in matrix:
        print(''.join(line))


import sys

input_file_name = 'input.txt'
if len(sys.argv) > 1:
    input_file_name = sys.argv[1]

print_matrix(rotate(get_file_content(input_file_name)))