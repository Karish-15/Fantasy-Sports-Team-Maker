from itertools import combinations
from statistics import median

def findCombinations(lst, K, N): 
    minbat, minbowl, minall, minwk = 3, 3, 3, 1
    all_comb = [list(team) for team in combinations(lst,N) if ((sum([temp['points'] for temp in team]) <= (K-9) and sum([temp['points'] for temp in team]) >= 88) and positioncheck(team, minbat, minbowl, minall, minwk))]
    all_comb.sort(key = lambda x: sum([y['performance'] for y in x]), reverse=True)
    return all_comb

def positioncheck(team, minbat,minbowl,minall,minwk): # team is a tuple of dictionaries
    bat, bowl, all_count, wk = 0,0,0,0
    for player in team:
        if(player['pos'] == 'BAT'):
            bat += 1
        elif(player['pos'] == 'BOWL'):
            bowl += 1
        elif(player['pos'] == 'ALL'):
            all_count += 1
        elif(player['pos'] == 'WK'):
            wk += 1
    return (bat >= minbat and bat <=6) and (bowl >= minbowl and bowl<=6) and (all_count>=minall and all_count<=4) and (wk>=minwk and wk<=2)

def giveCaptain(team):
    team.sort(key = lambda x: x['performance'])
    return [team[0]['name'], team[1]['name']]

