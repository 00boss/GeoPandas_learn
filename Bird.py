import geopandas as gpd
import pandas as pd
from shapely.geometry import LineString

#加载GPS数据
birds_df = pd.read_csv('purple_martin.csv',parse_dates=['timestamp'])
print('共有{}只鸟'.format(birds_df["tag-local-identifier"].nunique()))

#将df对象转换成gdf对象,传入df对象和使用point_from_xy方法传入经度和维度制造出geometry列
birds = gpd.GeoDataFrame(birds_df,geometry=gpd.points_from_xy(birds_df["location-long"],birds_df["location-lat"]))

#设置crs下面两句等价
#birds.crs = {'init','epsg:4326'}
birds.crs = "+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs"

#设置crs后修改crs
birds.to_crs(epsg=4326)

#从geopandas加载世界的数据
wold = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
#获取美洲所有国家（包括北美和南美）边界的地理数据
americas = wold.loc[wold['continent'].isin(['North America', 'South America'])]

#绘制小鸟在美洲到达过的地方
ax = americas.plot(figsize=(10,10),color='whitesmoke',linestyle=':',edgesolor='black') #地图
birds.plot(ax=ax,markersize=10) #小鸟位置标记

#显示每只鸟的路径
path_df = birds.groupby('tag-local-identifier')['geometry'].apply(list).apply(lambda x:lineString(x)).reset_index()
path_gdf = gpd.GeoDataFrame(path_df,geometry=path_df.geometry)
path_gdf.crs = {'init':'epsg:4326'}

#每只鸟的起点
start_df = birds.groupby('tag-local-identifier')['geometry'].apply(list).apply(lambda x:x[0]).reset_index()
start_gdf = gpd.GeoDataFrame(start_df,geometry=start_df.geometry)
start_gdf.crs = {'init':'epsg:4326'}

#每只鸟的终点
end_df = birds.groupby('tag-local-identifier')['geometry'].apply(list).apply(lambda x:x[-1]).reset_index()
end_gdf = gpd.GeoDataFrame(end_df,geometry=end_df.geometry)
end_gdf.crs = {'init':'epsg:4326'}

#绘制每只鸟的旅行路线
ax = americas.plot(figsize=(10,10),color='white',linestyle=':',edgecolor='black')
start_gdf.plot(ax=ax,markersize=30,color='red')
path_gdf.plot(ax=ax,cmap='tab20b',linestyle='-',linewidth=1,zorder=1)#最后一个参数决定显示一半路径还是全部路径
end_gdf.plot(ax=ax,markersize=30,color='blue')











