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

dash.register_page(__name__,  name='Categories Interactions')

catdf = pd.read_csv('data/duration/categoryInteractions.csv')

# Barchart

fig = go.Figure(data=[
    go.Bar( name='Average Likes', x=catdf['Category'], y=catdf['Average Likes']),
    go.Bar( name='Avegare Comments', x=catdf['Category'], y=catdf['Average Comments'], marker_color='#dd2b2b')
])

fig.update_layout(title_text='Average viewer interactions in different categories', barmode='stack',
            plot_bgcolor='#e7e7e7',
            paper_bgcolor='#d1d1d1')
fig.update_xaxes(title='Category')
fig.update_yaxes(title='Interactions per 1000 views')


# Layout

layout = html.Div(

    dbc.Row([
        dbc.Col(
            html.H2('Viewer interaction in different categories', style={'color': '#dd2b2b'}),
                width={'size': 5, 'offset': 1},
                style={'height':'80px'},
        ),

        dbc.Row(dbc.Col(
                html.H5('The charts on this page show the differences in viewer engagement across different categories.', ),
                width={'size': 7, 'offset': 1},
                style={'height':'80px'},
            )),

            dbc.Row([
                dbc.Col(dcc.Graph(
                id='category-bar', figure=fig),
                width={'size': 7, 'offset': 1},
                style={'padding': '5px', 'background-color': '#d1d1d1', 'border-radius': '10px', 'box-shadow': '0px 2px 5px #949494'},
                ),
            dbc.Col(html.H5('''
                        This barchart shows the average likes and comments in selected categories.
                        To obtain this data, we selected a few channels per category and analyzed the video informtion for 1000 videos per category. 
                        For better comparison, we selected channels that have similar characteristics for each category. All videos used for this chart are from english speaking channels that have  
                        more than one million subsribers. Additionally, we excluded YouTube Shorts from this statistic. Adding to that, we made sure that the length and views of the selected channels' videos
                        is comparible. Of course it is not possible to find 5000 videos that have the same ammount of views and playtime, but most videos used for this chart are in the same range of views 
                        and have a simillar length.
                        
                    '''))
            ]),
    ]),
    
)