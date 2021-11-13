import sqlite3
import pandas as pd

# import geopandas as geopandas
import numpy as np
# import geopandas
import matplotlib.pyplot as plt
from util.CircularBarplot import draw_24_hour

sql_file = './data/switrs.sqlite'
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


def stat_by_env():
    field = 'road_surface'
    export_case_by_env_csv = f'./data/export/by_env/case_by_{field}.csv'
    export_case_by_env_png = f'./data/export/by_env/case_by_{field}.png'
    case_by_geo_df = pd.read_sql_query(
        f"SELECT count(case_id) as cases, {field} as {field} FROM collisions group by {field}",
        cnx)
    case_by_geo_df.to_csv(path_or_buf=export_case_by_env_csv)
    df = pd.read_csv(export_case_by_env_csv)
    df.plot.pie(x=field, y='cases')
    plt.savefig(export_case_by_env_png)
    plt.show()


# stat_by_env()

def export_collision_only():
    csv_file = 'data/export/collisions_la.csv'
    case_by_date_df = pd.read_sql_query(
        "SELECT case_id"
        ",strftime('%Y',date(collision_date)) as collision_year"
        ",collision_date"
        ",strftime('%w',date(collision_date)) as day_of_week"
        ",collision_time"
        ",county_location"
        ",latitude"
        ",longitude"
        ",primary_road"
        " FROM collisions "
        " WHERE collision_year >= '2020'"
        " AND latitude IS NOT NULL AND longitude IS NOT NULL",
        cnx)
    print(len(case_by_date_df))
    case_by_date_df.to_csv(path_or_buf=csv_file)


def print_data():
    data = pd.read_sql_query("SELECT case_id,collision_time,county_location,latitude,longitude, primary_road"
                             " from collisions "
                             " where date(collision_date) > (date('2020-01-01')) "
                             " AND latitude IS NOT NULL AND longitude IS NOT NULL "
                             " limit 100"
                             ,
                             cnx)
    print(data)


export_collision_only()
# print_data()
