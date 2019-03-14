import arcpy
from arcpy import env
env.workspace = "L:/Final237eaton"
buffinput = "ranger_station.shp"
buffoutput = "station_buff.shp"
arcpy.Buffer_analysis(buffinput, buffoutput, "6 MILES", "", "", "ALL")
buffoutput = "station_buff"
buffinput = "ranger_station"
arcpy.Buffer_analysis(buffinput, buffoutput, "6 MILES", "", "", "ALL")

