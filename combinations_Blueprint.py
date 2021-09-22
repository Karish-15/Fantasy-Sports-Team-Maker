# TO GET COMBINATIONS SUCH THAT SUM IS K AND NUMBER OF PLAYERS IS N

from itertools import combinations 
def findCombinations(lst, K, N): 
    all_comb = [team for team in combinations(lst,N) if sum([temp['points'] for temp in team]) == K]
    return all_comb


# List of player name and points
lst = [{'points': 30, 'Name': 'a'},{'points': 25, 'Name': 'b'},
        {'points': 15, 'Name': 'c'},{'points': 20, 'Name': 'd'},
        {'points': 10, 'Name': 'e'},{'points': 20, 'Name': 'f'},
        {'points': 30, 'Name': 'aa'},{'points': 25, 'Name': 'bb'},
        {'points': 15, 'Name': 'cc'},{'points': 20, 'Name': 'dd'},
        {'points': 10, 'Name': 'ee'},{'points': 20, 'Name': 'ff'}]
K = 100
N = 5

temp = findCombinations(lst, K, N) # Returns a list of tuples and each tuple has multiple dictionaries in it
for t in temp:
    names = ', '.join([temp['Name'] for temp in t])
    print(names)



# TO GET SUM OF PLAYER VALUES IN CURRENT TEAM(LIST OF DICTIONARIES)

# d = [{'points': 30},{'points': 25},{'points': 15},{'points': 5},{'points': 10},{'points': 20}]
# temp = [temp['points'] for temp in d]
# print(sum(temp))