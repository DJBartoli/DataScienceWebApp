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
        html.H1("Welcome to the Home Page"),
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
            dbc.Col(dcc.Graph(id='video-length-bar'),
                width={'size': 6, 'offset': 1}
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
            dbc.Col(dcc.Graph(id='video-length-lineplot'),
                width={'size': 6, 'offset': 1}
                ),
            dbc.Col(
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
     Output('video-length-lineplot', 'figure')],
    [Input('data-dropdown', 'value')]
)
def update_graphs(selected_data):
    if selected_data == 'original_data':
        data_to_use = video_length_data
    elif selected_data == 'filtered_data':
        data_to_use = filtered_video_length_data

    bar_fig = px.bar(
        data_to_use,
        x='Year',
        y='Duration_minutes',
        color='Category Title',
        barmode='group',
        labels={'Year': 'Year', 'Duration_minutes': 'Duration in Minutes'},
        hover_data={'Category Title': False, 'Duration_minutes': ':.2f', 'Year': False},
        hover_name= 'Category Title'
    )
    bar_fig.update_traces(hovertemplate='Duration: %{y:.2f} min')

    bar_fig.update_layout(
    plot_bgcolor='#e7e7e7',
    paper_bgcolor='#d1d1d1',
    )

    line_fig = px.line(
        data_to_use,
        x='Year',
        y='Duration_minutes',
        color='Category Title',
        markers=True,
        labels={'Year': 'Year', 'Duration_minutes': 'Duration in Minutes'},
        hover_data={'Category Title': False, 'Duration_minutes': ':.2f', 'Year': False},
        hover_name= 'Category Title'
    )
    line_fig.update_traces(hovertemplate='Duration: %{y:.2f} min')

    line_fig.update_layout(
    plot_bgcolor='#e7e7e7',
    paper_bgcolor='#d1d1d1',
    )

    return bar_fig, line_fig
# ------------------------------------------------------------------------------
# Starting the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)