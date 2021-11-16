import math

import pandas as pd
from shapely import geometry
from osgeo import ogr, osr


def create_poly(poly):
    # list.sort(poly, reverse=True)
    ring = ogr.Geometry(ogr.wkbLineString)
    for i in range(len(poly)):
        point = poly[i]
        ring.AddPoint(point[1], point[0])
    return ring
    # poly = ogr.Geometry(ogr.wkbPolygon)
    # poly.AddGeometry(ring)
    # return poly


def write_shape(dict_polygons, out_file_name):
    # Now convert it to a shapefile with OGR
    driver = ogr.GetDriverByName('Esri Shapefile')
    ds = driver.CreateDataSource(f'./shape/{out_file_name}.shp')
    # srs = osr.SpatialReference()
    # srs.ImportFromEPSG(4326)
    layer = ds.CreateLayer("line", None, ogr.wkbLineString)
    idField = ogr.FieldDefn("id", ogr.OFTString)
    layer.CreateField(idField)
    for key in dict_polygons:
        define = layer.GetLayerDefn()
        # Create a new feature (attribute and geometry)
        feat = ogr.Feature(define)
        feat.SetField('id', key)
        # parse poly
        poly = dict_polygons[key]
        geo_poly = create_poly(poly)
        # Make a geometry, from Shapely object
        feat.SetGeometry(geo_poly)
        layer.CreateFeature(feat)
        # destroy these
        feat = geom = None
    # Save and close everything
    ds = layer = feat = geom = None
