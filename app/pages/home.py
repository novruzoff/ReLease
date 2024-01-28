"""
This module defines the home page for the ReLease web application.

Functions:
    update_catalog(cards): Retrieves all documents from a data source, creates a card for each 
    document, and adds these cards to the catalog.

Imports:
    dash: The core Dash backend.
    dash_bootstrap_components as dbc: Components from the Dash Bootstrap library.
    server.functions as f: Functions for performing CRUD operations on the MongoDB database.
    dash_mantine_components as dmc: Additional components from the Dash Mantine library.
    layout.layout as com: The layout for the page.
"""
import dash
from dash import Input, Output, html, callback
import dash_bootstrap_components as dbc
from server import functions as f
import dash_mantine_components as dmc
from layout import layout as com

dash.register_page(__name__, path="/", title="ReLease", name="ReLease")


layout = dbc.Container(
    [
        html.H1("Welcome!"),
        dbc.Row(
            dbc.Col(
                html.Div(
                    "Browse our catalog of leases, made for Montrealers by Montrealers"
                )
            ), class_name='mb-4'
        ),
        com.grid,
    ]
)


@callback(Output("grid", "children"), [Input("grid", "children")])
def update_catalog(cards):
    """
    Updates the catalog with new cards created from documents.

    This function retrieves all documents from a data source, creates a card for each document,
    and adds these cards to the catalog. The cards are then returned to be displayed in the UI.

    Args:
        cards (list): A list of existing cards in the catalog.

    Returns:
        list: A list of cards created from the documents.
    """
    cards = []
    for doc in f.get_all_documents():
        card = create_card(doc)

        cards.append(card)
    return cards

# @callback(Output("listing_id", "children"), [Input("view-listing-btn", "n_clicks")])
# def view_listing(n_clicks):
    # return n_clicks
    

def create_card(doc) -> dmc.Card:
    """
    Create a Mantine Card component based on the given document.

    Args:
        doc (dict): The document containing information for the card.

    Returns:
        dmc.Card: The Mantine Card component.
    """
    man = dmc.Card(
        children=[
            dmc.CardSection(
                dmc.Image(
                    src=doc["image"],
                    height=160,
                )
            ),
            dmc.Group(
                [
                    dmc.Text(doc["title"], weight=500),
                    dmc.Badge("On Sale", color="red", variant="light"),
                ],
                position="apart",
                mt="md",
                mb="xs",
            ),
            dmc.Text(
                doc["description"],
                size="sm",
                color="dimmed",
            ),
            dmc.Button(
                dmc.NavLink(label="View listing", href='/listing/{}'.format(doc['_id']), variant='light'),#change
                variant="light",
                color="blue",
                fullWidth=True,
                mt="md",
                radius="md",
                id="view-listing-btn",
            ),
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        style={"width": 350},
    )
    return man
