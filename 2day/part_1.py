#important information:
#red, green, blue - cubes colours
"""
    Each time you play this game, he will 
hide a secret number of cubes of each 
color in the bag, and your goal is to 
figure out information about the number of cubes.

    A few times per game the Elf will reach into 
the bag, grab a handful of random cubes, 
show them to you, and then put them back in the bag.

Main task:
    Determine which games would have been possible 
if the bag had been loaded with only 12 red cubes, 
13 green cubes, and 14 blue cubes.
What is the sum of the IDs of those games?

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

def main(data_file, colors_tuple):
    nb_red, nb_green, nb_blue = colors_tuple
    data_from_file = load_data_from_file(data_file)
    data_tuples = decode_data(data_from_file.split('\n'))

    possible_games = []
    sum_possible_games = 0

    for game in data_tuples:
        if (game[1][0]<=nb_red) and (game[1][1]<=nb_green) and (game[1][2]<=nb_blue):
            possible_games.append(game[0])
            sum_possible_games += int(game[0])
            
    return possible_games, sum_possible_games


def test_function(data_file):
    answers = (8,)
    test_colors_nb = (12, 13, 14)
    possible_games, sum_possible_games = main(data_file, test_colors_nb)

    if (sum_possible_games==answers[0]):
        print('Pass') 
    else:
        print(f'Failed. Possible games: {possible_games}, sum:{sum_possible_games}, expected {answers[0]}') 

if __name__ == '__main__':
    test_function('data1.txt')