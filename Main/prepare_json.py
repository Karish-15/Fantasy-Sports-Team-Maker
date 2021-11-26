import json
import pandas

# Prepare JSON from sample.csv
d = {'name':'', 'team':'', 'pos': '', 'points': 0, 'performance': 0}
filename = 'teams.json'

df = pandas.read_csv('sample.csv')
df.fillna(0, inplace=True)
lst = []


players = df['Name'].tolist()
df.set_index('Name', inplace=True)



for player in players:
        temp_dict = {}
        temp_dict['name'] = player
        details = df.loc[player]
        temp_dict['team'] = details['TEAM']
        temp_dict['pos'] = details['POS']
        temp_dict['points'] = details['VALUE']
        temp_dict['performance'] = details['POINTS'] 

        lst.append(temp_dict)

print(lst)

with open(filename, 'w') as fp:
    json.dump(lst,fp)


