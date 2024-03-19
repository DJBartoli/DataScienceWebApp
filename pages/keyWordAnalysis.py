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

dash.register_page(__name__, name='Keyword Analysis')
TOPICS = ['sports', 'gaming', 'lifestyle', 'politics', 'society', 'knowledge']
step_size = 1


def create_image_dataframe():
    """
    this method creates a dataframe storing all the paths for the topic separated wordclouds
    :return: A Dataframe, with columns : topic, year, path
    """
    image_df = pd.DataFrame()
    i = 0
    for topic in TOPICS:
        for year in range(2013, 2024):
            path = f'data/keyWordClouds/topicKeyWords/youtube_keywords_{topic}_{year}.png'
            new_row = pd.DataFrame({'topic': topic, 'year': str(year), 'path': path}, index=[i])
            image_df = pd.concat([image_df, new_row])
            i += 1

    for year in range(2013, 2024):
        path = f'data/keyWordClouds/yearlyKeyWords/youtube_keywords_{year}.png'
        new_row = pd.DataFrame({'topic': 'all categories', 'year': str(year), 'path': path}, index=[i])

        image_df = pd.concat([image_df, new_row], )
        i += 1

    return image_df

topic_images = create_image_dataframe()

marks = {str(year): str(year) for year in topic_images['year'].unique()}
layout = html.Div([
    dbc.Row(
        [
            dbc.Col(
                children=[html.H2('YouTube through the years', style={'color': '#dd2b2b'}),
                          html.H3(
                              'Discover the most watched videos according to the keywords. Choose the year an category of interest'),
                          ],
                width={'size': 6, 'offset': 3},

            ),
        ]
    ),
    dbc.Row([
        dbc.Col(
            children=[

                dcc.Dropdown(
                    id='category-dropdown',
                    options=[{'label': topic, 'value': topic} for topic in topic_images['topic'].unique()],
                    value=topic_images['topic'].unique()[0],
                    clearable=False,
                    searchable=False,
                ),
            ],
            width={'size': 6, 'offset': 3},
            style={'color': '#121212'}
        ),
    ]),
    dbc.Row([
        dbc.Col(
            children=[
                dcc.Slider(
                    id='year-slider',
                    min=2013,
                    max=2023,
                    value=2013,
                    marks=marks,
                    step=step_size,
                    included=True,  # Alle Markierungen werden immer angezeigt
                    tooltip={
                        "always_visible": False,
                        "style": {"color": "#dd2b2b", "fontSize": "20px"},
                    },

                ),
            ],
            width={'size': 5, 'offset': 3},
            style={'margin-top': '5px'},
        ),
        dbc.Col(
            children=[
                html.Button('◄', id='slider-left', n_clicks=0,
                            style={'font-size': '20px', 'background-color': '#dd2b2b', 'color': '#ffffff',
                                   'border-color': '#ffffff', 'margin-right': '5px',
                                   'border-radius': '10px'}),
                html.Button('►', id='slider-right', n_clicks=0,
                            style={'font-size': '20px', 'background-color': '#dd2b2b', 'color': '#ffffff',
                                   'margin-left': '5px',
                                   'border-radius': '10px', 'border-color': '#ffffff'}),
            ],
            width={'size': 1, 'offset': 0},
            style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}
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


@callback(
    Output('graph', 'figure'),
    [Input('category-dropdown', 'value'),
     Input('year-slider', 'value')]
)
def update_wordcloud(topic, year):

    if topic == 'all categories':
        path = f'data/keyWordClouds/yearlyKeyWords/youtube_keywords_{year}.png'
    else:
        path = f'data/keyWordClouds/topicKeyWords/youtube_keywords_{topic}_{year}.png'

    img = plt.imread(path)

    fig = px.imshow(img)

    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)

    return fig


@callback(
    Output('year-slider', 'value'),
    [Input('slider-left', 'n_clicks'),
     Input('slider-right', 'n_clicks')],
    [State('year-slider', 'value')]
)
def update_slider_value(left_clicks, right_clicks, current_value):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'slider-left' in changed_id:
        return max(current_value - step_size, 2013)
    elif 'slider-right' in changed_id:
        return min(current_value + step_size, 2023)
    return current_value
