import os
from datetime import datetime, timedelta
import json

import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

from geopy.geocoders import Nominatim
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import json
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True)

server = app.server

app.layout = html.Div(
    [
        html.Div([
            dbc.NavbarSimple(
                children=[
                    dbc.NavItem(dbc.NavLink(page['name'], href=page['path']))
                    for page in dash.page_registry.values()
                ],
                brand="Visualizing YouTube",
                brand_href="#",
                color="#dd2b2b",
                dark=True,
            )
        ]),
        html.Hr(),
        dash.page_container
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
# ------------------------------------------------------------------------------
# Starting the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)
