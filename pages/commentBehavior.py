import os
from datetime import datetime, timedelta

import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px

import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

dash.register_page(__name__, name='Comment Behavior')

# Define the list of YouTube channels for data retrieval
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

# Define the directory path where the comment data is stored
directory_path = "data/comments/"

# List to hold DataFrames for each channel
dataframes = []

# Iterate through each channel to read and process its data
for channel in channels:
    filepath = os.path.join(directory_path, channel, "development.csv")
    
    # Check if the file exists
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        
        # Aggregate daily statistics
        daily_stats = df.groupby('Day').agg({
            'Average per Video': 'mean',
            'Relative Probability (%)': 'mean'
        })
        daily_stats = daily_stats.reset_index()
        daily_stats['Channel'] = channel
        
        # Append the DataFrame to the list
        dataframes.append(daily_stats)
    else:
        print(f"File 'development.csv' for channel '{channel}' not found.")

# Combine all DataFrames into one
combined_df = pd.concat(dataframes)

# Aggregate overall averages
average_overall = combined_df.groupby('Day').agg({
    'Average per Video': 'mean',
    'Relative Probability (%)': 'mean'
}).reset_index()
average_overall['Channel'] = 'Overall'
average_overall = average_overall[average_overall['Day'] <= 30]


#///////////////Layout//////////////////

layout = html.Div([
    # Header
    dbc.Row(
        [
            dbc.Col(
                html.H2('Youtube Comments', style={'color': '#dd2b2b'}),
                width={'size': 5, 'offset': 1},
            ),
        ]
    ),
    # Description
    dbc.Row(
        [
            dbc.Col(
                html.H5('''
                This section is about commenting behavior on YouTube videos.
                The data is from selected channels, from different categories,
                in order to create the most accurate image possible.
                '''),
                width={'size': 5, 'offset': 1},
            ),
        ],
        style={'height':'100px'}
    ),
    # Dropdown for selecting value type
    dbc.Row([
        dbc.Col(dcc.Dropdown(
            id='value-dropdown',
            options=[
                {'label': 'Relative Probability', 'value': 'Relative Probability (%)'},
                {'label': 'Average per Video', 'value': 'Average per Video'}
            ],
            value='Relative Probability (%)',
            clearable=False,
            searchable=False,
        ),
            style={'color': '#262626'},
            width={'size': 2, 'offset': 1})
    ],
    style={'height':'50px'}
    ),
    # Overall Line Chart
    dbc.Row([
        dbc.Col(dcc.Graph(id='overall-line-chart'), width={'size': 8, 'offset': 1},
        style={'padding': '5px', 'background-color': '#d1d1d1', 'border-radius': '10px', 'box-shadow': '0px 2px 5px #949494'},
        ),
        dbc.Col(html.H5('''
            In this graph, you can clearly see that a very large proportion of comments are written on the first day, and only 1/5 are written on the second day.
            After 10 days, less than 1% of comments are written. This shows how fast-moving videos on YouTube are.
            '''),
            width=2
        )
    ]),
    # Separator
    dbc.Row([
        dbc.Col(html.Hr(style={'margin': '20px 0', 'border': 'none', 'border-top': '1px solid #ccc'}),
        width={'size':10, 'offset':1}
                )
    ],
    style={'height':'50px'},
    ),
    # Channel Selection Description
    dbc.Row([
        dbc.Col(html.H5('''
                In this section, you can take a closer look at what the comment behavior is like on the selected channels.
                To do this, simply select the channel in the drop-down menu. You can then click on the individual days to get a more detailed overview.
                You also have the option to move “Days After Release” to get further away from the release date.
                '''),
            width={'size': 5, 'offset': 1},)
    ],
    style={'height':'120px'}
    ),
    # Channel Dropdown
    dbc.Row([
        dbc.Col(dcc.Dropdown(
            id='channel-dropdown',
            options=[{'label': channel, 'value': channel} for channel in channels],
            value=channels[0],
            clearable=False,
            searchable=False,
        ),
            style={'color': '#262626'},
            width={'size': 2, 'offset': 1}
        ),
        dbc.Col(
        )
    ],
    style={'height':'50px'}
    ),
    # Bar Chart for Channel Comments
    dbc.Row([
        dbc.Col(dcc.Graph(id='comment-bar-chart'), width={'size': 5, 'offset': 1},
        style={'padding': '5px', 'background-color': '#d1d1d1', 'border-radius': '10px', 'box-shadow': '0px 2px 5px #949494'},),
        dbc.Col(dcc.Graph(id='selected-comment-bar-chart'), width={'size': 5, 'offset': 0},
        style={'padding': '5px', 'background-color': '#d1d1d1', 'border-radius': '10px', 'box-shadow': '0px 2px 5px #949494'},)
    ]),
    dbc.Row([
        dbc.Col(html.H5())
    ]),
])


