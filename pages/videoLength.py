from datetime import datetime, timedelta

import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px

import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Register the page with the specified name
dash.register_page(__name__,  name='Video Length')

# Load original and filtered video length data
video_length_data = pd.read_csv('./data/videoLength/VideoLengthData.csv')
filtered_video_length_data = pd.read_csv('./data/videoLength/Filtered_VideoLengthData.csv')


# ///////////////Layout//////////////////

layout = html.Div([
    # Header
    dbc.Row(
        [
            dbc.Col(
                html.H2('Analysis of Video Duration by Category (2013-2023)', style={'color': '#dd2b2b'}),
                width={'size': 5, 'offset': 1},
            ),
        ]
    ),
    # Description
    dbc.Row([
        dbc.Col(
            html.H5('''
                    The following charts illustrate the average duration of videos across various categories over the period from 2013 to 2023 in the USA.
                    Each line or area represents a distinct category.
                    This analysis focuses on data from the United States, as it accounts for the highest traffic on the platform, providing a comprehensive overview.
                '''),
            width={'size': 4, 'offset': 1}
        ),
    ]),
    # Dropdown to select data type
    dbc.Row([
        dbc.Col(dcc.Dropdown(id='data-dropdown',
                             options=[
                                 {'label': 'Original Data', 'value': 'original_data'},
                                 {'label': 'Filtered Data', 'value': 'filtered_data'},
                             ],
                             value='original_data',
                             clearable=False,
                             searchable=False,
                             ),
                style={'color': '#262626'},
                width={'size': 2, 'offset': 5, 'order': 0}
                ),
        dbc.Col(),
    ]),
    # Empty row
    dbc.Row([dbc.Col(html.H1()), dbc.Col()]),
    # Graphs and text output
    dbc.Row([
        dbc.Col(dcc.Graph(id='video-length-lineplot'),
                width={'size': 6, 'offset': 1},
                style={'padding': '5px', 'background-color': '#d1d1d1', 'border-radius': '10px', 'box-shadow': '0px 2px 5px #949494'},
                ),
        dbc.Col(html.H5(id='text-output'),
                width=4
                ),
    ]),
    # Empty row
    dbc.Row([dbc.Col(html.H1()), dbc.Col()]),
    # Graphs and description
    dbc.Row([
        dbc.Col(dcc.Graph(id='video-length-bar'),
                width={'size': 6, 'offset': 1},
                style={'padding': '5px', 'background-color': '#d1d1d1', 'border-radius': '10px', 'box-shadow': '0px 2px 5px #949494'},
                ),
        dbc.Col(html.H5('''
                In the upper graph, it is evident how the average video duration significantly decreases in the 'Film & Animation' category,
                as a large number of short films are included in the most-viewed videos over time. In the lower diagram, this category has been filtered out,
                resulting in a much clearer trend. Up until the Short Release in 2021, the average video duration noticeably increases,
                attributed to improved internet connectivity and consequently faster upload times.
                '''),
                width=4
                ),
    ])
])


# ///////////////Callbacks//////////////////

# Callback to update graphs and text output based on dropdown selectio
@callback(
    [Output('video-length-bar', 'figure'),
     Output('video-length-lineplot', 'figure'),
     Output('text-output', 'children')],
    [Input('data-dropdown', 'value')]
)
def update_graphs(selected_data):
    if selected_data == 'original_data':
        data_to_use = video_length_data
        text_output = [html.B("The Original Data"),
                       " refers to the unfiltered dataset obtained from the YouTube API through our request."]
    elif selected_data == 'filtered_data':
        data_to_use = filtered_video_length_data
        text_output = [
            html.Div([
                html.B("The Filtered Data "),
                "has been processed using a function designed to exclude entries with non-Latin characters in their titles. ",
                "This was done due to instances where video durations were inaccurately recorded. ",
                "For instance, in 2016, within the 'People & Blogs' category, numerous Arabic-language series were present, which were unrelated to the category. ",
                "(On YouTube, video creators can select the category, leading to potential distortions.) ",
                "As a result of this filtering process, ",
                html.B("16.68%"),
                " of the entries were ",
                html.B("removed"),
                "."
            ])
        ]

    common_legend_title = 'Category'
    bar_data = data_to_use[data_to_use['Category Title'] != 'Film & Animation']
    bar_fig = px.area(
        bar_data,
        x='Year',
        y='Duration_minutes',
        color='Category Title',
        # barmode='group',
        labels={'Year': 'Year', 'Duration_minutes': 'Average Duration'},
        hover_data={'Category Title': False, 'Duration_minutes': ':.2f', 'Year': False},
        hover_name='Category Title',
    )
    bar_fig.update_traces(hovertemplate='Duration: %{y:.2f} min'),
    bar_fig.add_vline(x=2021, line_dash="dash", line_color="red", annotation_text="Shorts Release",
                      annotation_font=dict(color="red")),
    bar_fig.add_vline(x=2020, line_dash="dash", line_color="red", annotation_text="Corona Pandemic",
                      annotation_position="top left", annotation_font=dict(color="red"))

    bar_fig.update_layout(
        plot_bgcolor='#e7e7e7',
        paper_bgcolor='#d1d1d1',
        legend_title=common_legend_title,
        height=550,
    )
    bar_fig.update_yaxes(tickvals=[], ticktext=[])
    

    line_fig = px.line(
        data_to_use,
        x='Year',
        y='Duration_minutes',
        color='Category Title',
        labels={'Year': 'Year', 'Duration_minutes': 'Duration in Minutes'},
        hover_data={'Category Title': False, 'Duration_minutes': ':.2f', 'Year': False},
        hover_name='Category Title',
        title='Average Video Duration by Category',
        # markers=True,
    )
    line_fig.update_traces(hovertemplate='Duration: %{y:.2f} min'),
    line_fig.add_vline(x=2021, line_dash="dash", line_color="red", annotation_text="Shorts Release",
                       annotation_font=dict(color="red")),
    line_fig.add_vline(x=2020, line_dash="dash", line_color="red", annotation_text="Corona Pandemic",
                       annotation_position="top left", annotation_font=dict(color="red")),

    line_fig.update_layout(
        plot_bgcolor='#e7e7e7',
        paper_bgcolor='#d1d1d1',
        legend_title=common_legend_title,
        height=550,
    )

    return bar_fig, line_fig, text_output