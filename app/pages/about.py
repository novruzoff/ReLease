"""About page. This page is a placeholder for the about page."""
import dash
from dash import Input, Output, html, callback
import dash_bootstrap_components as dbc
from layout import layout as com

dash.register_page(__name__, path='/about', title='About', name='About')

layout = dbc.Container([
    html.H1('About ReLease!'),
    
])