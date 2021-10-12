import sqlite3

import geopandas as geopandas
import numpy as np
import pandas as pd
# import geopandas
import matplotlib.pyplot as plt
from util.CircularBarplot import draw_24_hour

sql_file = './data/sqlite/archive/switrs.sqlite'
cnx = sqlite3.connect(sql_file)


# 1 stats by time
def stat_by_time():
    export_case_by_time_csv = './data/export/case_by_weekday.csv'
    case_by_date_df = pd.read_sql_query(
        "SELECT count(case_id) as cases, strftime('%w',date(collision_date)) as weekday FROM collisions group by weekday",
        cnx)
    print(case_by_date_df)
    case_by_date_df.to_csv(path_or_buf=export_case_by_time_csv)
    df = pd.read_csv(export_case_by_time_csv)
    df.plot.bar(x='weekday', y='cases')
    plt.show()
    print(df.iloc[:18:-1].append(df.iloc[::-1]))
    draw_24_hour(df.iloc[::-1])

    case_by_date_df = pd.read_sql_query(
        "SELECT count(case_id) as cases, strftime('%w',date(collision_date)) as weekday FROM collisions group by weekday",
        cnx)


def stat_by_geo():
    export_case_by_geo_csv = './data/export/by_geo/case_by_population.csv'
    case_by_geo_df = pd.read_sql_query(
        "SELECT count(case_id) as cases, population as population FROM collisions group by population",
        cnx)
    case_by_geo_df.to_csv(path_or_buf=export_case_by_geo_csv)
    df = pd.read_csv(export_case_by_geo_csv)
    df.plot.bar(x='population', y='cases')
    plt.show()
    # gdf = geopandas.GeoDataFrame(
    #     df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))

stat_by_geo()
