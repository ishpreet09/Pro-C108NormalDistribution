import pandas as pd
import plotly.figure_factory as pf

df=pd.read_csv("D:/DATA DESKTOP/Notes Of Code/Python/Homework/Pro-C108NormalDistribution/mobil_brand.csv")
fig=pf.create_distplot([df["Avg Rating"].to_list()],["Average Rating"])
fig.show()