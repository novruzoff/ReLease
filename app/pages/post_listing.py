import dash
from dash import Dash, dcc, html, Input, Output, State, callback
import dash_bootstrap_components as dbc
import datetime
from datetime import date

about_app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

dash.register_page(
    __name__,
    path="/post_listing",
    title="Create Your Listing",
    name="Create Your Listing",
)

layout = html.Div(
    [
        dbc.Container(
            fluid=True,
            children=[
                # Header
                dbc.Row(
                    [
                        dbc.Col(
                            html.H1(
                                "Create Your Listing", className="text-center my-5"
                            ),
                            width=12,
                        )
                    ]
                ),
                # Image row section
                dbc.Row(
                    [
                        # Image upload section
                        dbc.Col(
                            html.Div(
                                [
                                    dcc.Upload(
                                        id="upload-image",
                                        children=html.Div(
                                            [
                                                "Drag and Drop or ",
                                                html.A("Select Files"),
                                            ]
                                        ),
                                        style={
                                            "width": "100%",
                                            "height": "",
                                            "lineHeight": "50vh",
                                            "borderWidth": "2px",
                                            "borderStyle": "dashed",
                                            "borderRadius": "5px",
                                            "textAlign": "center",
                                            "marginLeft": "10px",
                                        },
                                        # Allow multiple files to be uploaded
                                        multiple=True,
                                    ),
                                    html.Div(id="output-image-upload"),
                                ]
                            ),
                            width=4,
                        ),
                        # Listing information input
                        dbc.Col(
                            html.Div(
                                [
                                    dbc.Label("Listing Title"),
                                    dbc.Input(
                                        type="text",
                                        style={
                                            "borderWidth": "2px",
                                            "borderColor": "grey",
                                        },
                                    ),
                                    dbc.Label("Price"),
                                    dbc.Input(
                                        type="number",
                                        style={
                                            "borderWidth": "2px",
                                            "borderColor": "grey",
                                        },
                                    ),
                                    dbc.Label("Address"),
                                    dbc.Input(
                                        type="text",
                                        style={
                                            "borderWidth": "2px",
                                            "borderColor": "grey",
                                        },
                                    ),
                                    dbc.Label("Transfer Date"),
                                    dcc.DatePickerSingle(
                                        id="my-date-picker-single",
                                        min_date_allowed=date(2024, 1, 1),
                                        max_date_allowed=date(2050, 9, 19),
                                        initial_visible_month=date(2024, 1, 28),
                                        date=date(2024, 1, 28),
                                        className="mt-4",
                                    ),
                                    dbc.Label("Lease End Date"),
                                    dcc.DatePickerSingle(
                                        id="my-date-picker-single",
                                        min_date_allowed=date(2024, 1, 1),
                                        max_date_allowed=date(2050, 9, 19),
                                        initial_visible_month=date(2024, 1, 28),
                                        date=date(2024, 1, 28),
                                        className="mt-4",
                                    ),
                                ]
                            )
                        ),
                    ],
                ),
                # Decription row section
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [
                                    dbc.Label('Description'),
                                    dbc.Textarea(
                                        className="mlb-3", placeholder="A Textarea"
                                    )
                                ], style={'marginLeft': '10px', 'marginTop': '10px'}
                            )
                        )
                    ]
                ),
            ],
        )
    ]
)


# Callback for image upload
def parse_contents(contents, filename, date):
    return html.Div(
        [
            html.H5(filename),
            html.H6(datetime.datetime.fromtimestamp(date)),
            # HTML images accept base64 encoded strings in the same format
            # that is supplied by the upload
            html.Img(src=contents),
            html.Hr(),
            html.Div("Raw Content"),
            html.Pre(
                contents[0:200] + "...",
                style={"whiteSpace": "pre-wrap", "wordBreak": "break-all"},
            ),
        ]
    )


@callback(
    Output("output-image-upload", "children"),
    Input("upload-image", "contents"),
    State("upload-image", "filename"),
    State("upload-image", "last_modified"),
)
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d)
            for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)
        ]
        return children
