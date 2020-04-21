import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv(r'C:\Users\owner\Projects_V\rec_costs.csv')
df['text'] = df['state'] + ", " + df['text']


fig = go.Figure(data=go.Choropleth(
    text =df['text'],
    locations=df['code'], # Spatial coordinates
    z = df['rec cost'].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Greens',
    colorbar_title = "USD",
))

fig.update_layout(
    title_text = 'Renewable Energy Credit Price by State (Dollars per MWH)',
    geo_scope='usa', #limit map scope to USA
)

fig.show()

print("Last updated April 21st")
