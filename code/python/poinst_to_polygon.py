import math

import pandas as pd
from shapely import geometry
from osgeo import ogr, osr

import util.write_shape as ws


def polygon_data():
    csv_file = './data/export/f.csv'
    data = pd.read_csv(csv_file)

    map_point_dict = {}
    for i in range(len(data)):
        lat = data['latitude'][i]
        lon = data['longitude'][i]
        road = data['main_road'][i]
        if math.isnan(lat) or math.isinf(lat) or math.isnan(lon) or math.isinf(lon):
            continue
        map_point_dict.setdefault(road, []).append([lat, lon])

    polygons = []
    final_dict = {}

    for key in map_point_dict:
        if len(map_point_dict[key]) > 1_000:
            points = map_point_dict[key]
            final_dict.setdefault(key, points)
            poly = geometry.Polygon([[p[0], p[1]] for p in points])
            # print(poly)
            polygons.append(poly)
    ws.write_shape(final_dict, out_file_name='la_main_road_polygon_4')


polygon_data()
