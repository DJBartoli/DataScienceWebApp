import os
from datetime import datetime, timedelta
import json

import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px

from geopy.geocoders import Nominatim
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import json
import dash_bootstrap_components as dbc


dash.register_page(__name__, )

geolocator = Nominatim(user_agent="country_locator")


with open('data/europe.geojson', encoding='utf-8') as f:
    geojson_data = json.load(f)

data_folder = 'data/Trends100vRegions'

eu_countries_iso2 = {
    'Austria': 'AT',
    'Australia': 'AU',
    'Belgium': 'BE',
    'Brazil': 'BR',
    'Bulgaria': 'BG',
    'Canada': 'CA',
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
    'India': 'IN',
    'Ireland': 'IE',
    'Italy': 'IT',
    'Japan': 'JP',
    'Latvia': 'LV',
    'Lithuania': 'LT',
    'Luxembourg': 'LU',
    'Malta': 'MT',
    'Netherlands': 'NL',
    'Niger': 'NG',
    'Poland': 'PL',
    'Portugal': 'PT',
    'Romania': 'RO',
    'Slovakia': 'SK',
    'Slovenia': 'SI',
    'Spain': 'ES',
    'Sweden': 'SE',
    'United Kingdom': 'GB',
    'USA': 'US',
}

category_options = pd.read_csv('data/Categories.csv')

file_list = os.listdir(data_folder)
dfs = []

for file_name in file_list:
    if file_name.endswith('.csv'):
        df = pd.read_csv(os.path.join(data_folder, file_name))
        df['Country'] = file_name[:2]
        dfs.append(df)
weekly_df = pd.concat(dfs, ignore_index=True)


def get_country_coordinates(country):
    location = geolocator.geocode(country)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None


pie_data = pd.read_csv(f'{data_folder}/DE_category_distribution.csv')
df_selected_date = pie_data[pie_data['Execution Date'] == '2024-03-15']
selected_pie_data = df_selected_date.groupby('Category Title')['Quantity'].sum().reset_index()
pie_first_data = px.pie(selected_pie_data, values='Quantity', names='Category Title',
                        hover_data={'Category Title': False, 'Quantity': True}, hover_name='Category Title')
pie_first_data.update_traces(hovertemplate='Quantity')

#///////////////Layout//////////////////
layout = html.Div([
    dbc.Row(
        [
            dbc.Col(
                html.H2('Youtube Trends Analytics', style={'color': '#dd2b2b'}),
                width={'size': 5, 'offset': 1},
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
            style={'color': '#262626'},
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
            width={'size': 4, 'offset': 1}
        ),
        dbc.Col(
            dcc.Graph(id='map-graph'),
            width={'size': 4, 'offset': 0}
        )
    ]),
    dbc.Row([
        dbc.Col(html.H2('''

            '''),
                )
    ]),
    dbc.Row([
        dbc.Col(dcc.Dropdown(
            id='category-dropdown',
            options=[{'label': category, 'value': category} for category in category_options['Category Title']],
            value=None,
            placeholder="Select a category",
        ),
            style={'color': '#262626'},
            width={'size': 2, 'offset': 1}
        ),
        dbc.Col(dcc.Graph(id='weekly-graph'), width=4)
    ]),
    dbc.Row([
        dbc.Col(html.H5('''
                Here, you can view the distribution of individual
                 categories over a few days for the selected country above.
                '''),
                width={'size': 2, 'offset': 1}
                )
    ])
])

@callback(
    Output('weekly-graph', 'figure'),
    [Input('category-dropdown', 'value'),
    Input('country-dropdown', 'value')]
)


def update_weeklygraph(selected_category, selected_country):
    if selected_category and selected_country:
        weekly_df['Execution Date'] = pd.to_datetime(weekly_df['Execution Date'])
        filtered_df = weekly_df[(weekly_df['Category Title'] == selected_category) &
                                (weekly_df['Country'] == selected_country) &
                                (weekly_df['Execution Date'] >= weekly_df['Execution Date'].min()) &
                                (weekly_df['Execution Date'] <= weekly_df['Execution Date'].max())]
        weekly_fig = px.bar(filtered_df, x='Execution Date', y='Quantity', color='Country', title=f'Data for {selected_category} in {selected_country}')
        weekly_fig.update_traces(marker_color='#dd2b2b')
        weekly_fig.update_xaxes(title_text='Date')
        weekly_fig.update_yaxes(title_text='Distribution')
        weekly_fig.update_layout(
            plot_bgcolor='#e7e7e7',
            paper_bgcolor='#d1d1d1',
            showlegend=False)
        return weekly_fig
    else:
        return {}

@callback(
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


@callback(
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
        margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )
    return map_fig
