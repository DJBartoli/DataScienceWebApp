import dash
import dash_bootstrap_components as dbc

from dash import dcc, html, callback


dash.register_page(__name__, name='Imprint')

layout = (
    html.Div(
        dbc.Row(
            [
                dbc.Col([
                    html.H2('Imprint'),
                    html.P('Responsible for all content:'),
                    html.P('Anton Ach, Dante Bartoli, Konstantin Hamann'),
                    html.P('stu231800@uni-kiel.de'),
                    html.P('Preetzer Straße 37'),
                    html.P('24223 Schwentinental'),
                ],
                width={'size': 6, 'offset': 3}
                )
            ],

        )
    )

)
