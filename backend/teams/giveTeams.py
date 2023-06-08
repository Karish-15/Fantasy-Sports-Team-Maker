import pandas as pd
import io
from dotenv import load_dotenv
import os
import redis

from Main.makeTeams import makeTeams

def makeDataframe(file_obj):
    dataframe = pd.read_csv(io.StringIO(file_obj.read().decode('utf-8')), delimiter=',')
    return dataframe

def makeDataframe_list(list):
    for x in list:
        x['FREQ'] = 0
    dataframe = pd.DataFrame(list)
    return dataframe

# Also check if all columns are present or not
def csv_valid(file_obj, df):
    if not str(file_obj).endswith('.csv'):
        return False
    required_columns = [
        'Name', 'TEAM', 'POS', 'VALUE', 'POINTS'
        ]
    csv_columns = df.columns.tolist()
    for column in required_columns:
        if not column in csv_columns:
            return False

    return True

def form_teams(df, request_data):
    results = makeTeams(df, request_data)

    #Check if something can be done with Dataframe object
    response = {
        # "Dataframe": results[1],
        "Match": results[3][0] + ' vs ' + results[3][1], 
        "Time Taken": results[2],
        "Teams": results[0],
    }

    return response

def give_sample_data():
    load_dotenv()
    r = redis.Redis(
        host=os.environ.get('REDIS_HOST'),
        port=10370,
        password=os.environ.get('REDIS_PASSWORD'))

    l = list((r.json().get(name='players')['players']))

    return l;