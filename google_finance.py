import pandas as pd
import datetime
from pandas_datareader import data as web
import matplotlib.pyplot as plt 
from matplotlib import style

style.use('ggplot')

start=datetime.datetime(2017,1,1)
end=datetime.datetime(2017,3,1)

df=web.DataReader("F",'google',start,end)

print(df.head(200))
df.plot()
plt.show()