import csv
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('aul99999', 'YJdLMTY53oqOanHFhxrw')

with open("oil1.csv", "r") as database:
    reader = csv.DictReader(database)
    month = {}
    num = 1
    for i in reader:
        month.setdefault(num, [i["YEAR"], i["2555"]])
        num += 1

    xReader = []
    yReader = []
    for i in sorted(month):
        xReader.append(month[i][0])
        yReader.append(month[i][1])

trace1 = Scatter(x = xReader, y = yReader)

data = Data([trace1])
plot_url = py.plot(data)
