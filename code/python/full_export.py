import sqlite3
import pandas as pd
from pandas import isna

sql_file = './data/switrs.sqlite'
cnx = sqlite3.connect(sql_file)
# import geocoder


def build_full_query(last_id):
    return (" select "
            " a.case_id "
            " , substr(a.collision_date, 0, 5) as collision_year "
            " , collision_date "
            " , substr('SunMonTueWedThuFriSat', 1 + 3 * strftime('%w', collision_date), 3) as dayofweek "
            " , cast(substr(collision_time, 0, 3) as interger) collision_time "
            " , case "
            " when(cast(substr(collision_time, 0, 3) as interger) >= 6 and cast(substr(collision_time, 0, 3) as interger) < 11) "
            " or (cast(substr(collision_time, 0, 3) as interger) >= 3 and cast( "
            "     substr(collision_time, 0, 3) as interger) < 20) then "
            " 'rush' "
            " else 'not' "
            " end as is_rush_hour "
            " , county_location "
            " , latitude "
            " , longitude "
            " , primary_road "
            " , primary_road as main_road"
            " , weather_1 "
            " , road_surface "
            " , lighting "
            " , case "
            " when "
            " statewide_vehicle_type_at_fault = 'bicycle' "
            " then "
            " 'bicycle' "
            " when "
            " statewide_vehicle_type_at_fault = 'motorcycle or scooter' "
            " then "
            " 'motorcycle' "
            " when "
            " statewide_vehicle_type_at_fault = 'pedestrian' "
            " then "
            " 'pedestrian' "
            " when "
            " statewide_vehicle_type_at_fault = 'pickup or panel truck' "
            "                                   or statewide_vehicle_type_at_fault = 'truck or truck tractor' "
            "                                                                        or statewide_vehicle_type_at_fault = 'truck or truck tractor with trailer' "
            "                                                                                                             or statewide_vehicle_type_at_fault = 'pickup or panel truck with trailer' "
            " then "
            " 'truck' "
            " else 'orther' "
            " end as vehicle_caused_fault "
            " , case "
            " when "
            " killed_victims > 0 "
            " then "
            " 'killed' "
            " when "
            " injured_victims > 0 "
            " then "
            " 'injured' "
            " else 'not serious' "
            " end as collision_degree "
            " from collisions a "
            # " -- @ left "
            # " join "
            # " parties "
            # " b "
            # " - - @ on "
            # " a.case_id = "
            # " @b.case_id "
            # " - - left "
            #
            # " join "
            # " victims "
            # " c "
            # " - - @ on "
            # " a.case_id = "
            # " @c.case_id "
            # " - - @ and b.party_number "
            # " "
            # " = "
            # " "
            # " @c.party_number "
            # " "
            " where "
            " county_location = 'los angeles' "
            " and primary_road like 'I-%'")

main_roads = ['I-5', 'I-10','I-210','I-405','I-105','I-605','I-710','I-110']

def truncate_road(data):
    truncated = []
    for i in range(len(data)):
        road = data['primary_road'][i]
        try:
            split = road.split()
            main_road = split[0].replace('--', '-')
            main_road = main_road.split('(')[0]
            data['main_road'][i] = main_road
            if main_road in main_roads:
                truncated.append(data['main_road'][i])
        finally:
            i = i
    return truncated


def export_full():
    csv_file = 'data/export/collisions_la_main_road_only.csv'
    last_id = 0
    batch_data = pd.read_sql_query(build_full_query(last_id), cnx)
    print(len(batch_data))
    # truncate primary_road
    truncate_road(batch_data)
    batch_data.to_csv(path_or_buf=csv_file)


# def read_data():
#     csv_file = './data/export/collisions_la.csv'
#     csv_file_export = './data/export/location_2_json.csv'
#     data = pd.read_csv(csv_file)
#
#     ex_data = []
#     for i in range(len(data)):
#         lat = data['latitude'][i]
#         lon = data['longitude'][i]
#         if lat == 0 or isna(lat):
#             continue
#         if lon == 0 or isna(lon):
#             continue
#         lat_lon = [lat, lon]
#         g = geocoder.osm(lat_lon, method='reverse')
#         ex_data.append([lat_lon, g.json])
#         print(len(ex_data))
#     ex_data.to_csv(path_or_buf=csv_file_export)


export_full()
# read_data()
