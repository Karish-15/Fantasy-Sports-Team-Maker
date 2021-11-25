import json, time
from functions import findCombinations, giveCaptain
import pandas

start_time = time.time()
filename = 'teams.json'
# Get list from JSON
with open(filename) as file:
    lst = json.load(file)
allteams = findCombinations(lst, 100, 10)
index = 0
for team in allteams:
    if(index > 500):
        break
    print(str(index) + '. '+ ', '.join([temp['name'] for temp in team]) + '\t ', end = '' )
    print(' ' + str(sum([y['performance'] for y in team])), end = ' ')
    captains = giveCaptain(team)
    print('Captain: ' + captains[0] + ' VC: ' + captains[1])
    
    
    index +=1



print('Time Taken to form teams: ' + str(time.time() - start_time) + ' seconds')