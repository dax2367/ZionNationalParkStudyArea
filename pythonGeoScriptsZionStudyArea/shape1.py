import arcpy
from arcpy import env
env.workspace = "L:/Final237eaton"
out_path = "L:/Final237eaton"
out_name = "research_area.shp"
prjfile = "L:/Final237eaton/rivers.prj"
spatial_ref = arcpy.SpatialReference (rivers.prj)
arcpy.Exists("rivers.shp")
arcpy.Exists ("research_area.shp")
Spatialref = arcpy.SpatialReference(prjfile)
arcpy.CreateFeatureclass_management (out_path,out_name,"POLYGON","","","",Spatialref)

