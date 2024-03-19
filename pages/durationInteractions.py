import os
from datetime import datetime, timedelta
import json

import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
import plotly.graph_objects as go

from geopy.geocoders import Nominatim
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import json
import dash_bootstrap_components as dbc

dash.register_page(__name__,  name='Duration Interactions')

df = pd.read_csv('data\duration\Markiplier_Formatted.csv')

avg_like = df.groupby('Category')['Like/View'].mean().reset_index()

avg_comment = df.groupby('Category')['Comment/View'].mean().reset_index()

# Barchart

fig = go.Figure(data=[
    go.Bar( name='Average Likes', x=avg_like['Category'], y=avg_like['Like/View']),
    go.Bar( name='Avegare Comments', x=avg_comment['Category'],
            y=avg_comment['Comment/View'])
])

fig.update_layout(title_text='Average Viewer Interaction per 1000 views', barmode='stack',
            plot_bgcolor='#e7e7e7',
            paper_bgcolor='#d1d1d1')
fig.update_xaxes(title='Category')
fig.update_yaxes(title='Interactions')

# Boxplot

fig2 = go.Figure(data=[
    go.Box( name='Average Likes', x=df['Category'], y=df['Like/View']),
    go.Box( name='Avegare Comments', x=df['Category'], y=df['Comment/View'])
])

fig2.update_layout(
    title_text='Average Viewer Interaction per 1000 views', 
    boxmode='group',
    plot_bgcolor='#e7e7e7',
    paper_bgcolor='#d1d1d1',
)
fig2.update_xaxes(title='Category')
fig2.update_yaxes(title='Interactions')

layout = html.Div(
    dbc.Row(
        [
            dbc.Col(
                html.H2('Viewer interaction based on video length', style={'color': '#dd2b2b'}),
                width={'size': 5, 'offset': 1},
                style={'height':'80px'},
            ),

            dbc.Row([
                dbc.Col(dcc.Graph(
                id='duration-bar', figure=fig),
                width={'size': 8, 'offset': 1},
                style={'padding': '5px', 'background-color': '#d1d1d1', 'border-radius': '10px', 'box-shadow': '0px 2px 5px #949494'},
                ),
            dbc.Col(html.H5('''
                    Text
                    '''))
            ]),
            dbc.Row([
                dbc.Col(html.Hr(style={'margin': '20px 0', 'border': 'none', 'border-top': '1px solid #ccc'}),
                width={'size':10, 'offset':1}
                        )
            ],
            style={'height':'50px'},
            ),
            dbc.Col(
                html.H3('Enter Text for Figure 1 here', style={'color': '#dd2b2b'}),
                width={'size': 5, 'offset': 1},
                style={'height':'70px'}
            ),

            dbc.Row(
                dbc.Col(dcc.Dropdown(
                id='duration-drop',
                options=[{'label': '0-5 minutes', 'value': 1},
                        {'label': '5-10 minutes', 'value': 2},
                        {'label': '10-20 minutes', 'value': 3},
                        {'label': '20-30 minutes', 'value': 4},
                        {'label': '30-60 minutes', 'value': 5},
                        {'label': '60+ minutes', 'value': 6}],
                        value=1 
                        ),

                        style={'color': '#262626'},
                        width={'size': 2, 'offset': 1} ),

            ),
            dbc.Row(dbc.Row(html.H5(),style={'height':'20px'})),

            dbc.Row([
                dbc.Col(dcc.Graph(
                id='duration-boxplot',),
                width={'size': 5, 'offset': 1},
                style={'padding': '5px', 'background-color': '#d1d1d1', 'border-radius': '10px', 'box-shadow': '0px 2px 5px #949494'},
                
                ),
                dbc.Col(html.H5('''
                        Text
                        '''))
            ]),

            

            
    ])
            

    ),

    

@callback(
    Output('duration-boxplot', 'figure'),
    [Input('duration-drop', 'value')]
)

def update_duration_box(selected_value):

    y_data = df[df['Category']== selected_value]

    trace = go.Box(y=y_data['Like/View'], name='Boxplot')
    trace2 = go.Box(y=y_data['Comment/View'], name='Boxplot2')

    layout = go.Layout(title=f'Boxplot for {selected_value}', plot_bgcolor='#e7e7e7', paper_bgcolor='#d1d1d1')

    return{'data': [trace, trace2], 'layout': layout}


