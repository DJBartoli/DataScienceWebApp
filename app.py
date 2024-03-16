import os
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import json
import dash_bootstrap_components as dbc
from datetime import datetime

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

with open('data\\europe.geojson', encoding='utf-8') as f:
    geojson_data = json.load(f)

video_length_data = pd.read_csv('VideoLengthData.csv')
filtered_video_length_data = pd.read_csv('Filtered_VideoLengthData.csv')

data_folder = 'data\\Trends100vRegions'

eu_countries_iso2 = {
    'Austria': 'AT',
    'Australia':'AU',
    'Belarus': 'BY',
    'Belgium': 'BE',
    'Brazil':'BR',
    'Bulgaria': 'BG',
    'Canada':'CA',
    'Croatia': 'HR',
    'Cyprus': 'CY',
    'Czech Republic': 'CZ',
    'Denmark': 'DK',
    'Estonia': 'EE',
    'Finland': 'FI',
    'France': 'FR',
    'Germany': 'DE',
    'Greece': 'GR',
    'Hungary': 'HU',
    'India':'IN',
    'Ireland': 'IE',
    'Italy': 'IT',
    'Japan':'JP',
    'Latvia': 'LV',
    'Lithuania': 'LT',
    'Luxembourg': 'LU',
    'Malta': 'MT',
    'Netherlands': 'NL',
    'Niger':'NI',
    'Poland': 'PL',
    'Portugal': 'PT',
    'Romania': 'RO',
    'Slovakia': 'SK',
    'Slovenia': 'SI',
    'Spain': 'ES',
    'Sweden': 'SE',
    'United Kingdom': 'GB',
    'USA':'US',
}

# world_map = px.choropleth_mapbox(
#         # europe_geojson,
#         locations=['id'],
#         featureidkey="properties.id",
#         mapbox_style="carto-positron",
#         zoom=3,
#         center={"lat": 51, "lon": 9},
#         opacity=0.5,
#         width=800,
#         height=1000,
#     )
# world_map.update_layout(clickmode='event+select')

# ------------------------------------------------------------------------------
# App layout
# Layout of the home page
home_layout = html.Div(
    children=[
        html.H1("Welcome to the Home Page"),
        html.Div("Select a project to visualize:"),
        dcc.Link("Project 1", href="/project-1"),
        html.Br(),
        dcc.Link("Video Length Development", href="/video-length"),
        html.Br(),
        dcc.Link("Project 2", href="/project-2"),
        html.Br(),
        dcc.Link("Project 3", href="/project-3"),
        html.Br(),
        dcc.Link("Home", href="/"),
    ]
)

# Layout for Project 1
project_1_layout = html.Div([
    dbc.Row(
        [
            dbc.Col(
                html.H2('Youtube Trends Analytics', style={'color': '#dd2b2b'}),
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
    # dbc.Row(dbc.Col(html.Div('''
    #                     A interactive Worldmap.
    #                 '''),
    #             width={'size': 4, 'offset': 1}
    #             ),
    #     ),
    # dbc.Row(
    #     [
    #         dbc.Col(dcc.Graph(id='europe-map', config={'scrollZoom': False}),
    #             width={'size':5,'offset':1},
    #             ),
    #         dbc.Col(html.Div(id='iso2-output'),
    #             width={'size':4, 'offset':1},
    #             ),
    #     ]
    # ),
    dbc.Row([
        dbc.Col(
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': iso2} for country, iso2 in eu_countries_iso2.items()],
                value='DE'
            ),
            style={'color':'#262626'},
            width={'size': 2, 'offset': 0, 'order': 1}
        ),
        dbc.Col(
            dcc.DatePickerSingle(
                id='date-picker',
                min_date_allowed=datetime(2024, 3, 6),
                max_date_allowed=datetime.today(),
                initial_visible_month=datetime.today(),
                date=datetime.today()
            ),
            width={'size': 1, 'offset': 1, 'order': 0}
        ),
    ]),
    dbc.Row([
        dbc.Col(
            dcc.Graph(id='pie-chart'),
            width={'size':4, 'offset':1}
        )
    ])
])
project_1_2_layout = html.Div([
    dbc.Row(
        [
            dbc.Col(
                html.H2('Youtube Video Length Development', style={'color': '#dd2b2b'}),
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
                style={'color':'#262626'},
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
            dbc.Col(html.H5('''
            Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
            sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
            Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
            At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.
            '''),
            width=4
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
    elif pathname == "/video-length":
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

    common_legend_title = 'Category'

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
        legend_title=common_legend_title 
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
        legend_title=common_legend_title 
    )

    return bar_fig, line_fig

@app.callback(
    Output('pie-chart', 'figure'),
    [Input('country-dropdown', 'value'),
     Input('date-picker', 'date')]
)
def update_pie_chart(selected_country, selected_date):
    if selected_country is None or selected_date is None:
        return {}

    # Lade die Daten aus der CSV-Datei
    file_path = f'{data_folder}/{selected_country}_category_distribution.csv'
    df = pd.read_csv(file_path)

    # Filtere nach dem ausgewählten Datum
    selected_date = datetime.strptime(selected_date, '%Y-%m-%d')
    df_selected_date = df[df['Execution Date'] == selected_date.strftime('%Y-%m-%d')]

    # Gruppiere nach Kategorie und berechne die Summe der Menge
    df_grouped = df_selected_date.groupby('Category Title')['Quantity'].sum().reset_index()

    # Erstelle das Tortendiagramm
    fig = px.pie(df_grouped, values='Quantity', names='Category Title')
    return fig

# App starten
if __name__ == '__main__':
    app.run_server(debug=True)
# ------------------------------------------------------------------------------
# Starting the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)