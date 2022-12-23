import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("dsp.csv")

highest = 0
lowest = 1000
for i in (range(len(df))):
    if(df["High"].iloc[i] > highest):
        highest = df["High"].iloc[i]
        highesttime = i
        print(highest)
    if(df["Low"].iloc[i] < lowest):
        lowest = df["Low"].iloc[i]
        lowesttime = i

localmax = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0]
localmaxtime = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0]
localmin = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,100, 100, 100, 100, 100, 100,100,100,100,100, 100,100,100,100,100, 100,100,100,100,100]
localmintime = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0]

for y in range(38):
    for i in range(140*y,140*(y+1)):
        if (df["High"].iloc[i] > localmax[y]):
            localmax[y] = df["High"].iloc[i]
            localmaxtime[y] = i
        if (df["Low"].iloc[i] < localmin[y]):
            localmin[y] = df["Low"].iloc[i]
            localmintime[y] = i

fig = go.Figure(data=[go.Candlestick(x=df["Time"],
                open=df['Open'], high=df['High'],
                low=df['Low'], close=df['Close'])
                     ])
##ALL MAX
fig.add_traces(
    go.Scatter(
        x=[df["Time"][0],df["Time"][highesttime],df["Time"][len(df)-1]],
        y=[highest,highest,highest], line = {'color':'orange','width':2},name= "GLOBAL MAX"
    ))

## ALL MIN
fig.add_traces(
    go.Scatter(
        x=[df["Time"][0],df["Time"][lowesttime],df["Time"][len(df)-1]],
        y=[lowest,lowest,lowest], line = {'color':'black','width':2},name= "GLOBAL MIN"
    ))

## Global Destek Çizgisi:
fig.add_traces(
    go.Scatter(
        x=[df['Time'][localmintime[ 0 ]],df['Time'][localmintime[ 1 ]],df['Time'][localmintime[ 2 ]],df['Time'][localmintime[ 3 ]],df['Time'][localmintime[ 4 ]],df['Time'][localmintime[ 5 ]],df['Time'][localmintime[ 6 ]], \
        df['Time'][localmintime[ 7 ]],df['Time'][localmintime[ 8 ]],df['Time'][localmintime[ 9 ]],df['Time'][localmintime[ 10 ]],df['Time'][localmintime[ 11 ]],df['Time'][localmintime[ 12 ]],df['Time'][localmintime[ 13 ]],df['Time'][localmintime[ 14 ]],\
        df['Time'][localmintime[ 15 ]],df['Time'][localmintime[ 16 ]],df['Time'][localmintime[ 17 ]],df['Time'][localmintime[ 18 ]],\
        df['Time'][localmintime[ 19 ]],df['Time'][localmintime[ 20 ]],df['Time'][localmintime[ 21 ]],df['Time'][localmintime[ 22 ]],df['Time'][localmintime[ 23 ]],df['Time'][localmintime[ 24 ]],df['Time'][localmintime[ 25 ]],df['Time'][localmintime[ 26 ]],df['Time'][localmintime[ 27 ]],df['Time'][localmintime[ 28 ]],df['Time'][localmintime[ 29 ]],df['Time'][localmintime[ 30 ]],\
        df['Time'][localmintime[ 31 ]],df['Time'][localmintime[ 32 ]],df['Time'][localmintime[ 33 ]],df['Time'][localmintime[ 34 ]],df['Time'][localmintime[ 35 ]],df['Time'][localmintime[ 36 ]],df['Time'][localmintime[ 37 ]]],
        y=[localmin[ 0 ],localmin[ 1 ],localmin[ 2 ],localmin[ 3 ],localmin[ 4 ],localmin[ 5 ],localmin[ 6 ],localmin[ 7 ],localmin[ 8 ],localmin[ 9 ],\
        localmin[ 10 ],localmin[ 11 ],localmin[ 12 ],localmin[ 13 ],localmin[ 14 ],localmin[ 15 ],localmin[ 16 ],\
        localmin[ 17 ],localmin[ 18 ],localmin[ 19 ],localmin[ 20 ],localmin[ 21 ],localmin[ 22 ],localmin[ 23 ],\
        localmin[ 24 ],localmin[ 25 ],localmin[ 26 ],localmin[ 27 ],localmin[ 28 ],localmin[ 29 ],localmin[ 30 ],\
        localmin[ 31 ],localmin[ 32 ],localmin[ 33 ],localmin[ 34 ],localmin[ 35 ],localmin[ 36 ],localmin[ 37 ]], line={'color': 'lime', 'width':10,'shape':'spline'}, opacity=0.3, name="DESTEK"
    ))

