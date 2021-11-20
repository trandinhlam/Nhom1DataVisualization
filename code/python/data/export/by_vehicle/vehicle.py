import sqlite3
import pandas as pd
connection = sqlite3.connect('/Volumes/LaCie/Document/Master - 4th Semester/Visualization/switrs.sqlite')

vehicleIn = pd.read_sql_query('SELECT case_id, statewide_vehicle_type_at_fault, primary_road, secondary_road, chp_vehicle_type_at_fault, pedestrian_collision,motorcycle_collision, truck_collision, bicycle_collision, pedestrian_killed_count, pedestrian_injured_count, bicyclist_killed_count, bicyclist_injured_count, motorcyclist_killed_count, motorcyclist_injured_count, collision_date, collision_time, latitude, longitude FROM collisions WHERE county_location = "los angeles"', connection)
vehicleIn['year'] = pd.DatetimeIndex(vehicleIn['collision_date']).year
vehicleIn = vehicleIn[vehicleIn['year'] >= 2016]
vehicleIn.to_csv('vehicle.csv')

