# Page to display a single listing
import dash
from dash import Input, Output, html, callback
import dash_bootstrap_components as dbc
from layout import layout as com

dash.register_page(__name__, path='/listing', title='Listing', name='Listing')

layout = dbc.Container([
    html.H1('Listing!'),
    # html.Div('Browse our catalog of listings, from Montrealers to Montrealers'),
    # com.group
    
])
