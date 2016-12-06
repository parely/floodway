import csv
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('gundam1001', 'wa9h2ohwtx')

with open("oil_year.csv", "r") as database:
    reader = csv.DictReader(database)
    month = {}
    num = 1
    for i in reader:
        month.setdefault(num, [i["YEAR"], i["PRICE"]])
        num += 1

    xReader = []
    yReader = []
    for i in sorted(month):
        xReader.append(month[i][0])
        yReader.append(month[i][1])

trace1 = Scatter(x = xReader, y = yReader)

data = Data([trace1])
plot_url = py.plot(data)
