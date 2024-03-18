import os
from datetime import datetime, timedelta
import json

import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import json
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)
server = app.server

dark_colors = {
 'text': '#eae9fc',
 'background': '#292929',
 'primary': '#67a2d2',
 'secondary': '#121212',
 'accent': '#ff0000'
}
light_colors = {
 'text': '#040316',
 'background': '#d6d6d6',
 'primary': '#2e6999',
 'secondary': '#ededed',
 'accent': '#dd2b2b'
},

with open('custom.geo_small.json', encoding='utf-8') as f:
    geojson_data = json.load(f)

video_length_data = pd.read_csv('VideoLengthData.csv')
filtered_video_length_data = pd.read_csv('Filtered_VideoLengthData.csv')

# video_length_bar = px.bar(
#     video_length_data,
#     x='Year',
#     y='Duration_minutes',
#     color='Category Title',
#     barmode='group',
#     labels={'Year': 'Year', 'Duration_minutes': 'Duration in Minutes'}
# )

# video_length_lineplot = px.line(
#     video_length_data,
#     x='Year',
#     y='Duration_minutes',
#     color='Category Title',
#     markers=True,
#     labels={'Year': 'Year', 'Duration_minutes': 'Duration in Minutes'},
#     hover_data={'Category Title': True, 'Duration_minutes': ':.2f'}
# )

world_map = px.choropleth_mapbox(
    geojson=geojson_data,
    # locations=df['location'],  # Add the appropriate location data from the DataFrame
    featureidkey="properties.id",  # Adjust this according to your GeoJSON structure
    # color=df['property_to_color'],  # Add the appropriate column from the DataFrame for color representation
    mapbox_style="carto-positron",
    zoom=3,  # Adjust the zoom level
    center={"lat": 51, "lon": 9},  # Adjust the center accordingly
    opacity=0.5
)

# ------------------------------------------------------------------------------
# App layout
# Layout of the home page
home_layout = html.Div(
    children=[
        dbc.Row([
            dbc.Col(
              html.Img(src='assets/logo.png'),
                width={'size': 1, 'offset': 4}

            ),
            dbc.Col(
                html.H1("Visualizing YouTube", style={'margin-top': '1vh', }),

                width={'size': 3, 'offset': 1},
            ),
        ]),
        html.Div("Select a project to visualize:"),
        dcc.Link("Project 1", href="/project-1"),
        html.Br(),
        dcc.Link("Project 1.2", href="/project-1.2"),
        html.Br(),
        dcc.Link("Project 2", href="/project-2"),
        html.Br(),
        dcc.Link("Project 3", href="/project-3"),
    ]
)

