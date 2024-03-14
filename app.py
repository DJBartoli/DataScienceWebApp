import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

from dash import callback_context
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)
server = app.server

layout_home = html.Div([
    html.H1('Home'),
    html.P('Welcome to the Home Page!')
])

layout_page1 = html.Div([
    html.H1('Page 1'),
    html.P('Welcome to Page 1!')
])

layout_page2 = html.Div([
    html.H1('Page 2'),
    html.P('Welcome to Page 2!')
])

navbar = html.Div([
    dcc.Link('Home ', href='/'),
    dcc.Link('Page 1 ', href='/page-1'),
    dcc.Link('Page 2 ', href='/page-2')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return layout_page1
    elif pathname == '/page-2':
        return layout_page2
    else:
        return layout_home

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
    [html.H1('This ist a Website represesenting interactive Youtube Data'),
    html.H3('Datascience project CAU Kiel')

    ]
])

if __name__ == '__main__':
    app.run_server(debug=True)