import dash
from dash import Input, Output, html, callback
import dash_bootstrap_components as dbc
from layout import layout as com

dash.register_page(__name__, path='/', title='ReLease', name='ReLease')


layout = dbc.Container([
    html.H1('Welcome!'),
    html.Div('Browse our catalog of listings, from Montrealers to Montrealers'),
    com.group
    
])

# in callback: get all documents, for every document create a card component and return it to the cardgroup children
@callback(Output("cardgroup", "children"),[Input("cardgroup", "children")])
def update_catalog(cardgroup):
    # Here you should fetch the actual listings from a database or service.
    # This function returns placeholder elements for demonstration.
    # You would replace this with your actual data retrieval and processing.
    return [
        
            com.card  # Add the card to the layout
        
        for _ in range(10)  # Replace with actual number of listings
    ]
