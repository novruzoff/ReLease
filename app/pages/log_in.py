import dash
from dash import Input, Output, html, callback
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/log_in",
    title="Log in",
    name="Log in",
)

layout = (html.H1('log in')

)