import os
from datetime import datetime, timedelta
import json

import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px

from geopy.geocoders import Nominatim
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import json
import dash_bootstrap_components as dbc
dash.register_page(__name__, name='Comment Behavior')

channels = [
    'baldandbankrupt',
    'BestEverFoodReviewShow',
    'ColdFusion',
    'HaraldBaldr',
    'PracticalEngineeringChannel',
    'RoCarsTV',
    'strictlydumpling',
    'tavarish',
    'theonlyzanny',
    'thespiffingbrit',
    'TravelThirstyBlog',
    'YesTheory'
]



layout = html.Div([
    dbc.Row(
        [
            dbc.Col(
                html.H2('Youtube Comment behavior', style={'color': '#dd2b2b'}),
                width={'size': 5, 'offset': 1},
            ),
        ]
    ),
    dbc.Row([
        dbc.Col(dcc.Dropdown(
            id='channel-dropdown',
            options=[{'label': channel, 'value': channel} for channel in channels],
            value=channels[0]
        ),
            style={'color': '#262626'},
            width={'size': 2, 'offset': 1}
        ),
        dbc.Col(dcc.Dropdown(
            id='value-dropdown',
            options=[
                {'label': 'Relative Probability', 'value': 'Relative Probability (%)'},
                {'label': 'Average per Video', 'value': 'Average per Video'}
            ],
            value='Relative Probability (%)'
        ),
            style={'color': '#262626'},
            width={'size': 2, 'offset': 0}
        )
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='comment-bar-chart'), width={'size': 10, 'offset': 1})
    ])
])


@callback(
    Output('comment-bar-chart', 'figure'),
    [Input('channel-dropdown', 'value'),
     Input('value-dropdown', 'value')]
)
def update_bar_chart(selected_channel, selected_value):
    data_path = f'data\\comments\\{selected_channel}/'
    channel_data = pd.read_csv(f'{data_path}development.csv')
    channel_data = channel_data[channel_data['Day'] <= 100]

    if selected_value == 'Relative Probability (%)':
        value_title = 'Relative Probability (%)'
    elif selected_value == 'Average per Video':
        value_title = 'Average per Video'
    else:
        value_title = 'Value'

    comment_fig = px.bar(
        channel_data,
        x='Day',
        y=channel_data[selected_value],
        labels={'Day': 'Days After Video Release', selected_value: value_title}
    )
    comment_fig.update_layout(
        plot_bgcolor='#e7e7e7',
        paper_bgcolor='#d1d1d1',
    )

    return comment_fig

