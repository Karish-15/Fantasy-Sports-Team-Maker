
def givePlayerList(df):
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
    
    return lst