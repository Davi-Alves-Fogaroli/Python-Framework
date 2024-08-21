from dash import Dash, html, dash_table, dcc, Output, Input, callback
import plotly.express as px
import pandas as pd

# Static App
# Connecting to Data; Visualizing Data; Controls and Callbacks

# Take data
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv")

# Initialize the app
app = Dash()

# App layout, here is located all components will be exhibit in the web browser
app.layout = [
    html.Div(children="My first App with Data"),
    html.Hr(),
    dash_table.DataTable(data=df.to_dict("records"), page_size=6),
    dcc.RadioItems(options=["pop", "lifeExp", "gdpPercap"], value="lifeExp", id="controls-and-radio-item"),
    # dcc.Graph(figure=px.histogram(df, x="continent", y="lifeExp", histfunc="avg"))
    dcc.Graph(figure={}, id="controls-and-graph")
    ]

# Add controls to build the interaction
@callback(
    Output(component_id="controls-and-graph", component_property="figure"),
    Input(component_id="controls-and-radio-item", component_property="value")
)
def update_graph(col_chosen):
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig


# Run the app
if __name__ == "__main__":
    app.run(debug=True)