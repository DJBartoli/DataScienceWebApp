import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import dash
from dash import dcc, html, callback
import plotly.express as px

from geopy.geocoders import Nominatim
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import json
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Covid Comments')


COVID_COMMENTS = pd.read_csv(r'data/covidComments/comments_with_emotions.csv')

layout = html.Div([
    dbc.Row(
        [
            dbc.Col(
                children=[html.H2('Covid Comments', style={'color': '#dd2b2b'}),
                          html.H3(
                              'How has the mood among the Youtube comments changed during the course of the covid19 pandemic?'),
                          ],
                width={'size': 6, 'offset': 3},

            ),
        ]
    ),
    dbc.Row([
        dbc.Col(
            children=[

                dcc.Dropdown(

                ),
            ],
            width={'size': 6, 'offset': 3},
            style={'color': '#121212'}
        ),
    ]),
    dbc.Row([
        dbc.Col(
            children=[

            ],
            width={'size': 5, 'offset': 3},
            style={'margin-top': '5px'},
        ),

    ]),
    dbc.Row([
        dbc.Col(
            children=[

                dcc.Graph(id='graph'),

            ],
            width={'size': 6, 'offset': 3},
            style={'padding': '5px', 'background-color': 'white', 'border-radius': '10px',
                   'box-shadow': '0px 2px 5px #949494'},
        )
    ],

    ),

])


