import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import json

app = dash.Dash(__name__)
server = app.server

with open('custom.geo.json', encoding='utf-8') as f:
    geojson_data = json.load(f)

# ------------------------------------------------------------------------------
# App layout
# Layout of the home page
home_layout = html.Div(
    children=[
        html.H1("Welcome to the Home Page"),
        html.Div("Select a project to visualize:"),
        dcc.Link("Project 1", href="/project-1"),
        html.Br(),
        dcc.Link("Project 2", href="/project-2"),
        html.Br(),
        dcc.Link("Project 3", href="/project-3"),
    ]
)

# Layout for Project 1
project_1_layout = html.Div(
    children=[
        html.H1("Project 1"),
        dcc.Graph(id='map-graph')
    ]
)

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
# Connect the Plotly graphs with Dash Components
@app.callback(
    Output('map-graph', 'figure'),
    [Input('url', 'pathname')]
)
def update_map(pathname):
    if pathname == '/project-1':  # Update the map only for Project 1
        # Dummy DataFrame for demonstration purposes
        df = pd.DataFrame({
            'location': ['Location1', 'Location2', 'Location3'],  # Sample location data
            'property_to_color': [10, 20, 30]  # Sample data for color representation
        })
        
        fig = px.choropleth_mapbox(
            geojson=geojson_data,
            locations=df['location'],  # Add the appropriate location data from the DataFrame
            featureidkey="properties.id",  # Adjust this according to your GeoJSON structure
            color=df['property_to_color'],  # Add the appropriate column from the DataFrame for color representation
            mapbox_style="carto-positron",
            zoom=3,  # Adjust the zoom level
            center={"lat": 51, "lon": 9},  # Adjust the center accordingly
            opacity=0.5
        )
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})  # Layout adjustments
        return fig
    else:
        return {}
# ------------------------------------------------------------------------------
# Starting the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)