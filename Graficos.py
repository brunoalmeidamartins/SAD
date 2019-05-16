import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import os

#%matolotlib inline

sb.set()

path_banco = os.getenv("HOME") + '/SAD/base_Match_mod.csv'

base_Match = pd.read_csv(path_banco, low_memory = False)

colunas_em_uso = ['country_id','league_id','season','home_team_goal','away_team_goal','possession_home','possession_away','home_player_1','home_player_2','home_player_3','home_player_4','home_player_5',
                         'home_player_6','home_player_7','home_player_8','home_player_9','home_player_10','home_player_11',
                         'away_player_1','away_player_2','away_player_3','away_player_4','away_player_5','away_player_6',
                         'away_player_7','away_player_8','away_player_9','away_player_10','away_player_11', 'match_api_id',
                         'home_team_api_id','away_team_api_id','shoton', 'shotoff']


base1 = base_Match.loc[:,['home_team_goal','away_team_goal','possession_home', 'possession_away']]

base2 = base_Match.loc[:,['country_id','league_id','season','home_player_1','home_player_2','home_player_3','home_player_4','home_player_5',
                         'home_player_6','home_player_7','home_player_8','home_player_9','home_player_10','home_player_11',
                         'away_player_1','away_player_2','away_player_3','away_player_4','away_player_5','away_player_6',
                         'away_player_7','away_player_8','away_player_9','away_player_10','away_player_11', 'match_api_id',
                         'home_team_api_id','away_team_api_id','home_team_goal','away_team_goal']]

base3 = base_Match.loc[:,['home_team_goal', 'away_team_goal', 'shoton', 'shotoff']]

#sb.pairplot(base2)

i = 1
for nome in colunas_em_uso:
    base_plot = base_Match.loc[:,[nome]]

    sb.boxplot(data=base_plot)
    if i <= 9:
        plt.savefig('IMG/0'+str(i)+'-'+ nome +'.png')
    else:
        plt.savefig('IMG/' + str(i) + '-' + nome + '.png')
    i+=1

print(base2.describe())