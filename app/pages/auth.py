# Authentication Page
import dash
from dash import Input, Output, html, callback
import dash_bootstrap_components as dbc
from layout import layout as com

dash.register_page(__name__, path='/login', title='Login', name='Login')

layout = html.Div(
    children=[
        html.Iframe(
            src="/assets/login.html",
            style={"height": "1067px", "width": "100%"},
        )
    ]
)