# ///////////////Callbacks//////////////////

# Callback to update overall line chart
@callback(
    Output('overall-line-chart', 'figure'),
    [Input('value-dropdown', 'value')]
)
def update_overall_line_chart(selected_value):
    if selected_value == 'Relative Probability (%)':
        value_title = 'Relative Probability (%)'
    elif selected_value == 'Average per Video':
        value_title = 'Average per Video'
    else:
        value_title = 'Value'

    overall_line_chart = px.bar(
        average_overall,
        x='Day',
        y=average_overall[selected_value],
        labels={'Day': 'Days After Video Release', selected_value: value_title},
        color_discrete_sequence=['#dd2b2b'],
        title='Average Comments on YouTube Videos'
    )
    overall_line_chart.update_layout(
        plot_bgcolor='#e7e7e7',
        paper_bgcolor='#d1d1d1',
    )
    return overall_line_chart

# Callback to update the bar chart for a selected channel and value type
@callback(
    Output('comment-bar-chart', 'figure'),
    [Input('channel-dropdown', 'value'),
     Input('value-dropdown', 'value')]
)
def update_bar_chart(selected_channel, selected_value):
    data_path = f'data/comments/{selected_channel}/'
    channel_data = pd.read_csv(f'{data_path}development.csv')
    # channel_data = channel_data[channel_data['Day'] <= 100]

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
        labels={'Day': 'Days After Video Release', selected_value: value_title},
        color_discrete_sequence=['#dd2b2b'],
        title=f'Average Comments under Videos from {selected_channel}'
        
    )
    comment_fig.update_layout(
        xaxis=dict(range=[0.5, 50]),
        plot_bgcolor='#e7e7e7',
        paper_bgcolor='#d1d1d1',
    )

    return comment_fig

# Callback to update the selected comment bar chart based on user clicks
@callback(
    Output('selected-comment-bar-chart', 'figure'),
    [Input('comment-bar-chart', 'clickData'),
    Input('channel-dropdown', 'value'),
    Input('value-dropdown', 'value')]
)
def update_selected_bar_chart(clickData, selected_channel, selected_value):
    data_path = f'data/comments/{selected_channel}/'
    filepath = os.path.join(data_path,"development_daily.csv")
    df = pd.read_csv(filepath)
    df['Relative Probability (%)'] = df['Relative Probability']

    if clickData:
        selected_day = clickData['points'][0]['x']
        selected_day = selected_day - 1
    else:
        selected_day = df['Day'].iloc[0]
    
    selected_day_data = df[df['Day'] == selected_day]

    selected_figure = px.bar(
        selected_day_data, 
        x='Hour', 
        y=selected_day_data[selected_value], 
        title=f'Comments for day {selected_day + 1}',
        color_discrete_sequence=['#dd2b2b']
    )

    selected_figure.update_layout(
        plot_bgcolor='#e7e7e7',
        paper_bgcolor='#d1d1d1',
    )

    return selected_figure


