import pandas as pd

class Database:
    df = pd.read_csv('sample.csv')
    df.fillna(0, inplace=True)

    df.set_index("Name", inplace=True)

    @staticmethod
    def get_by_name(player, col):
        return Database.df[col][player]
    
    @classmethod
    def save_csv(cls, filename):
        cls.df.reset_index(inplace=True)
        cls.df.to_csv(filename, index=False)

class Player:
    def __init__(self, name, position, team) -> None:
        self.name = name
        self.position = position
        self.team = team

        self.standard_deviation = float(Database.df.loc[self.name, 'STANDARD'])
        self.mean = float(Database.df.loc[self.name, 'MEAN'])

    def get_total(self):
        return Database.df['total'][self.name]