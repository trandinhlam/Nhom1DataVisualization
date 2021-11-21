import numpy as np # linear algebra
import pandas as pd # data processing
import sqlite3
import os
import matplotlib.pyplot as plt
import seaborn as sns
import bioinfokit.analys


pd.set_option('display.max_rows', 1500)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

sql_file = '../data/switrs.sqlite'


# cur = con.cursor()
def read_data():
    con = sqlite3.connect(sql_file)
    parties_query = " SELECT * FROM parties WHERE case_id IN \
    (SELECT case_id FROM collisions WHERE motorcycle_collision == 1)"

    victims_query = " SELECT * FROM victims WHERE case_id IN \
    (SELECT case_id FROM collisions WHERE motorcycle_collision == 1)"

    # Read the data
    collisions1 = pd.read_sql_query("SELECT * FROM collisions WHERE motorcycle_collision == 1", con)
    parties1 = pd.read_sql_query(parties_query, con)
    victims1 = pd.read_sql_query(victims_query, con)

    # Save the data as csv files
    collisions1.to_csv('collisions.csv', index=False)
    parties1.to_csv('parties.csv', index=False)
    victims1.to_csv('victims.csv', index=False)

    con.close()


# We will change dtype when we need it, multiple types are memory inefficient
collisions = pd.read_csv('collisions.csv', dtype=str)
parties = pd.read_csv('parties.csv', dtype=str)
victims = pd.read_csv('victims.csv', dtype=str)
all_vehicles = parties.groupby(['statewide_vehicle_type']).agg({'case_id': 'count'})
# How large is our data
print("There are {x} records from collisions.".format(x=collisions.shape[0]))
print("There are {y} records from parties.".format(y=parties.shape[0]))
print("There are {z} records from victims.".format(z=victims.shape[0]))

all_vehicles = parties.groupby(['statewide_vehicle_type']).agg({'case_id':'count'})

motorcycle = ['motorcycle or scooter', 'moped']
motorcycles = parties[parties.statewide_vehicle_type.isin(motorcycle)]

# What are the most popular motorbikes in collisions
count1 = motorcycles.groupby(['vehicle_make']).agg({'case_id':'count'})
count_sorted1 = count1.sort_values(by='case_id', ascending=False)
print(count_sorted1.head(20))
