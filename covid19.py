#scraping data -> json -> dataframe -> mysql
import pandas as pd
import requests
import json
from bs4 import BeautifulSoup
import sqlalchemy

#connect to MySQL DB in AWS
db_username = 'administrator'
db_password = 'Corona19'
db_ip       = 'covid19db.co2z4r8ftwl1.us-east-2.rds.amazonaws.com'
db_name     = 'covid19'
db_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                         format(db_username, db_password, db_ip, db_name))
#get url for world dataset
res = requests.get("https://www.worldometers.info/coronavirus/")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0] 
df = pd.read_html(str(table))

# to json
a = df[0].to_json(orient='records')

# read json to dataframe
df1 = pd.read_json(a,orient='columns')

# dataframe to Mysql DB
df1.to_sql(con=db_connection, name='covid_world', if_exists='replace')
    
#USA Dataset
res_usa = requests.get("https://www.worldometers.info/coronavirus/country/us")
soup_usa = BeautifulSoup(res_usa.content,'lxml')
table_usa = soup_usa.find_all('table')[0] 
df_usa = pd.read_html(str(table_usa))
a_usa = df_usa[0].to_json(orient='records')
df1_usa = pd.read_json(a_usa,orient='columns')
df1_usa.to_sql(con=db_connection, name='covid_usa', if_exists='replace')