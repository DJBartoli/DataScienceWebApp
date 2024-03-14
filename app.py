import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)
server = app.server

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
        html.Div("Here is a visualization for Project 1."),
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

# Starting the Dash app
if __name__ == "__main__":
    app.run_server(debug=True)