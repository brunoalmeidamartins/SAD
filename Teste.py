import pandas as pd
import sqlite3

con=sqlite3.connect("Banco_Dados/database.sqlite")

data=pd.read_sql_query("SELECT * FROM country",con)

x = pd.read_sql_query("SHOW TABLES ", con)
print(x)