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

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('Introducing the YouTube API', style ={'text-align': 'center','color': '#dd2b2b'}),
    dbc.Col(style={'height':'50px'}),
    dbc.Col(html.H4('''
            Lorem ipsum dolor sit amet, consetetur sadipscing elitr,
            sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
            sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum.
            Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
            Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor
            invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
            At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
            no sea takimata sanctus est Lorem ipsum dolor sit amet.
            '''),
        className='text-center',
        width={'size':4,'offset':4}
    ),
    dbc.Col(style={'height':'50px'}),
    dbc.Row(
        [
            dbc.Col(html.Hr(style={'margin': '20px 0', 'border': 'none', 'border-top': '1px solid #ccc'}),
                width={'size':10, 'offset':1}
                )
        ]
    ),
    dbc.Row(dbc.Col(html.H1('Topics with Research Questions'),className='text-center align-self-end', style={'color': '#dd2b2b'})),
    dbc.Row(style={'height':'50px'}),
    dbc.Row(
        [   
            dbc.Col(
                [   html.Div(html.H4("User Interaction & Duration")),
                    html.Hr(style={'margin': '10px 0', 'border': 'none', 'border-top': '1px solid #ccc'}),
                    html.Ul([
                        html.Li(['Are there any visible differences in engagement on videos between different categories? ', 
                        html.A("Here", href="/categoriesinteractions")], 
                        style={'text-align': 'left'}),
                        html.Br(),
                        html.Li(['How does the comment behaviour develop after the video is published? ',
                        html.A("Here", href="/commentbehavior")],
                        style={'text-align': 'left'}),
                        html.Br(),
                        html.Li(['How has the mood among the Youtube comments changed during the course of the covid19 pandemic? ', 
                        html.A("Here", href="/covidcomments")], 
                        style={'text-align': 'left'})
                    ])
                ],  
                        style={'padding': '8px', 'background-color': '#2e2d2d',
                        'border-radius': '10px', 'box-shadow': '0px 2px 5px #4d4c4c'},
                        width={'size':2,'offset':0},
                        className='text-center',
                    ),
            dbc.Col(width=1),
            dbc.Col(
                [   html.Div(html.H4("Content Analysis & Engagement")),
                    html.Hr(style={'margin': '10px 0', 'border': 'none', 'border-top': '1px solid #ccc'}),
                    html.Ul([
                        html.Li(['How does the length of a Youtube Video affect the viewers engagement measured by likes and comments? ',
                        html.A("Here", href="/durationinteractions")],
                        style={'text-align': 'left'}),
                        html.Br(),
                        html.Li(['Question 7: How has the average video length developed over the last 10 years? ',
                        html.A("Here", href="/videolength")],
                        style={'text-align': 'left'}),
                    ])
                ],
                        style={'padding': '8px', 'background-color': '#2e2d2d',
                        'border-radius': '10px', 'box-shadow': '0px 2px 5px #4d4c4c'},
                        width={'size':2,'offset':0},
                        className='text-center',
                    ),
            dbc.Col(width=1),
            dbc.Col([html.Div(html.H4("Trends & Insights")),
                    html.Hr(style={'margin': '10px 0', 'border': 'none', 'border-top': '1px solid #ccc'}),
                    html.Ul([
                        html.Li(['How does the category distribution among the top 100 videos differ in the various regions and locations? ',
                        html.A("Here", href="/trendscategorys")],
                        style={'text-align': 'left'}),
                        html.Br(),
                        html.Li([' How have the keywords of the most viewed videos changed over the last 10 years? ',
                        html.A("Here", href="/keywordanalysis")],
                        style={'text-align': 'left'})
                    ])
                    ],
                        style={'padding': '8px', 'background-color': '#2e2d2d',
                        'border-radius': '10px', 'box-shadow': '0px 2px 5px #4d4c4c'},
                        width={'size':2,'offset':0},
                        className='text-center',
                    ),
        ],
        justify='center',
        style ={'text-align': 'center'}
    ),
    dbc.Row([
            dbc.Col(style={'height':'50px'})
        ]
    ),
])