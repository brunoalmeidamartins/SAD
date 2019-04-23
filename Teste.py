import pandas as pd
import numpy as np
import os

path_banco = os.getenv("HOME") + '/Bancos_Dados/UFJF/Periodo_2019_1/SAD/'

'''

con=sqlite3.connect("Banco_Dados/database.sqlite")

data=pd.read_sql_query("SELECT * FROM country",con)

x = pd.read_sql_query("SHOW TABLES ", con)
print(x)

'''
#Bases

#base_Country = pd.read_csv(path_banco + 'Country.csv')
#base_League = pd.read_csv(path_banco + 'League.csv')
base_Match = pd.read_csv(path_banco + 'Match.csv')
#base_Player = pd.read_csv(path_banco + 'Player.csv')
#base_Player_Attributes = pd.read_csv(path_banco + 'Player_Attributes.csv')
#base_Team= pd.read_csv(path_banco + 'Team.csv')
#base_Team_Attributes= pd.read_csv(path_banco + 'Team_Attributes.csv')
#base_sqlite_sequence= pd.read_csv(path_banco + 'sqlite_sequence.csv')

'''
Posse de bola influencia no resultado final da partida:
Banco: 'Match' Colunas: 'home_team_goal', 'away_team_goal', 'possession'

Time que menos modifica seus jogadores tem melhor colocacao na tabela
Banco: 'Match' Colunas: 'home_player', ...
'''

#print(base_Match)
base_Match.describe()

'''
Tratamento de valores inconsistentes

#Valores negativos
##base_Match.loc[base_Match['name_colun'] < 0]


# apagar a coluna
##base.drop('name_colum', 1, inplace=True)


# apagar somente os registros com problema
##base_Match(base_Match[base_Match.nome_colum < 0].index, inplace = True)

# preencher os valores manualmente
# preencher os valores com a média
##base_Match.mean()
##base_Match['name_colum'].mean()
##base_Match['name_colum'][base_Match.name_colum > 0].mean()
#base_Match.loc[base_Match.name_colum < 0, 'name_colum'] = 40.92

FIM Tratamento de valores inconsistentes
'''


'''
Tratamento de valores faltantes
'''
#base = base_Match
#pd.isnull(base['BSD'])

#base.loc[pd.isnull(base['BSD'])]

#previsores = base.iloc[:, 1:4].values

'''
Preenchendo valores com biblioteca

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean',axis=0)
imputer = imputer.fit(previsores[:, 0:2])
previsores[:, 0:2] = imputer.transform(previsores[:, 0:3]) #Recebe a proria transformacao
'''

base = base_Match

base.columns #Colunas do DataFrame

base.shape #Qauntidade de linhas e colunas do DataFrame

base.index #Descricao do Index

base.count() #Contagem de dados nao nulos

'''
Resumo dos dados:
'''

#Soma dos valores de um DataFrame
base.sum()
#Menor valor de um DataFrame
base.min()
#Maior valor
base.max()
#Index do menor valor
base.idmin()
#Index do maior valor
base.idmax()
#Resumo estatístico do DataFrame, com quartis, mediana, etc.
base.describe()
#Média dos valores
base.mean()
#Mediana dos valores
base.median()
