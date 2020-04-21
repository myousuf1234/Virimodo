import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv(r'C:\Users\owner\Projects_V\hourlevel.csv')



fig = px.line(df, x='Time Bucket (America/New_York)', y='Main (kWh)')
fig.update_layout(title = 'Hour Level Data with Peak levels highlighted', xaxis=dict(title='Time by hour'),
                  yaxis=dict(title="Kilowat Hours"))

fig.update_layout(xaxis_rangeslider_visible=True)


fig.add_shape(
        # Line Horizontal
            type="rect",
            x0=0,
            y0=0,
            x1=16,
            y1=4.5,
            fillcolor='red',
            opacity=0.5,
            line_width=0,
            layer='below'
    )

fig.add_shape(
        # Line Horizontal
            type="rect",
            x0=24,
            y0=0,
            x1=40,
            y1=4.5,
            fillcolor='red',
            opacity=0.5,
            line_width=0,
            layer='below'
    )

fig.add_shape(
        # Line Horizontal
            type="rect",
            x0=48,
            y0=0,
            x1=64,
            y1=4.5,
            fillcolor='red',
            opacity=0.5,
            line_width=0,
            layer='below'
    )

fig.add_shape(
        # Line Horizontal
            type="rect",
            x0=72,
            y0=0,
            x1=88,
            y1=4.5,
            fillcolor='red',
            opacity=0.5,
            line_width=0,
            layer='below'
    )


fig.add_shape(
        # Line Horizontal
            type="rect",
            x0=96,
            y0=0,
            x1=100,
            y1=4.5,
            fillcolor='red',
            opacity=0.5,
            line_width=0,
            layer="below"
    )
fig.show()