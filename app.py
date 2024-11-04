import requests
import pandas as pd
from datetime import datetime as dt, timedelta
from dateutil import parser
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
import urllib
import pyodbc

server_name = ''
database= ''
username = ''
password = ''
schema=''

def scrape_data(url):

    response = requests.get(url)
    data=response.json()

    
    dataframe=pd.DataFrame(data)
   

    dataframe['datetime'] = dataframe['time'].apply(lambda x: pd.to_datetime(x, unit='ms'))
    dataframe['datetime'] = pd.to_datetime(dataframe['datetime']).dt.date

    dataframe=dataframe.groupby(dataframe['datetime']).max().reset_index()

#    dataframe.to_excel('data.xlsx', index=False, engine='xlsxwriter')
    connection_string_Gclinique = urllib.parse.quote_plus(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server_name};DATABASE={database};UID={username};PWD={password};')
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % connection_string_Gclinique)
    connection=engine.connect()



    try:
        dataframe.to_sql('devise_marroc', con=connection, index=False, schema=schema, if_exists='replace')
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'importation des données dans SQL Server : {str(e)}")
    
    print('les données sont ajouter a la table devise_marroc avec succées')


    

        

scrape_data('https://wise.com/rates/history+live?source=MAD&target=TND&length=5&resolution=daily&unit=year')