# Layout for Project 1
project_1_layout = html.Div(
    className='container-fluid',
    children=[
        html.H1(children="Youtube Trends Analytics"),
        html.Div(children='''
            A interactive Worldmap.
        '''),
        html.Div(
            className='row',
            children=[
                html.Div(
                    className='ten.columns',  # Verwenden Sie 'col-md-6', um die Hälfte der Seite einzunehmen
                    children=[
                        html.Div(
                            style={'width': '50%', 'height': '100vh'},  
                            children=[
                                dcc.Graph(id='map-graph', figure=world_map)
                            ]
                        )
                    ]
                ),
<<<<<<< HEAD
                html.Div(
                    className='col-md-6',  
                    children=[
                        html.Div(
                            style={'width': '50%', 'height': '100vh'},
                            children=[
                                html.Div(children=[
                                    'new stuff'
                                ])
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)
project_1_2_layout = html.Div([
    dbc.Row(dbc.Col(html.H2('Youtube Video Length Development'),
                width={'size':5, 'offset': 1},
                ),
        ),
    dbc.Row(dbc.Col(html.Div('''
                        The development of the video duration over the past 10 years.
=======
                width={'size':1, 'offset':5},
                className="bg-dark border",
                style={'color': '#2e6999'}
            ),
        ]
    ),
    dbc.Row(dbc.Col(html.H5('''
                    Here, you can observe the distribution of categories in the top 100 videos per day and country.
                    The countries available for selection include all EU member states and a selection of interesting countries from each additional continent.
                    The date selection is available within the range where data is present.
                    '''),
            width={'size': 4, 'offset': 1}
            ),
    ),
    dbc.Row(dbc.Col(html.H1('''
                    '''),
            ),
    ),
    dbc.Row([
        dbc.Col(
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': iso2} for country, iso2 in eu_countries_iso2.items()],
                value='DE'
            ),
            style={'color':'#262626'},
            width={'size': 2, 'offset': 1, 'order': 1}
        ),
        dbc.Col(
            dcc.DatePickerSingle(
                id='date-picker',
                min_date_allowed=datetime(2024, 3, 6),
                max_date_allowed=(datetime.today() - timedelta(days=1)),
                initial_visible_month=datetime.today(),
                date=(datetime(2024, 3, 15))
            ),
            width={'size': 1, 'offset': 1, 'order': 0}
        ),
    ]),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='pie-chart', figure=pie_first_data),
            width={'size':4, 'offset':1}
        ),
        dbc.Col(
            dcc.Graph(id='map-graph'),
            width={'size':4, 'offset':0}
        )
    ]),
    dbc.Row([
        dbc.Col(html.H5('''
            
            '''),
            width={'size':4, 'offset':1}
        ),
        dbc.Col(
            width={'size':4, 'offset':1}
        )
    ])
])
# Layout for Video Length Development
project_1_2_layout = html.Div([
    dbc.Row(
        [
            dbc.Col(
                html.H2('Analysis of Video Duration by Category (2013-2023)', style={'color': '#dd2b2b'}),
                width={'size': 5, 'offset': 1},
            ),
            dbc.Col(
                html.Div(
                    [
                        html.Br(),
                        dcc.Link("Home", href="/"),
                    ],
                    style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}
                ),
                width={'size':1, 'offset':5},
                className="bg-dark border",
                style={'color': '#2e6999'}
            ),
        ]
    ),
    dbc.Row(dbc.Col(html.H5('''
                        The following charts illustrate the average duration of videos across various categories over the period from 2013 to 2023 in the USA.
                        Each line or area represents a distinct category.
                        This analysis focuses on data from the United States, as it accounts for the highest traffic on the platform, providing a comprehensive overview.
>>>>>>> development
                    '''),
                width={'size': 4, 'offset': 1}
                ),
        ),
    dbc.Row(
        [
            dbc.Col(dcc.Dropdown(id='data-dropdown',
                                options=[
                                {'label': 'Original Data', 'value': 'original_data'},
                                {'label': 'Filtered Data', 'value': 'filtered_data'},
                                ],
                                value='original_data'
                            ),
                width={'size': 2, 'offset': 5, 'order': 0}
                ),
            dbc.Col(
                ),
        ]
    ),
    dbc.Row(
        [
            dbc.Col(html.H1()
                ),
            dbc.Col(
                ),
        ]
    ),
    dbc.Row(
        [
<<<<<<< HEAD
            dbc.Col(dcc.Graph(id='video-length-bar'),
                width={'size': 6, 'offset': 1}
                ),
            dbc.Col(
                ),
=======
            dbc.Col(dcc.Graph(id='video-length-lineplot'),
                width={'size': 6, 'offset': 1}
            ),
            dbc.Col(html.H5(id='text-output'),
            width=4
            ),
>>>>>>> development
        ]
    ),
    dbc.Row(
        [
            dbc.Col(html.H1()
                ),
            dbc.Col(
                ),
        ]
    ),
    dbc.Row(
        [
            dbc.Col(dcc.Graph(id='video-length-bar'),
                width={'size': 6, 'offset': 1}
            ),
            dbc.Col(html.H5('''
                    In the upper graph, it is evident how the average video duration significantly decreases in the 'Film & Animation' category,
                    as a large number of short films are included in the most-viewed videos over time. In the lower diagram, this category has been filtered out,
                    resulting in a much clearer trend. Up until the Short Release in 2021, the average video duration noticeably increases,
                    attributed to improved internet connectivity and consequently faster upload times.
                    '''),
                width=4
            ),
        ]
    ),
])
# Layout für Project 1-2
# project_1_2_layout = html.Div(
#     className='container-fluid',
#     children=[
#         html.H1(children="Youtube Video Length Development"),
#         html.Div(children='''
#             The development of the video duration over the past 10 years.
#         '''),
#         html.Div(
#             className='row',
#             children=[
#                 html.Div(
#                     style={'width': '20%', 'height': '10vh'},
#                     children=[
#                         dcc.Dropdown(
#                             id='data-dropdown',
#                             options=[
#                                 {'label': 'Original Data', 'value': 'original_data'},
#                                 {'label': 'Filtered Data', 'value': 'filtered_data'},
#                             ],
#                             value='original_data'
#                         )
#                     ]
#                 ),
#                 html.Div(
#                     style={'width': '70%', 'height': '100vh'},
#                     children=[
#                         dcc.Graph(id='video-length-bar'),
#                         dcc.Graph(id='video-length-lineplot')
#                     ]
#                 )
#             ]
#         )
#     ]
# )

# Layout for Project 2
project_2_layout = html.Div(
    children=[
        html.H1("Project 2"),
        html.Div("Here is a visualization for Project 2."),
    ]
)

# Layout for Project 3
project_3_layout = html.Div(
    children=[
        html.H1("Project 3"),
        html.Div("Here is a visualization for Project 3."),
    ]
)

# Callback to display the respective layouts based on the URL
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/project-1":
        return project_1_layout
    elif pathname == "/project-1.2":
        return project_1_2_layout
    elif pathname == "/project-2":
        return project_2_layout
    elif pathname == "/project-3":
        return project_3_layout
    else:
        return home_layout

# Layout of the entire page
app.layout = html.Div(
    children=[
        dcc.Location(id="url", refresh=False),
        html.Div(id="page-content")
    ]
)


# ------------------------------------------------------------------------------
# Callbacks
@app.callback(
    [Output('video-length-bar', 'figure'),
     Output('video-length-lineplot', 'figure'),
     Output('text-output', 'children')],
    [Input('data-dropdown', 'value')]
)

# Graphs for the Video Length Development 
def update_graphs(selected_data):
    if selected_data == 'original_data':
        data_to_use = video_length_data
        text_output = [html.B("The Original Data"), " refers to the unfiltered dataset obtained from the YouTube API through our request."]
    elif selected_data == 'filtered_data':
        data_to_use = filtered_video_length_data
        text_output = [
    html.Div([
        html.B("The Filtered Data"), 
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

<<<<<<< HEAD
    bar_fig = px.bar(
        data_to_use,
=======
    common_legend_title = 'Category'
    bar_data = data_to_use[data_to_use['Category Title'] != 'Film & Animation']
    bar_fig = px.area(
        bar_data,
>>>>>>> development
        x='Year',
        y='Duration_minutes',
        color='Category Title',
        # barmode='group',
        labels={'Year': 'Year', 'Duration_minutes': 'Duration in Minutes'},
        hover_data={'Category Title': False, 'Duration_minutes': ':.2f', 'Year': False},
        hover_name= 'Category Title',
    )
    bar_fig.update_traces(hovertemplate='Duration: %{y:.2f} min'),
    bar_fig.add_vline(x=2021, line_dash="dash", line_color="red", annotation_text="Shorts Release", annotation_font=dict(color="red")),
    bar_fig.add_vline(x=2020, line_dash="dash", line_color="red", annotation_text="Corona Pandemic", annotation_position="top left", annotation_font=dict(color="red"))

<<<<<<< HEAD
=======
    bar_fig.update_layout(
        plot_bgcolor='#e7e7e7',
        paper_bgcolor='#d1d1d1',
        legend_title=common_legend_title,
        height=550,
    )

>>>>>>> development
    line_fig = px.line(
        data_to_use,
        x='Year',
        y='Duration_minutes',
        color='Category Title',
        labels={'Year': 'Year', 'Duration_minutes': 'Duration in Minutes'},
        hover_data={'Category Title': False, 'Duration_minutes': ':.2f', 'Year': False},
        hover_name= 'Category Title',
        title='Average Video Duration by Category',
        # markers=True,
    )
    line_fig.update_traces(hovertemplate='Duration: %{y:.2f} min'),
    line_fig.add_vline(x=2021, line_dash="dash", line_color="red", annotation_text="Shorts Release", annotation_font=dict(color="red")),
    line_fig.add_vline(x=2020, line_dash="dash", line_color="red", annotation_text="Corona Pandemic", annotation_position="top left", annotation_font=dict(color="red")),

    line_fig.update_layout(
<<<<<<< HEAD
    plot_bgcolor='#1f2630',
    paper_bgcolor='#ededed',
    )

    return bar_fig, line_fig
=======
        plot_bgcolor='#e7e7e7',
        paper_bgcolor='#d1d1d1',
        legend_title=common_legend_title,
        height=550,
    )

    return bar_fig, line_fig, text_output

@app.callback(
    Output('pie-chart', 'figure'),
    [Input('country-dropdown', 'value'),
     Input('date-picker', 'date')]
)
def update_pie_chart(selected_country, selected_date):
    if selected_country is None or selected_date is None:
        return {}

    file_path = f'{data_folder}/{selected_country}_category_distribution.csv'
    df = pd.read_csv(file_path)

    selected_date = datetime.strptime(selected_date[:10], '%Y-%m-%d')
    df_selected_date = df[df['Execution Date'] == selected_date.strftime('%Y-%m-%d')]

    if df_selected_date.empty:
        return {
            'data': [],
            'layout': {
                'annotations': [{
                    'text': 'No data available for the selected date.',
                    'x': 0.5,
                    'y': 0.5,
                    'xref': 'paper',
                    'yref': 'paper',
                    'showarrow': False,
                    'font': {
                        'size': 25
                    }
                }],
                'showlegend': False,
                'plot_bgcolor': '#d1d1d1',
                'paper_bgcolor': '#d1d1d1',
                'xaxis': {'visible': False},
                'yaxis': {'visible': False}
            }
        }

    df_grouped = df_selected_date.groupby('Category Title')['Quantity'].sum().reset_index()
    pie = px.pie(df_grouped, values='Quantity', names='Category Title', hover_name='Category Title')
    pie.update_traces(hovertemplate='%{hovertext}')
    pie.update_layout(
        # showlegend=False,
        plot_bgcolor='#e7e7e7',
        paper_bgcolor='#d1d1d1',
    )
    return pie

@app.callback(
    Output('map-graph', 'figure'),
    [Input('country-dropdown', 'value')]
)     
def update_map(selected_country):
    if selected_country is None:
        return {}

    # Lade die Koordinaten für das ausgewählte Land
    country_lat, country_lon = get_country_coordinates(selected_country)

    # Erstelle eine Karte mit dem ausgewählten Land zentriert
    map_fig = px.choropleth_mapbox(
        color=[1],
        mapbox_style="carto-positron",
        center={"lat": country_lat, "lon": country_lon},
        zoom=3
    )
    map_fig.update_layout(
        plot_bgcolor='#e7e7e7',
        paper_bgcolor='#d1d1d1',
        margin={"r":0,"t":0,"l":0,"b":0}
    )
    return map_fig

@app.callback(
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

# App starten
if __name__ == '__main__':
    app.run_server(debug=True)
>>>>>>> development
# ------------------------------------------------------------------------------
# Starting the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)