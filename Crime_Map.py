# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 22:52:04 2022

@author: admin
"""

import pandas as pd
import geopandas as gpd
import folium
from folium import Choropleth,Circle,Marker
from folium.plugins import HeatMap,MarkerCluster

m_1 = folium.Map(location=[42.32,-71.0589], tiles='openstreetmap', zoom_start=10)
m_1
