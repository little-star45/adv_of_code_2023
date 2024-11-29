#important information:
#red, green, blue - cubes colours
"""
    What is the fewest number of cubes of each color that could have been 
in the bag to make the game possible?

Main task:
    For each game, find the minimum set of cubes 
that must have been present. What is the sum of the power of these sets?
"""

def load_data_from_file(data_file):
    return open(data_file,'r').read()

def decode_data(data):
    #turn data from file into tuple:
    """
    [
    (_id,(max_blue, max_red, max_green)),
    (_id,(max_blue, max_red, max_green)),
    (_id,(max_blue, max_red, max_green)),
    ...
    ]
    """
    data_traces = []

    for trace in data:
        full_id = trace.split(':')[0]
        _id = full_id.split(' ')[1]

        main_data = trace.split(':')[1]
        main_data_split = main_data.split(';')

        max_dict = {
                'blue': 0,
                'red': 0,
                'green': 0
            }

        for data_trace in main_data_split:
            data_trace_split = data_trace.split(',')

            for x in data_trace_split:
                decode_trace = x.split(' ')
                if (max_dict[decode_trace[2]]<int(decode_trace[1])):
                    max_dict[decode_trace[2]]=int(decode_trace[1])

        data_traces.append((_id, (max_dict['red'], max_dict['green'], max_dict['blue'])))
    return data_traces

def main(data_file):

    data_from_file = load_data_from_file(data_file)
    data_tuples = decode_data(data_from_file.split('\n'))

    sum_power_sets = 0
    control_list = []

    print(data_tuples)
    for game in data_tuples:
        sum_power_sets += game[1][0]*game[1][1]*game[1][2]
        control_list.append(game[1][0]*game[1][1]*game[1][2])
            
    return control_list,sum_power_sets


def test_function(data_file):
    answers = (2286,(48, 12, 1560, 630, 36))

    control_list,sum_power_sets = main(data_file)
    print(control_list)

    for idx in range(len(control_list)):

        if (control_list[idx]==answers[1][idx]):
            print('Pass') 
        else:
            print(f'Failed. Sum:{sum_power_sets}, list of powers:{control_list[idx]} exp:{answers[1][idx]} , expected {answers[0]}') 

if __name__ == '__main__':
    test_function('data_test.txt')
    # _,sum_power_sets = main('data1.txt')

    # print(sum_power_sets)
    
    #Right answer: 2913