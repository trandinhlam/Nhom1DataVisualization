import pandas as pd
from shapely import geometry
from osgeo import ogr
import config as cfg
from util.write_shape import write_shape


def _load_points(file_name):
    points = pd.read_csv(file_name)
    return points


dict_roads = {}
for road in cfg.main_roads:
    print(road)
    file_name = f'data/export/polygons/{road}.csv'
    points = _load_points(file_name)
    print(len(points))
    for index, row in points.iterrows():
        dict_roads.setdefault(road, []).append([row['Latitude'], row['Longitude']])
    write_shape(dict_roads, out_file_name='manual_line_main_roads')


