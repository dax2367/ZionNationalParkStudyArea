import arcpy
from arcpy import env
env.workspace = "L:/Final237eaton"
arcpy.Clip_analysis("rivers","park_boundary","river_clip")
arcpy.Clip_analysis("roads", "park_boundary","roads_clip")

