from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

grid = dmc.SimpleGrid(id="grid", cols=3, spacing='lg', children=[])

links = dbc.Nav(
    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.NavItem(
                        dbc.NavLink(
                            "Post a Listing",
                            active=True,
                            href="/post_listing",
                        ),
                        className="ms-2",
                    ),
                ],
                width="auto",
            ),
            dbc.Col(
                [
                    dbc.NavItem(
                        dbc.NavLink(
                            "Sign up",
                            active=True,
                            href="/assets/signup.html",
                            target="_blank",
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
                        href="/login.html", #href="/assets/login.html", target="_blank"
                        target="_blank",
                    ),
                    className="ms-2",
                ),
                width="auto",
            ),
            dbc.Col(
                dbc.NavItem(
                    dbc.NavLink("About", active=True, href="/about"),
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
                                html.Img(src="/assets/mainlogo.png", height="60px"),
                                href="/",
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
    color="dark",
    dark=True,
)


filter_menu = dbc.Container([])
