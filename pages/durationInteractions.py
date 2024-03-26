import pandas as pd

import dash
import dash_bootstrap_components as dbc
import plotly.graph_objects as go

from dash import dcc, html, callback
from dash.dependencies import Input, Output

dash.register_page(__name__, name='Duration Interactions')

# Loading and formatting CSVs needed for this page.

df = pd.read_csv('data/duration/Markiplier_Formatted.csv')

boxdf = pd.read_csv('data/duration/Boxplot_Data.csv')

avg_like = df.groupby('Category')['Like/View'].mean().reset_index()

avg_comment = df.groupby('Category')['Comment/View'].mean().reset_index()

# Creating the first Barchart.

# Manually changing titles for the bars.

bar_titles = ['0-5', '5-10', '10-20', '20-30', '30-60', '60+']

fig = go.Figure(data=[
    go.Bar(name='Average Likes', x=avg_like['Category'], y=avg_like['Like/View']),
    go.Bar(name='Avegare Comments', x=avg_comment['Category'], y=avg_comment['Comment/View'], marker_color='#dd2b2b', )
])

bar_titles = ['0-5', '5-10', '10-20', '20-30', '30-60', '60+']
fig.update_layout(title_text='Average Viewer Interactions measured by Comments and Likes', barmode='stack',
                  plot_bgcolor='#e7e7e7',
                  paper_bgcolor='#d1d1d1')
fig.update_xaxes(title='Video Length in Minutes', tickvals=avg_like['Category'], ticktext=bar_titles)
fig.update_yaxes(title='Interactions per 1000 Views')

# Layout

layout = html.Div(

    dbc.Row(

        [
            # Title for this page.

            dbc.Col(
                html.H2('Viewer Interaction based on Video Length', style={'color': '#dd2b2b'}),
                width={'size': 5, 'offset': 1},
                style={'height': '80px'},
            ),

            # Short site description.

            dbc.Row(dbc.Col(
                html.H5(
                    'The charts on this page show the correlation between video length and viewer engagement for the channel "Markiplier".', ),
                width={'size': 7, 'offset': 1},
                style={'height': '80px'},
            )),

            # Displaying the first barchart.

            dbc.Row([
                dbc.Col(dcc.Graph(
                    id='duration-bar', figure=fig),
                    width={'size': 7, 'offset': 1},
                    style={'padding': '5px', 'background-color': '#d1d1d1', 'border-radius': '10px',
                           'box-shadow': '0px 2px 5px #949494'},
                ),

                # Text next to the figure.

                dbc.Col(html.H5('''
                    Since viewer engagement can vary a lot between different channels, this graph focuses on a single YouTube channel. We are using the channel "Markiplier" because there
                    are lots of videos with a great variety in length uploaded to the channel. Another factor that influenced our choice is the amount of YouTube Shorts uploaded to the channel, 
                    since in terms of length and interaction ratio, they are not comparable to regular videos on the platform. On Markiplier's channel, there are only 4 Shorts uploaded, so they don't have a noticeable 
                    influence on our data because the data used on this page contains a total of 5000 Videos. The Barchart shows a clear trend, especially for the average comment values. The shortest videos have 
                    the highest amount of comments, and the longer the video gets, the lower amount of comments per view. For the average like count, it can also be said that it is the highest for the 
                    shortest video and the lowest for the longest video, but there is no clear trend for the categories in between.
                    '''

                                ))
            ]),

            # Seperation line between visualizations.

            dbc.Row([
                dbc.Col(html.Hr(style={'margin': '20px 0', 'border': 'none', 'border-top': '1px solid #ccc'}),
                        width={'size': 10, 'offset': 1}
                        )
            ],

                style={'height': '50px'},

            ),

            # Title for the second figure.

            dbc.Col(
                html.H2('Data displayed as a Boxplot', style={'color': '#dd2b2b'}),
                width={'size': 5, 'offset': 1},
                style={'height': '70px'}
            ),

            # Inserting the dropdown menu to change between boxplots.

            dbc.Row(
                dbc.Col(dcc.Dropdown(
                    id='duration-drop',
                    options=[{'label': 'Comments', 'value': 'Comments'},
                             {'label': 'Likes', 'value': 'Likes'},
                             ],
                    value='Comments',
                    clearable=False
                ),

                    style={'color': '#262626'},
                    width={'size': 2, 'offset': 1}),

            ),

            # Inserting an empty row to create a gap between dropdown menu and boxplots.

            dbc.Row(dbc.Row(html.H5(), style={'height': '20px'})),

            # Inserting the boxplots.

            dbc.Row([
                dbc.Col(dcc.Graph(
                    id='duration-boxplot', ),
                    width={'size': 7, 'offset': 1},
                    style={'padding': '5px', 'background-color': '#d1d1d1', 'border-radius': '10px',
                           'box-shadow': '0px 2px 5px #949494'},

                ),

                # Text next to the boxplots.

                dbc.Col(html.H5('''
                        These boxplots show how the interaction values are distributed in each video length category. In the drop-down menu, you can choose between the comment and the like plots.
                        In these boxplots, you can see that there are many outliers, especially for shorter videos. To filter out extreme points, we removed all entries 
                        in the dataset that were more than 3 times the standard deviation away from the mean. In total, 190 entries were filtered out. Since we already filtered out the outliers that we do not 
                        want to have in our visualization, we are using the linear algorithm for the computation of the boxplots. These boxplots show similar trends to the barchart above. You can see that the 
                        amount of comments consistently gets lower the longer the videos get, while there is also no clear trend for the likes.
                        '''))
            ]),

        ])

),


# Callback to receive input from dropdown menu and change plots.

@callback(
    Output('duration-boxplot', 'figure'),
    [Input('duration-drop', 'value')]
)
# Callback Function.

# Function returns different boxplots for 'Comments' or 'Likes'.

def update_duration_box(selected_value):
    if selected_value == 'Comments':

        trace = go.Box(x=boxdf['Length'], y=boxdf['Comment/View'], marker_color='#dd2b2b', name='Boxplot')

        layout = go.Layout(title=f'Boxplot for {selected_value}', xaxis_title='Video Duration in Minutes',
                           yaxis_title='Comments per 1000 Views', plot_bgcolor='#e7e7e7', paper_bgcolor='#d1d1d1')

        return {'data': [trace], 'layout': layout}

    elif selected_value == 'Likes':

        trace2 = go.Box(x=boxdf['Length'], y=boxdf['Like/View'], name='Boxplot2')

        layout = go.Layout(title=f'Boxplot for {selected_value}', xaxis_title='Video Duration in Minutes',
                           yaxis_title='Likes per 1000 Views', plot_bgcolor='#e7e7e7', paper_bgcolor='#d1d1d1')

        return {'data': [trace2], 'layout': layout}
