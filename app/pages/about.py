"""About page. This page is a placeholder for the about page."""
import dash
from dash import Input, Output, html, callback
import dash_bootstrap_components as dbc
from layout import layout as com

dash.register_page(__name__, path='/about', title='About', name='About')

about_app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout for the about page
layout = html.Div([
    dbc.Container(fluid=True, children=[
        # Header
        dbc.Row(dbc.Col(html.H1("About ReLease!", className="text-center my-5"), width=12)),

        # Content Section
        dbc.Row(dbc.Col(
            html.Div([
                html.H2("Our Mission", className="mt-4 mb-3"),
                html.P("In Canada, specifically in Montreal, people might want to move from their apartment, but there may still be some time (a year or more) left in the lease contract. Landlords usually have high penalties for breaking their contract before the expiration date, so people usually rush to find someone else to transfer their lease to. Currently, there does not exist a specific website solely for this purpose. ", className="mb-3"),
                html.P("Our website is intended to facilitate the lease transfer process between the citizens of Montreal during the current housing crisis. The application would enable tenants to advertise their apartments, post their current lease agreement clauses, the period in which they would like to find another lease, and what they are looking for during the transfer process.", className="mb-3"),
                html.H2("About creators", className="mt-4 mb-3"),
                html.P("The creators of this website:", className="mb-3"),
                html.P("• Murad Novruzov (McGill University)", className="mb-3"),
                html.P("• Emilia Krichevsky (Concordia University)"),
                html.P("• Vicky Li-Yoo (Concordia University)"),
                html.P("• Muhammad Sohail (McGill University)"),
                # More sections as needed
            ]),
            width={"size": 8, "offset": 2}  # Center the column with offset
        )),

        # Contact Section with a different style
        dbc.Row(dbc.Col(
            html.Div([
                html.H2("Contact Information", className="text-center my-4"),
                html.P("You can reach us at:", className="text-center"),
                html.P("Email: murad.novruzov@mail.mcgill.ca", className="text-center"),
                # Add more contact information as needed
            ], className="bg-light p-4 rounded"),  # This div has a different background color and is rounded
            width=12
        ))
    ])
])