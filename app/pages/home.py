import dash
from dash import Input, Output, html, callback
import dash_bootstrap_components as dbc
from server import functions as f

dash.register_page(__name__, path="/", title="ReLease", name="ReLease")


layout = dbc.Container(
    [
        html.H1("Welcome!"),
        html.Div("Browse our catalog of listings, from Montrealers to Montrealers"),
        html.Div(id="cards")
    ]
)


# in callback: get all documents, for every document create a card component and return it to the cardgroup children
@callback(Output("cards", "children"), [Input("cards", "children")])
def update_catalog(cards):
    cards = []
    for doc in f.get_all_documents():
        print(doc)
        card = dbc.Card(
                [
                    dbc.CardHeader(doc["location"]),
                    dbc.CardBody(
                        [
                            html.H5(doc["title"], className="card-title"),
                            html.P(
                                doc["description"],
                                className="card-text",
                            ),
                        ]
                    ),
                ]
            )
        cards.append(card)
    return cards
