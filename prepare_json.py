import json
d = {'name':'', 'team':'', 'pos': '', 'points': 0, 'performance': 0}

ls = [{'name':'N. Pooran', 'team':'A', 'pos': 'WK', 'points': 8.5, 'performance': 76},
        {'name':'A Markram', 'team':'A', 'pos': 'BAT', 'points': 8.5, 'performance': 50},
        {'name':'M Agarwal', 'team':'A', 'pos': 'BAT', 'points': 9.5, 'performance': 380},
        {'name':'D Hooda', 'team':'A', 'pos': 'ALL', 'points': 8.5, 'performance': 287},
        {'name':'F Allen', 'team':'A', 'pos': 'ALL', 'points': 8.5, 'performance': 57},
        {'name':'KL Rahul', 'team':'A', 'pos': 'WK', 'points': 11, 'performance': 506},
        {'name':'P Singh', 'team':'A', 'pos': 'BOWL', 'points': 8.5, 'performance': 88},
        {'name':'A Rashid', 'team':'A', 'pos': 'BOWL', 'points': 8.5, 'performance': 50},
        {'name':'A Singh', 'team':'A', 'pos': 'BOWL', 'points': 8.5, 'performance': 223},
        {'name':'H Brar', 'team':'A', 'pos': 'BOWL', 'points': 8, 'performance': 199},
        {'name':'I Porel', 'team':'A', 'pos': 'BOWL', 'points': 8, 'performance': 40},
        {'name':'M Shami', 'team':'A', 'pos': 'BOWL', 'points': 9, 'performance': 259},
        {'name':'R Parag', 'team':'B', 'pos': 'BAT', 'points': 8.5, 'performance': 219},
        {'name':'Y Jaiswal', 'team':'B', 'pos': 'BAT', 'points': 8.5, 'performance': 107},
        {'name':'C Morris', 'team':'B', 'pos': 'ALL', 'points': 9.5, 'performance': 512},
        {'name':'L Livingstone', 'team':'B', 'pos': 'ALL', 'points': 9, 'performance': 99},
        {'name':'M Lomror', 'team':'B', 'pos': 'ALL', 'points': 8, 'performance': 100},
        {'name':'R Tewatia', 'team':'B', 'pos': 'ALL', 'points': 9, 'performance': 192},
        {'name':'S Samson', 'team':'B', 'pos': 'WK', 'points': 9.5, 'performance': 443},
        {'name':'C Sakariya', 'team':'B', 'pos': 'BOWL', 'points': 8.5, 'performance': 237},
        {'name':'K Tyagi', 'team':'B', 'pos': 'BOWL', 'points': 8, 'performance': 90},
        {'name':'M Rahman', 'team':'B', 'pos': 'BOWL', 'points': 9, 'performance': 270}]
filename = 'teams.json'

with open(filename, 'w') as fp:
    json.dump(ls,fp)


