import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import dash
from dash import dcc, html, callback
import plotly.express as px

from geopy.geocoders import Nominatim
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import json
import dash_bootstrap_components as dbc

dash.register_page(__name__, name='Keyword Analysis')
TOPICS = ['sports', 'gaming', 'lifestyle', 'politics', 'society', 'knowledge']


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
                width={'size': 5, 'offset': 1},

            ),
        ]
    ),
    dbc.Row([
        dbc.Col(
            [
                dcc.Dropdown(
                    id='category-dropdown',
                    options=[{'label': topic, 'value': topic} for topic in topic_images['topic'].unique()],
                    value=topic_images['topic'].unique()[0]
                ),
                dcc.Slider(
                    id='year-slider',
                    min=2013,
                    max=2023,
                    value=2013,
                    marks=marks
                ),
                dcc.Graph(id='graph')
            ]
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
    path = f'data/keyWordClouds/topicKeyWords/youtube_keywords_{topic}_{year}.png'
    img = plt.imread(path)

    fig = px.imshow(img)

    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=False)

    return fig

@callback(
    Output('year-slider', 'value'),
    [Input('year-slider', 'value')]
)
def update_slider_value(value):
    # Suchen Sie den nächstgelegenen Wert in den markierten Werten und setzen Sie ihn zurück
    nearest_value = min(marks.keys(), key=lambda x: abs(int(x) - value))
    return int(nearest_value)

# Rufen Sie die aktualisierte Dropdown-Optionen basierend auf dem aktuellen Jahr ab
@callback(
    Output('year-slider', 'marks'),
    [Input('year-slider', 'value')]
)
def update_slider_marks(value):
    # Verwenden Sie das aktuelle Jahr, um die Optionen für die Dropdown-Liste zu aktualisieren
    current_year = value
    new_marks = {str(year): str(year) for year in range(2013, current_year + 1)}
    return new_marks