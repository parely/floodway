import csv
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('gundam1001', 'wa9h2ohwtx')

with open("WaterFlood 2548-2558.csv", "r") as database:
    reader = csv.DictReader(database)
    month1 = {}
    month2 = {}
    month3 = {}
    month4 = {}
    month5 = {}
    month6 = {}
    num = 1
    for i in reader:
        month1.setdefault(num, [i["year"], i["North"]])
        month2.setdefault(num, [i["year"], i["Northeast"]])
        month3.setdefault(num, [i["year"], i["Central"]])
        month4.setdefault(num, [i["year"], i["East"]])
        month5.setdefault(num, [i["year"], i["South North"]])
        month6.setdefault(num, [i["year"], i["South East"]])
        num += 1

    xReader1 = []
    yReader1 = []
    xReader2 = []
    yReader2 = []
    xReader3 = []
    yReader3 = []
    xReader4 = []
    yReader4 = []
    xReader5 = []
    yReader5 = []
    xReader6 = []
    yReader6 = []
    
    for i in sorted(month1):
        xReader1.append(month1[i][0])
        yReader1.append((month1[i][1]))
    for i in sorted(month2):
        xReader2.append(month2[i][0])
        yReader2.append((month2[i][1]))
    for i in sorted(month3):
        xReader3.append(month3[i][0])
        yReader3.append((month3[i][1]))
    for i in sorted(month4):
        xReader4.append(month4[i][0])
        yReader4.append((month4[i][1]))
    for i in sorted(month5):
        xReader5.append(month5[i][0])
        yReader5.append((month5[i][1]))
    for i in sorted(month6):
        xReader6.append(month6[i][0])
        yReader6.append((month6[i][1]))

trace1 = Scatter(x = xReader1, y = yReader1, name = 'ภาคเหนือ')
trace2 = Scatter(x = xReader2, y = yReader2, name = 'ภาคตะวันออกเฉียงเหนือ')
trace3 = Scatter(x = xReader3, y = yReader3, name = 'ภาคกลาง')
trace4 = Scatter(x = xReader4, y = yReader4, name = 'ภาคตะวันออก')
trace5 = Scatter(x = xReader5, y = yReader5, name = 'ภาคใต้ฝั่งตะวันตก')
trace6 = Scatter(x = xReader6, y = yReader6, name = 'ภาคใต้ฝั่งตะวันออก')

data = Data([trace1, trace2, trace3, trace4, trace5, trace6])
plot_url = py.plot(data)
