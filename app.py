import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    [html.H1('This ist a Website represesenting interactive Youtube Data')
     html.H3('Datascience project CAU Kiel')

    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)