import os
from datetime import datetime, timedelta
import json

import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

from geopy.geocoders import Nominatim
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import json
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

layout = html.Div(
    html.H1('Introducing the YouTube API', style ={'text-align': 'center'}),

)