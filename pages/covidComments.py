import os

import pandas as pd

import dash
import dash_bootstrap_components as dbc

import plotly.express as px
from _plotly_utils.png import Image
from dash import dcc, html, callback
from dash.dependencies import Input, Output


dash.register_page(__name__, name='Covid Comments')

COVID_COMMENTS = pd.read_csv(r'data/covidComments/comments_with_emotions.csv')
YEARS = COVID_COMMENTS['year'].unique().tolist()
YEARS.append('All Years')

QUERIES = COVID_COMMENTS['query'].unique().tolist()
QUERIES.append('All Queries')

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
        dbc.Col([

            dbc.Label("Select Year"),
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': str(year), 'value': year} for year in YEARS],
                value='All Years',
                multi=False,
                style={'color': '#121212'}
            ),
        ], width={'size': 3, 'offset': 3},
            style={'color': '#dd2b2b'}
        ),
        dbc.Col([

            dbc.Label("Select Query"),
            dcc.Dropdown(
                id='query-dropdown',
                options=[{'label': query, 'value': query} for query in QUERIES],
                value='All Queries',
                multi=False,
                style={'color': '#121212'}
            ),
        ], width={'size': 3},
            style={'color': '#dd2b2b'}
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

                dcc.Graph(id='comment-histogram'),

            ],
            width={'size': 6, 'offset': 3},
            style={'padding': '5px', 'background-color': 'white', 'border-radius': '10px',
                   'box-shadow': '0px 2px 5px #949494'},
        )
    ]),
    dbc.Row([
        dbc.Col(
            children=[

                dbc.Col(dcc.Graph(id='comment-pie'))

            ],
            width={'size': 6, 'offset': 3},
            style={'padding': '5px', 'margin-top': '20px', 'background-color': 'white', 'border-radius': '10px',
                   'box-shadow': '0px 2px 5px #949494'},
        )
    ]),
    dbc.Row([
        dbc.Col(
            children=[
                dbc.Col(dcc.Graph(id='emotion-over-time')),
            ],

            width={'size': 6, 'offset': 3},
            style={'padding': '5px', 'margin-top': '20px', 'background-color': 'white', 'border-radius': '10px',
                   'box-shadow': '0px 2px 5px #949494'},
        ),

    ])

])


@callback(
    Output('comment-histogram', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('query-dropdown', 'value')]
)
def update_graph(selected_year, selected_query):
    filtered_df = COVID_COMMENTS.copy()
    if selected_year != 'All Years':
        filtered_df = filtered_df[filtered_df['year'] == selected_year]
    if selected_query != 'All Queries':
        filtered_df = filtered_df[filtered_df['query'] == selected_query]

    emotion_order = ['joy', 'sadness', 'fear', 'anger', 'disgust', 'ambiguous']

    # Generate visualization using Plotly Express
    fig = px.histogram(filtered_df, x='emotion', color='emotion', title='Emotion Distribution',
                       category_orders={'emotion': emotion_order},
                       color_discrete_map={'joy': '#7EBB22', 'sadness': '#AC44CC', 'fear': '#7D3C98',
                                           'anger': '#E63946', 'disgust': '#F1C40F'})

    img_bytes = fig.to_image(format="png", scale=4)
    img = Image(img_bytes)
    if not os.path.exists("images"):
        os.mkdir("images")
        
    fig.write_image("images/fig1.png")

    return fig


@callback(
    Output('comment-pie', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('query-dropdown', 'value')]
)
def update_pie(selected_year, selected_query):
    filtered_df = COVID_COMMENTS.copy()
    if selected_year != 'All Years':
        filtered_df = filtered_df[filtered_df['year'] == selected_year]
    if selected_query != 'All Queries':
        filtered_df = filtered_df[filtered_df['query'] == selected_query]

    emotion_order = ['joy', 'sadness', 'fear', 'anger', 'disgust', 'ambiguous']
    # Calculate relative distribution of emotions
    emotion_counts = filtered_df['emotion'].value_counts(normalize=True)

    # Generate visualization using Plotly Express
    fig = px.pie(names=emotion_counts.index, values=emotion_counts.values, title='Relative Emotion Distribution',
                 color=emotion_counts.index,
                 category_orders={'emotion': emotion_order},
                 color_discrete_map={'joy': '#7EBB22', 'sadness': '#AC44CC', 'fear': '#7D3C98',
                                      'anger': '#E63946', 'disgust': '#F1C40F'})

    return fig


@callback(
    Output('emotion-over-time', 'figure'),
    [Input('year-dropdown', 'value'),
     Input('query-dropdown', 'value')]
)
def update_line_plot(selected_year, selected_query):
    if selected_year != 'All Years':
        return px.line()  # Return empty plot if a specific year is selected

    filtered_df = COVID_COMMENTS.copy()
    if selected_query != 'All Queries':
        filtered_df = filtered_df[filtered_df['query'] == selected_query]

    emotion_order = ['joy', 'sadness', 'fear', 'anger', 'disgust', 'ambiguous']
    # Calculate relative distribution of emotions over time
    emotion_counts_over_time = filtered_df.groupby(['year', 'emotion']).size().unstack(fill_value=0)
    emotion_counts_over_time = emotion_counts_over_time.apply(lambda x: x / x.sum(), axis=1)  # Normalize by row

    # Generate visualization using Plotly Express
    fig = px.line(emotion_counts_over_time, x=emotion_counts_over_time.index, y=emotion_counts_over_time.columns,
                  title='Relative Emotion Distribution Over Time',
                  labels={'year': 'Year', 'value': 'Relative Frequency', 'emotion': 'Emotion'},
                  category_orders={'emotion': emotion_order},
                  color_discrete_map={'joy': '#7EBB22', 'sadness': '#AC44CC', 'fear': '#7D3C98',
                                      'anger': '#E63946', 'disgust': '#F1C40F'})

    return fig
