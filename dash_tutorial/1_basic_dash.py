# Dash is the best way to build analytical apps in Python using Plotly figures. To run the app below, 
# run pip install dash, click "Download" to get the code and run python app.py.
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)


app.layout = html.Div([
    html.H4('Life expentancy progression of countries per continents'),
    dcc.Graph(id="graph"),
    dcc.Checklist(
        id="checklist",
        options=["Asia", "Europe", "Africa","Americas","Oceania"],
        value=["Americas", "Oceania"],
        inline=True
    ),
])


@app.callback(
    Output("graph", "figure"), 
    Input("checklist", "value"))
def update_line_chart(continents):
    df = px.data.gapminder() # replace with your own data source
    mask = df.continent.isin(continents)
    fig = px.line(df[mask], 
        x="year", y="lifeExp", color='country')
    return fig


app.run_server(debug=True)