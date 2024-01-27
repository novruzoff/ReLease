import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/home', title='ReLease', name='ReLease')


layout = dbc.Container([
    html.H1('This is our Home page'),
    html.Div('This is our Home page content.'),
    
])