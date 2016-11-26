import csv
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('aul99999', 'YJdLMTY53oqOanHFhxrw')

with open("Rubber.csv", "r") as database:
    reader = csv.DictReader(database)
    month = {}
    num = 1
    for i in reader:
        month.setdefault(num, [i["YEAR"], i["2558"]])
        num += 1

    xReader = []
    yReader = []
    for i in sorted(month):
        xReader.append(month[i][0])
        yReader.append(int(month[i][1]))

trace1 = Scatter(x = xReader, y = yReader)

data = Data([trace1])
plot_url = py.plot(data)