## Global Direnç

fig.add_traces(
    go.Scatter(
        x=[df['Time'][localmaxtime[ 0 ]],df['Time'][localmaxtime[ 1 ]],df['Time'][localmaxtime[ 2 ]],df['Time'][localmaxtime[ 3 ]],df['Time'][localmaxtime[ 4 ]],df['Time'][localmaxtime[ 5 ]],df['Time'][localmaxtime[ 6 ]], \
        df['Time'][localmaxtime[ 7 ]],df['Time'][localmaxtime[ 8 ]],df['Time'][localmaxtime[ 9 ]],df['Time'][localmaxtime[ 10 ]],df['Time'][localmaxtime[ 11 ]],df['Time'][localmaxtime[ 12 ]],df['Time'][localmaxtime[ 13 ]],df['Time'][localmaxtime[ 14 ]],\
        df['Time'][localmaxtime[ 15 ]],df['Time'][localmaxtime[ 16 ]],df['Time'][localmaxtime[ 17 ]],df['Time'][localmaxtime[ 18 ]],\
        df['Time'][localmaxtime[ 19 ]],df['Time'][localmaxtime[ 20 ]],df['Time'][localmaxtime[ 21 ]],df['Time'][localmaxtime[ 22 ]],df['Time'][localmaxtime[ 23 ]],df['Time'][localmaxtime[ 24 ]],df['Time'][localmaxtime[ 25 ]],df['Time'][localmaxtime[ 26 ]],df['Time'][localmaxtime[ 27 ]],df['Time'][localmaxtime[ 28 ]],df['Time'][localmaxtime[ 29 ]],df['Time'][localmaxtime[ 30 ]],\
        df['Time'][localmaxtime[ 31 ]],df['Time'][localmaxtime[ 32 ]],df['Time'][localmaxtime[ 33 ]],df['Time'][localmaxtime[ 34 ]],df['Time'][localmaxtime[ 35 ]],df['Time'][localmaxtime[ 36 ]],df['Time'][localmaxtime[ 37 ]]],
        y=[localmax[ 0 ],localmax[ 1 ],localmax[ 2 ],localmax[ 3 ],localmax[ 4 ],localmax[ 5 ],localmax[ 6 ],localmax[ 7 ],localmax[ 8 ],localmax[ 9 ],\
        localmax[ 10 ],localmax[ 11 ],localmax[ 12 ],localmax[ 13 ],localmax[ 14 ],localmax[ 15 ],localmax[ 16 ],\
        localmax[ 17 ],localmax[ 18 ],localmax[ 19 ],localmax[ 20 ],localmax[ 21 ],localmax[ 22 ],localmax[ 23 ],\
        localmax[ 24 ],localmax[ 25 ],localmax[ 26 ],localmax[ 27 ],localmax[ 28 ],localmax[ 29 ],localmax[ 30 ],\
        localmax[ 31 ],localmax[ 32 ],localmax[ 33 ],localmax[ 34 ],localmax[ 35 ],localmax[ 36 ],localmax[ 37 ]], line={'color': 'dodgerblue', 'width':10,'shape':'spline'}, opacity=0.9, name="DİRENÇ"
    ))

##

for i in range(38):
    fig.add_traces(go.Scatter(
        x=[df["Time"][localmaxtime[i] - 10], df["Time"][localmaxtime[i]], df["Time"][localmaxtime[i] + 10]],
        y=[localmax[i], localmax[i], localmax[i]], line={'color': 'green', 'width': 2}, name=("LocalMax"+str(i))
    ))

    fig.add_traces(
        go.Scatter(
            x=[df["Time"][localmintime[i] - 10], df["Time"][localmintime[i]], df["Time"][localmintime[i] + 10]],
            y=[localmin[i], localmin[i], localmin[i]], line={'color': 'red', 'width': 2}, name=("LocalMin"+ str(i))
        ))

for i in range(38):
    print("localmin[",i,"],")




