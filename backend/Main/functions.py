from itertools import combinations

def findCombinations(lst, K, N, first_team, second_team, minpositions): 
    minbat, minbowl, minall, minwk = minpositions['bat'], minpositions['bowl'], minpositions['all'], minpositions['wk']
    all_comb = [
                list(team) 
                for team in combinations(lst,N) 
                if ((sum([temp['points'] for temp in team]) <= (K) 
                    and sum([temp['points'] for temp in team]) >= 97 ) 
                    and filterTeams(team, first_team, second_team) 
                    and positioncheck(team, minbat, minbowl, minall, minwk))
                ]

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
    team.sort(key = lambda x: x['performance'], reverse = True)
    return [team[0]['name'], team[1]['name']]

def filterTeams(team, first_team, second_team):
    first_count, second_count = 0, 0
    team_eligible = True

    for player in team:
        if(first_count>6 or second_count>6):
            team_eligible = False

        if(player['team'] == first_team):
            first_count += 1

        elif(player['team'] == second_team):
            second_count += 1
    
    return team_eligible

def givePlayerPositions(team):
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
    return {'bat': bat, 'bowl': bowl, 'all':all_count, 'wk': wk}