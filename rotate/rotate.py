import sys
import partition_sort

def trim(test_list):   
    res = [] 
    for sub in test_list: 
        res.append(sub.replace("\n", ""))   
    return res

def split_line(line): 
    return [char for char in line]

def get_file_content(file_name:str):
    input_file = open(file_name, 'r')
    lines = [] 
    for line in input_file: 
        line_sequences = partition_sort.get_line_sequences(line)
        sorted_line = partition_sort.sort_line_sequences(line_sequences).replace('\n','')
        lines.append(split_line(sorted_line))
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
        output[i] = [''] * len(matrix)
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            output[j][i] = matrix[i][j]
    return output

def print_matrix(matrix):    
    for line in matrix:
        print(''.join(line))


input_file_name = 'input.txt'
if len(sys.argv) > 1:
    input_file_name = sys.argv[1]

print_matrix(rotate(get_file_content(input_file_name)))