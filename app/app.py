"""
This module initializes and runs the Dash application for the ReLease web application.
"""
import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
from layout import layout as com

# Initialize the Dash app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.LITERA, dbc.icons.FONT_AWESOME],
    use_pages=True,
    suppress_callback_exceptions=True,
)

# Define the app layout
app.layout = html.Div(
    [
        # Top bar with Login and Sign Up
        dcc.Store(id="store", storage_type="session"),
        com.navbar,
        dbc.Container(children=[dash.page_container], id="page-content"),
    ],
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
