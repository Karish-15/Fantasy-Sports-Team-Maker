import time

from .functions import findCombinations, giveCaptain, givePlayerPositions
from .prepare_player_list import givePlayerList

def makeTeams(df, request_data):
    start_time = time.time()

    # Get Player List
    lst = givePlayerList(df)

    # Set team codes
    first_team_name = lst[0]['team']
    second_team_name = ''
    for i in range(len(lst)):
        while(lst[i]['team'] == first_team_name):
            i += 1
        second_team_name = lst[i]['team']
        break

    minpositions = request_data['minpositions']

    # Form Teams
    allteams = findCombinations(
        lst, 100, 11, 
        first_team = first_team_name, second_team = second_team_name,
        minpositions = minpositions
        )

    # Show Formed Teams
    index = 1

    formed_teams = []
    for team in allteams:
        if(index > 500):
            break
        
        captains = giveCaptain(team)
        
        temp_dict = {}
        temp_dict ['index'] = index
        temp_dict['Team Performance'] = sum([y['performance'] for y in team])
        temp_dict['Captain, Vice Captain'] = [captains[0], captains[1]]
        temp_dict['Player List'] = ', '.join([temp['name'] for temp in team])
        temp_dict['Position Count'] = givePlayerPositions(team)

        formed_teams.append(temp_dict)

        # Update CSV, Count player frequency (Number of times the player occured in formed teams)
        for player in team:
            freq = df.loc[player['name'], 'FREQ']
            freq = freq + 1
            df.loc[player['name'], 'FREQ'] = freq

        index +=1
    
    return [formed_teams, df, str(time.time() - start_time) + 'seconds', [first_team_name, second_team_name]]
    