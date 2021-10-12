import sqlite3
import numpy as np
import pandas as pd
# import geopandas
import matplotlib.pyplot as plt

# collision_file = f'./data/switrs/switrs_raw_csvs/20201024/20201024_CollisionRecords.txt'
# party_file = f'./data/switrs/switrs_raw_csvs/20201024/20201024_PartyRecords.txt'
# victim_file = f'./data/switrs/switrs_raw_csvs/20201024/20201024_VictimRecords.txt'
#
# collision_df = pd.read_csv(collision_file)

# print(collision_df)
from numpy.testing._private.parameterized import param

from util.CircularBarplot import draw_24_hour

sql_file = './data/sqlite/archive/switrs.sqlite'
export_case_by_time_csv = './data/export/case_by_hour.csv'

cnx = sqlite3.connect(sql_file)
# gdf = geopandas.GeoDataFrame(
#     df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))

# 1 stats by time
# case_by_date_df = pd.read_sql_query(
#     "SELECT count(case_id) as cases, substr(collision_time,0,3) as hour FROM collisions group by hour", cnx)
# case_by_date_df.to_csv(path_or_buf=export_case_by_time_csv)
df = pd.read_csv(export_case_by_time_csv)
# plt.show()
# print(df.iloc[:18:-1].append(df.iloc[::-1]))
draw_24_hour(df.iloc[::-1])
