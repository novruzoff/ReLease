import dash
from dash import Input, Output, html, callback
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/sign_up",
    title="Sign Up",
    name="Sign Up",
)

layout = (html.H1('Sign Up')

)