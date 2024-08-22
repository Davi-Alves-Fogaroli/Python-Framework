import pandas as pd
from dash import html, dash, dcc, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children="Go"),
    dcc.Input(id="input", value="", type="text"),
    html.Div(id="output-graph")
])

@app.callback(
    Output(component_id="output-graph", component_property="children"),
    [Input(component_id="input", component_property="value")]   
)
def update_graph(input_data):
    with open("data_file.json", "r") as file:
        df = pd.read_json(file)
        # print(df.head())
        # time = df["time"].tolist()
        # pressure = df["pressure"].tolist()
        # app = dash.Dash()
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