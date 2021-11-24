import sqlite3
import pandas as pd
from pandas.core.indexes.datetimes import DatetimeIndex
# connection = sqlite3.connect('/Volumes/LaCie/Document/Master - 4th Semester/Visualization/switrs.sqlite')

# temp = pd.read_sql_query('SELECT collisions.case_id, vehicle_year, vehicle_make, statewide_vehicle_type_at_fault, primary_road, secondary_road, chp_vehicle_type_at_fault, pedestrian_collision,motorcycle_collision, truck_collision, bicycle_collision, pedestrian_killed_count, pedestrian_injured_count, bicyclist_killed_count, bicyclist_injured_count, motorcyclist_killed_count, motorcyclist_injured_count, collision_time, latitude, longitude FROM collisions INNER JOIN parties ON collisions.case_id = parties.case_id WHERE county_location = "los angeles"', connection)
# temp.to_csv('temp.csv')
vehicleDB = pd.read_csv("/Volumes/LaCie/Nhom1DataVisualization/code/python/data/export/by_vehicle/temp.csv")
mainroadDB = pd.read_csv("/Volumes/LaCie/Nhom1DataVisualization/code/python/data/export/collisions_la_main_road_only.csv")
mainroadDB.dropna(axis=1)
vehicleDB.dropna(axis=1)
data = vehicleDB.merge(mainroadDB, on="case_id")
data['year'] = pd.DatetimeIndex(data['collision_date']).year
data['vehicle_year'] = pd.DatetimeIndex(pd.to_datetime(data['vehicle_year'], format='%Y')).year
data = data[data['year'] >= 2016]
data.to_csv('vehicle.csv')

# countMake = data.groupby(['vehicle_make']).size
# countMake.to_csv('vehicle_make.csv')

