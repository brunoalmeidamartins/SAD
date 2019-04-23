import pandas as pd
import sqlite3
import os

path_banco = os.getenv("HOME") + '/Bancos_Dados/UFJF/Periodo_2019_1/SAD/'

'''

con=sqlite3.connect("Banco_Dados/database.sqlite")

data=pd.read_sql_query("SELECT * FROM country",con)

x = pd.read_sql_query("SHOW TABLES ", con)
print(x)

'''
#Bases

base_Country = pd.read_csv(path_banco + 'Country.csv')
base_League = pd.read_csv(path_banco + 'League.csv')
base_Match = pd.read_csv(path_banco + 'Match.csv')
base_Player = pd.read_csv(path_banco + 'Player.csv')
base_Player_Attributes = pd.read_csv(path_banco + 'Player_Attributes.csv')
base_Team= pd.read_csv(path_banco + 'Team.csv')
base_Team_Attributes= pd.read_csv(path_banco + 'Team_Attributes.csv')
base_sqlite_sequence= pd.read_csv(path_banco + 'sqlite_sequence.csv')

