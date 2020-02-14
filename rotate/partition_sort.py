def same_case(first , second):
    if (first.isdigit() and second.isdigit()) or (not first.isdigit() and not second.isdigit()): 
        return True
    else : 
        return False
def get_lines(file_name:str):
    input_file = open(file_name, 'r')
    lines = [] 
    for line in input_file: 
        lines.append(line)
    return lines

def get_line_sequences(line:str):
    seq = ""
    line_sqeuences = []
    length = len(line)
    if length < 2 :
        line_sqeuences.append(line)
        return line_sqeuences
    for i in range(length):
        seq += line[i]
        if line[i+1] == line[-1]:
            line_sqeuences.append(seq)
            return line_sqeuences
        else:
            char = line[i]
            next_char = line[i+1]
            if same_case(char , next_char):
                continue
            else:
                line_sqeuences.append(seq)
                seq = ""

def sort_lines(lines:list):
    line_sequences = []
    sorted_line = ""
    for line in lines:
        line_sequences = get_line_sequences(line)
        sorted_line = sort_line_sequences(line_sequences)
        

def sort_line_sequences(line_sequences:list):
    sorted_line = ""
    for seq in line_sequences:
        sorted_line += ''.join(sorted(seq))
    return sorted_line

import sys

if len(sys.argv) > 1:
    input_file_name = sys.argv[1]
    sort_lines(get_lines(input_file_name))
else:
    print('NO Input FILE!')

