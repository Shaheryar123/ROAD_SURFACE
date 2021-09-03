import arcpy
from arcpy import env
import pandas as pd
import numpy as np
import os

env.workspace=""
print(workspace)


arcpy.CreateFeatureclass_management(workspace,"Road_Surface","POLYGON")
arcpy.AddField_management("SURFACE","UNITID","TEXT","","",16)
arcpy.AddField_management("SURFACE","COMPKEY","DOUBLE")
arcpy.AddField_management("SURFACE","COMPTYPE","DOUBLE")
arcpy.AddField_management("SURFACE","UNITTYPE","TEXT","","",16)
arcpy.AddField_management("SURFACE","LRS_CHAINAGE_START","DOUBLE")
arcpy.AddField_management("SURFACE","LRS_CHAINAGE_END","DOUBLE")
arcpy.AddField_management("SURFACE","SURVEY_ID","TEXT","","",16)
edit_polys=arcpy.da.InsertCursor("SURFACE",['Shape@','COMPKEY','UNITID','UNITTYPE','COMPTYPE','LRS_CHAINAGE_START','LRS_CHAINAGE_END','SURVEY_ID',])
edit_polys.fields

list_coords=[[785549.7673,2562092.0459],[785554.5521,2562084.4988],[785537.3304,2562175.3443],[785458.1128,2562184.1643],[785549.7673,2562092.0459]]
array=arcpy.Array()

for coords in list_coords:
    print (coords)

for coords in list_coords:
    point_obj=arcpy.Point(coords[0],coords[1])
    point_obj.X=coords[0]
    point_obj.Y=coords[1]
    array.add(point_obj)

points_count = array.count
print(points_count)

poly_obj=arcpy.Polygon(array)
polygon_area= poly_obj.area
print(polygon_area)
 
new_row=[poly_obj,'Square Polygon']
edit_polys.insertRow(new_row)
