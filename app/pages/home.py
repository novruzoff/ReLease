import dash
from dash import Input, Output, html, callback
import dash_bootstrap_components as dbc
from server import functions as f

dash.register_page(__name__, path="/", title="ReLease", name="ReLease")


layout = dbc.Container(
    [
        html.H1("Welcome!"),
        html.Div("Browse our catalog of listings, from Montrealers to Montrealers"),
        html.Div(id="cards"),
    ]
)

@callback(Output("cards", "children"), [Input("cards", "children")])
def update_catalog(cards):
    cards = []
    for doc in f.get_all_documents():
        print(doc)
        card = dbc.Card(
            [
                dbc.CardImg(src=doc['image'], top=True),
                dbc.CardBody(
                    [
                        html.H4(doc["title"], className="card-title"),
                        html.H5(doc["location"], className="card-text"),
                        html.P(
                            doc["description"],
                            className="card-text",
                        ),
                        dbc.Button("See more", color="info"), # add link to the individual listing page
                    ]
                ),
            ],
            style={"width": "18rem"},
            color="secondary",
            inverse=True,
        )
        cards.append(card)
    return cards
