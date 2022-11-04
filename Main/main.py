import json, time
from functions import findCombinations, giveCaptain
import pandas

# Set up Dataframe to update FREQ column
df = pandas.read_csv('sample.csv')
new_df = df
new_df.set_index('Name', inplace=True)
new_df.fillna(0, inplace=True)

start_time = time.time()

# Get list from JSON
filename = 'teams.json'
with open(filename) as file:
    lst = json.load(file)

# Set team codes
first_team_name = lst[0]['team']
second_team_name = ''
for i in range(len(lst)):
    while(lst[i]['team'] == first_team_name):
        i += 1
    
    second_team_name = lst[i]['team']
    break


# Form Teams
allteams = findCombinations(lst, 100, 11, first_team = first_team_name, second_team = second_team_name)

# Show Formed Teams
index = 1

for team in allteams:
    if(index > 500):
        break

    print(str(index) + '. '+ ', '.join([temp['name'] for temp in team]), end = '' )
    print('\t' + str(sum([y['performance'] for y in team])), end = ' ')

    captains = giveCaptain(team)
    print('\t\tCaptain: ' + captains[0] + ' VC: ' + captains[1])

    # Update CSV, Count player frequency (Number of times the player occured in formed teams)

    for player in team:
        freq = new_df.loc[player['name'], 'FREQ']
        freq = freq + 1
        new_df.loc[player['name'], 'FREQ'] = freq

    index +=1


if __name__ == '__main__':
    print(new_df)

    # new_df.to_csv('new_data.csv')

    print('Time Taken to form teams: ' + str(time.time() - start_time) + ' seconds')