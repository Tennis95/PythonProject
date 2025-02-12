import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"
data = pd.read_excel("/content/ODI world cup.xlsx")
print(data.head())
figure = px.bar(data,
                x=data["Winner"],
                title="Number of Matches Won by teams in ODI World Cup 2023")
figure.show()
won_by = data["won by"].value_counts()
label = won_by.index
counts = won_by.values
colors = ['gold','lightgreen']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Number of Matches Won By Runs Or Wickets')
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()
def func(x):
  x = str(x)
  if x == 'Field' or x == 'field':
    x = 'Bowl'
    return x
  elif x == 'Bat':
    return x

data['Toss decision'] = data['Toss decision'].apply(func)
data['Toss decision'].value_counts().plot.pie(autopct='%.2f')
figure = px.bar(data,
                x=data["top scorer"],
                y = data["highest score"],
                color = data["highest score"],
                title="Top Scorers in ODI World Cup 2023")
figure.show()
figure = px.bar(data,
                x = data["player of the match"],
                title="Player of the Match Awards in ODI World Cup 2023")
figure.show()
fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["Venue"],
    y=data["first innings score"],
    name='First Innings Runs',
    marker_color='blue'
))
fig.add_trace(go.Bar(
    x=data["Venue"],
    y=data["second innings score"],
    name='Second Innings Runs',
    marker_color='red'
))
fig.update_layout(barmode='group',
                  xaxis_tickangle=-45,
                  title="Best Stadiums to Bat First or Chase")
fig.show()
fig = go.Figure()
fig.add_trace(go.Bar(
    x=data["Venue"],
    y=data["first innings wicket"],
    name='First Innings Wickets',
    marker_color='blue'
))
fig.add_trace(go.Bar(
    x=data["Venue"],
    y=data["second innings wicket"],
    name='Second Innings Wickets',
    marker_color='red'
))
fig.update_layout(barmode='group',
                  xaxis_tickangle=-45,
                  title="Best Statiums to Bowl First or Defend")
fig.show()

