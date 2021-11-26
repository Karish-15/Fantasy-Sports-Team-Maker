from data_model import Database, Player
import pandas as pd
import statistics


for index, row in Database.df.iterrows():
    # index will be player name here, row is preceding columns

    sum_values = 0 # Sum of player's performance values
    track_column = 0 # Keep track of column number
    matches_played = 0 # Number of matches played
    player_values = []

    for index_row, value in row.iteritems():
        if track_column == 8:
            break
        else:
            if(value != 0):
                matches_played += 1
                player_values.append(int(value))
            track_column += 1
            # player_values.append(int(value))

    sum_values = sum(player_values)
    mean = float(sum_values)/float(matches_played) # Mean of performance points for current player

    standard_deviation = statistics.pstdev(player_values) # Calculate standard deviation    

    median = statistics.median(player_values) # Calculate median from player's performance from recent matches

    # Update values in Dataframe
    Database.df.loc[index, 'MEAN'] = mean
    Database.df.loc[index, 'STANDARD'] = standard_deviation
    Database.df.loc[index, 'MEDIAN'] = median
    

if __name__ == '__main__':
    print(Database.df)
    Database.save_csv('sample.csv')




    
