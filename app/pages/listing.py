# Page to display a single listing
import dash
from dash import Input, Output, html, callback, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from server import functions as f

dash.register_page(
    __name__, path_template="/listing/<listing_id>", title="Listing", name="Listing"
)

layout = dbc.Container(
    [],
    id="listing_id",
)


@callback(
    Output("listing_id", "children"),
    [Input("listing_id", "children")],
    State("store", "data"),
)
def display_listing(c, store):
    doc = f.get_document(store["id"])
    return setup(doc)


def setup(doc):
    jumbotron = html.Div(
        dbc.Container(
            [
                html.H1(doc["title"], className="display-3"),
                html.P(
                    [
                        dmc.Badge(doc["location"], size="xl"),
                        dmc.Badge(
                            "$ {}".format(doc["price_range"]), color="red", size="xl"
                        ),
                        dmc.Badge("Size: {}".format(doc["size"]), size="xl"),
                    ],
                    className="lead",
                ),
                html.Hr(className="my-2"),
                html.P(
                    doc["description"],
                    className="lead",
                ),
                dmc.Group(
                    position="apart",
                    children=[
                        dmc.Image(
                            src=doc["image"],
                            withPlaceholder=True,
                            placeholder=[dmc.Loader(color="gray", size="sm")],
                        ),
                        dbc.Card(
                            [
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dbc.CardBody(
                                                [
                                                    html.H4(
                                                        "Tenant Name: {}".format(
                                                            doc["tenant_name"]
                                                        ),
                                                        className="lead",
                                                    ),
                                                    html.P(
                                                        "Landlord Name: {}".format(
                                                            doc["landlord_name"]
                                                        ),
                                                        className="lead",
                                                    ),
                                                    html.P(
                                                        dbc.Button(
                                                            "Contact", color="info"
                                                        ),
                                                        className="lead",
                                                    ),
                                                    html.Small(
                                                        "Last update on {}".format(
                                                            doc["date"]
                                                        ),
                                                        className="card-text text-muted",
                                                    ),
                                                ]
                                            ),
                                            className="col-md-8",
                                        ),
                                    ],
                                    className="g-0 d-flex align-items-center",
                                )
                            ],
                            className="mb-3",
                            style={"maxWidth": "540px"},
                        ),
                    ],
                ),
            ],
            fluid=True,
            className="py-3",
        ),
        className="p-3 bg-light rounded-3",
    )
    return jumbotron