'''fig.add_trace(go.Scatter(
    x=x+x_rev,
    y=y1_upper+y1_lower,
    fill='toself',
    fillcolor='rgba(0,100,80,0.2)',
    line_color='rgba(255,255,255,0)',
    showlegend=False,
    name='Fair',
))
'''

partial_localmax = np.zeros((38,14,2))
partial_localmin = np.ones((38,14,2))
partial_lists = np.zeros((38,28,2))
for z in range(38):
    p=z*140
    for y in range(14):

        for i in range(10):
            if(df["High"].iloc[i+20*y+p] > partial_localmax[z][y][0]):
                    partial_localmax[z][y][0] = df["High"].iloc[i+20*y+p]
                    partial_localmax[z][y][1] = i+20*y+p
            if(df["Low"].iloc[i+20*y+p] < partial_localmin[z][y][0]):
                    partial_localmin[z][y][0] = df["Low"].iloc[i+20*y+p]
                    partial_localmin[z][y][1] = i+20*y+p
        partial_lists[z][2*y] = partial_localmax[z][y]
        partial_lists[z][2*y+1]=partial_localmin[z][y]

    for k in range(7):
        fig.add_traces(
            go.Scatter(
                x=[df["Time"][partial_localmax[z][k][1]]],
                y=[partial_localmax[z][k][0]], line = {'color':'black','width':8},name= "PARTIAL MAX"
            ))
        fig.add_traces(
            go.Scatter(
                x=[df["Time"][partial_localmin[z][k][1]]],
                y=[partial_localmin[z][k][0]], line = {'color':'black','width':8},name= "PARTIAL MIN"
            ))





for i in range(38):
        a = (sorted(partial_lists[i], key = lambda x: x[0]))
        percentage = (localmax[i]/localmin[i])*0.01
        mapperx = 2.07*percentage
        mapper = a[0][0]*mapperx
        gap = [0,0,0,0,0,0,0,0,0,0]
        mapped = [a[0][0], a[0][0]+mapper,a[0][0]+2*mapper,a[0][0]+3*mapper,a[0][0]+4*mapper,a[0][0]+5*mapper,a[0][0]+6*mapper,a[0][0]+7*mapper,a[0][0]+8*mapper,a[0][0]+9*mapper,a[0][0]+10*mapper]
        for y in range(28):
            if(mapped[0]<a[y][0]<mapped[1]):
                gap[0] = gap[0]+1
            elif(mapped[1]<a[y][0]<mapped[2]):
                gap[1] = gap[1]+1
            elif(mapped[2]<a[y][0]<mapped[3]):
                gap[2] = gap[2]+1
            elif(mapped[3]<a[y][0]<mapped[4]):
                gap[3] = gap[3]+1
            elif(mapped[4]<a[y][0]<mapped[5]):
                gap[4] = gap[4]+1
            elif(mapped[5]<a[y][0]<mapped[6]):
                gap[5] = gap[5]+1
            elif(mapped[6]<a[y][0]<mapped[7]):
                gap[6] = gap[6]+1
            elif(mapped[7]<a[y][0]<mapped[8]):
                gap[7] = gap[7]+1
            elif(mapped[8]<a[y][0]<mapped[9]):
                gap[8] = gap[8]+1
            elif(mapped[9]<a[y][0]<mapped[10]):
                gap[9] = gap[9]+1

        c= gap.index(max(gap))
        print(mapperx)
        fig.add_traces(
            go.Scatter(
                x=[df["Time"][0+i*140] , df["Time"][140+i*140]],
                y=[((mapped[c]+mapped[c+1])/2),((mapped[c]+mapped[c+1])/2)], line = {'color':'pink','width':35},opacity=0.8,name= "PARTIAL MIN"
            ))
        fig.add_traces(
            go.Scatter(
                x=[df["Time"][0+i*140] , df["Time"][140+i*140]],
                y=[mapped[c],mapped[c]], fill=None, mode = 'lines' , line_color = 'indigo',name= "PARTIAL MIN"
            ))

        fig.add_traces(
            go.Scatter(
                x=[df["Time"][0+i*140] , df["Time"][140+i*140]],
                y=[mapped[c+1],mapped[c+1]], fill='tonexty', mode = 'lines' , line_color = 'indigo',name= "PARTIAL MIN"
            ))





fig.update_traces(selector=dict(type='scatter'))
fig.update_layout(xaxis_rangeslider_visible=False)
fig.show()
