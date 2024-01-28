import dash
from dash import html
import dash_bootstrap_components as dbc
from layout import layout as com

# Initialize the Dash app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.LITERA, dbc.icons.FONT_AWESOME],
    use_pages=True,
)


# Define the app layout
app.layout = html.Div(
    [
        # Top bar with Login and Sign Up
        com.navbar,
        dbc.Container(children=[dash.page_container], id="page-content"),
    ],
)

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
