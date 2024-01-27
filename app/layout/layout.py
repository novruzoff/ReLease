import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc


card_body = dbc.CardBody(
    [
        html.H4("Card title", className="card-title"),
        html.P(
            "This is some card content that we'll reuse",
            className="card-text",
        ),
    ]
)

card = dbc.Card(card_body, color="primary", inverse=True)