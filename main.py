import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy

req_content = req.content

csv = open('C:\\temp\\data.csv', 'wb')
csv.write(req_content)
data = pd.read_csv('C:\\temp\\data.csv')

data.rename({'GMT MKT Interval': "DatetimeEST"}, axis=1, inplace=True)

print(data.head(10))
print(data.head(10))

avg = data.groupby('Date').mean()

print(avg.head(10))

plot = plt.plot(avg)
plt.show()
