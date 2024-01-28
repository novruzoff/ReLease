from dash import html
import dash_bootstrap_components as dbc

links = dbc.Nav(
    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.NavItem(
                        dbc.NavLink(
                            "Sign up",
                            active=True,
                            href="#",
                        ),
                        className="ms-2",
                    ),
                ],
                width="auto",
            ),
            dbc.Col(
                dbc.NavItem(
                    dbc.NavLink(
                        "Login",
                        active=True,
                        href="#",
                    ),
                    className="ms-2",
                ),
                width="auto",
            ),
            dbc.Col(
                dbc.NavItem(
                    dbc.NavLink("About", active=True, href="#", disabled=True),
                    className="ms-2",
                ),
                width="auto",
            ),
            dbc.Col(
                dbc.NavLink(
                    "",
                    href="https://github.com/emiliakrichevsky/ReLease",
                    class_name="fa-brands fa-github fa-xl",
                    style={"color": "#4582ec"},
                ),
                className="ms-2",   
                width="auto",
            ),
        ],
        className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
        align="center",
    ),
    pills=True,
    className="ms-auto",
)


# navigation bar
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [  
                        dbc.Col(
                            dbc.NavbarBrand(
                                html.Img(src="/assets/mainlogo.png", height="60px")
                            )
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="#",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                links,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="secondary",
    dark=True,
)

card_body = dbc.CardBody(
    [
        html.H4("Card title", className="card-title"),
        html.P(
            "This is some card content that we'll reuse",
            className="card-text",
        ),
    ]
)

card = dbc.Card(
    children=[
        dbc.CardImg(
            src="https://storage.cloud.google.com/release_bucket/images/10.jpg", #temp
            top=True,
        ),
        card_body,
    ],
    color="secondary",
    inverse=True,
)

group = dbc.CardGroup([], id="cardgroup", className="card-group")

filter_menu = dbc.Container([])
