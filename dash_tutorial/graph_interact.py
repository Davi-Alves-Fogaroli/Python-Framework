from dash import html, dash, dcc, Input, Output
from plotly import graph_objs as go
import plotly
from collections import deque
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children="Go"),
    dcc.Input(id="input", value="", type="text"),
    html.Div(id="output-graph"),
    dcc.Graph(id="live-graph", animate=True),
    dcc.Interval(id="graph-update", interval=1*1000),
])

#####################
##### real_time #####
#####################

@app.callback(Output("live-graph", "figure"),
              [Input("graph-update", "n_intervals")]
              )
def update_graph_scatter(input_data):
    with open("data_file.json", "r") as file:
        df = pd.read_json(file)
        df.set_index("time", inplace=True)
        x_data=df["time"].tolist()
        y_data=df["temperature"].tolist()
        data = plotly.graph_objs.Scatter(
                x=x_data,
                y=y_data,
                name="Scattter",
                mode="lines+markers",
        )

    return {"data": [data], "layout": go.Layout(xaxis=dict(range=[min(x_data),max(x_data)]),
                                                yaxis=dict(range=[min(y_data),max(y_data)]),
                                                )}

##########################
##### graph_interact #####
##########################

# @app.callback(
#     Output(component_id="output-graph", component_property="children"),
#     [Input(component_id="input", component_property="value")]   
# )
# def update_graph(input_data):
    with open("data_file.json", "r") as file:
        df = pd.read_json(file)
        df.set_index("time", inplace=True)
        
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': df.index, 'y': df, 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': input_data
            }
        }
    )

if __name__ =="__main__":
    app.run_server(debug=True)