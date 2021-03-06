import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('parely', 'wvpbvlh3yd')
trace1 = go.Bar(
    x=['ภาคเหนือ', 'ภาคตะวันออกเฉียงเหนือ', 'ภาคกลาง', 'ภาคตะวันออก', 'ภาคใต้ฝั่งตะวันตก', 'ภาคใต้ฝั่งตะวันออก'],
     y=[1314, 1212, 1212, 1657, 1937, 1678],
    name='ปี2548',
    marker=dict(
        color='9966CC'
    )
)
trace2 = go.Bar(
    x=['ภาคเหนือ', 'ภาคตะวันออกเฉียงเหนือ', 'ภาคกลาง', 'ภาคตะวันออก', 'ภาคใต้ฝั่งตะวันตก', 'ภาคใต้ฝั่งตะวันออก'],
    y=[1314, 1212, 1212, 1657, 1937, 1678],
    name='ปี2549',
    marker=dict(
        color='FF9900'
    )
)
trace3 = go.Bar(
    x=['ภาคเหนือ', 'ภาคตะวันออกเฉียงเหนือ', 'ภาคกลาง', 'ภาคตะวันออก', 'ภาคใต้ฝั่งตะวันตก', 'ภาคใต้ฝั่งตะวันออก'],
    y=[1262, 1452, 1168, 1668, 2465, 1954],
    name='ปี2550',
    marker=dict(
        color='66CC33'
    )
)
trace4 = go.Bar(
    x=['ภาคเหนือ', 'ภาคตะวันออกเฉียงเหนือ', 'ภาคกลาง', 'ภาคตะวันออก', 'ภาคใต้ฝั่งตะวันตก', 'ภาคใต้ฝั่งตะวันออก'],
    y=[1360, 1518, 1278, 1937, 2216, 1932],
    name='ปี2551',
    marker=dict(
        color='FFFF33'
    )
)
trace5 = go.Bar(
    x=['ภาคเหนือ', 'ภาคตะวันออกเฉียงเหนือ', 'ภาคกลาง', 'ภาคตะวันออก', 'ภาคใต้ฝั่งตะวันตก', 'ภาคใต้ฝั่งตะวันออก'],
    y=[1136, 1364, 1279, 1783, 2320, 812],
    name='ปี2552',
    marker=dict(
        color='FF6666'
    )
)
trace6 = go.Bar(
    x=['ภาคเหนือ', 'ภาคตะวันออกเฉียงเหนือ', 'ภาคกลาง', 'ภาคตะวันออก', 'ภาคใต้ฝั่งตะวันตก', 'ภาคใต้ฝั่งตะวันออก'],
    y=[1264, 1300, 1255, 1738, 2309, 1988],
    name='ปี2553',
    marker=dict(
        color='33CCCC'
    )
)
trace7 = go.Bar(
    x=['ภาคเหนือ', 'ภาคตะวันออกเฉียงเหนือ', 'ภาคกลาง', 'ภาคตะวันออก', 'ภาคใต้ฝั่งตะวันตก', 'ภาคใต้ฝั่งตะวันออก'],
    y=[1738, 1662, 1375, 2037, 2889, 2530],
    name='ปี2554',
    marker=dict(
        color='993333'
    )
)
trace8 = go.Bar(
    x=['ภาคเหนือ', 'ภาคตะวันออกเฉียงเหนือ', 'ภาคกลาง', 'ภาคตะวันออก', 'ภาคใต้ฝั่งตะวันตก', 'ภาคใต้ฝั่งตะวันออก'],
    y=[128, 1262, 1247, 1921, 2904, 2083],
    name='ปี2555',
    marker=dict(
        color='663399'
    )
)
trace9 = go.Bar(
    x=['ภาคเหนือ', 'ภาคตะวันออกเฉียงเหนือ', 'ภาคกลาง', 'ภาคตะวันออก', 'ภาคใต้ฝั่งตะวันตก', 'ภาคใต้ฝั่งตะวันออก'],
    y=[1329, 1457, 1222, 2236, 2769, 2107],
    name='ปี2555',
    marker=dict(
        color='CC6633'
    )
)
data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9]
layout = go.Layout(
    title='ปริมาณฝนสะสม',
    xaxis=dict(
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    yaxis=dict(
        title='ปริมาณน้ำฝน(มิลลิเมตร)',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='style-bar')
