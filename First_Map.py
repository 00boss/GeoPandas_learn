import pandas as pd
import geopandas as gpd

'''
GeoDataFrame 和DataFrame 类型类似
DF可以使用的方法GDF基本也可以使用
'''

#用gpd 读取.shp文件该文件夹下的所有文件才是一个完整的shapefile
world_loans = gpd.read_file("kiva_loans/kiva_loans/kiva_loans.shp")

# 该数据集在GeoPandas中提供
world_filepath = gpd.datasets.get_path('naturalearth_lowres')
#加载包含国家边界的GeoDataFrame世界.
world = gpd.read_file(world_filepath)

#使用world和world_loans GeoDataFrames可视化Kiva在世界各地的贷款位置。
ax = world.plot(figsize=(10,10),color='white',linestyle=':',edgecolor='black')
world_loans.plot(ax=ax,markersize=2)

#获取worl_loand 部分数据,获取菲律宾的数据
PHL_loans = world_loans.loc[world_loans.country.isin(['Philippines'])].copy()

#加载包含岛屿边界的KML文件
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
PHL = gpd.read_file("Philippines_AL258.kml\Philippines_AL258.kml", driver='KML')

#制作菲律宾贷款地图可视化,背景颜色,标记类型,边界颜色
ax = PHL.plot(figsize=(10,10),color='white',linestyle=':',edgecolor='black')
PHL_loans.plot(ax=ax,markersize=3)









