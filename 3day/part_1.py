from pprint import pprint

#ASCII:
#0-9 -> numbers 48 to 57; '.' -> 46
"""
    If you can add up all the part numbers in the engine schematic, 
it should be easy to work out which part is missing.

    Any number adjacent to a symbol, even diagonally, 
is a "part number" and should be included in your sum. 
(Periods (.) do not count as a symbol.)

Main task:
    Return sum of numbers that adjacent symbols except '.'.

"""

def load_data_from_file(data_file):
    return open(data_file,'r').read()

def add_empty_dots_rows(n):
    return '.'*n

def list_to_nb(nb):
    str_nb = ''
    for i in nb:
        str_nb += chr(i)
    if (len(str_nb)>0):
        return int(str_nb)
    else:
        return 0

def turn_into_ascii(data_list):
    char_ascii_list = []
    for x in data_list:
        char_ascii_list.append(ord(x))
    return char_ascii_list

def decode_data(data):
    row_data = data.split('\n')

    #adds blank lines to the data at the beginning and end, to avoid index out of range
    row_data.insert(0,add_empty_dots_rows(len(row_data[0])))
    row_data.append(add_empty_dots_rows(len(row_data[0])))

    data_to_ascii = []
    
    for row in row_data:
        data_to_ascii.append(turn_into_ascii(row))

    pprint(row_data)
    pprint(data_to_ascii)
    return data_to_ascii

def main(data_file):
    nb_or_dot = [x for x in range(48,58)]+[46]

    raw_data = load_data_from_file(data_file)
    ascii_data = decode_data(raw_data)

    one_number=[]
    adjacent_to_symbol = False
    result_sum = 0

    for i, row in enumerate(ascii_data[1:-1]):
        i +=1
        for j, nb in enumerate(row):
            if (j==0):
                if (nb>=48) and (nb<=57):
                    one_number.append(nb)
                    if (
                        (ascii_data[i+1][j] not in nb_or_dot)
                        or (ascii_data[i+1][j+1] not in nb_or_dot) 
                        or (ascii_data[i][j+1] not in nb_or_dot)
                        or (ascii_data[i-1][j] not in nb_or_dot) 
                        or (ascii_data[i-1][j+1] not in nb_or_dot)
                        ) :
                        adjacent_to_symbol = True
                else:
                    if(adjacent_to_symbol):
                        result_sum += list_to_nb(one_number)
                    one_number = []
                    adjacent_to_symbol = False

            elif (j==len(row)-1):
                if (nb>=48) and (nb<=57):
                    one_number.append(nb)
                    if (
                        (ascii_data[i+1][j] not in nb_or_dot) 
                        or (ascii_data[i-1][j] not in nb_or_dot) 
                        or (ascii_data[i+1][j-1] not in nb_or_dot)
                        or (ascii_data[i-1][j-1] not in nb_or_dot) 
                        or (ascii_data[i][j-1] not in nb_or_dot)
                        ) :
                        adjacent_to_symbol = True
                else:
                    if(adjacent_to_symbol):
                        result_sum += list_to_nb(one_number)
                    one_number = []
                    adjacent_to_symbol = False
            else:
                if (nb>=48) and (nb<=57):
                    one_number.append(nb)
                    if (
                        (ascii_data[i+1][j] not in nb_or_dot) 
                        or (ascii_data[i-1][j] not in nb_or_dot) 
                        or (ascii_data[i+1][j-1] not in nb_or_dot)
                        or (ascii_data[i-1][j-1] not in nb_or_dot) 
                        or (ascii_data[i][j-1] not in nb_or_dot)
                        or (ascii_data[i][j+1] not in nb_or_dot)
                        or (ascii_data[i+1][j+1] not in nb_or_dot)
                        or (ascii_data[i-1][j+1] not in nb_or_dot) 
                        ) :
                        adjacent_to_symbol = True
                else:
                    if(adjacent_to_symbol):
                        result_sum += list_to_nb(one_number)
                    one_number = []
                    adjacent_to_symbol = False
    print(result_sum)        


def test_function(data_file):
    answers = (4361,)
    _,__ = main(data_file)

    if (_==answers[0]):
        print('Pass') 
    else:
        print(f'') 

if __name__ == '__main__':
    # test_function('data1.txt')
    main('data_test.txt')

