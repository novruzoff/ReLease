import dash
from dash import Input, Output, html, callback
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/log_in",
    title="Log in",
    name="Log in",
)

layout = html.Div([
        dbc.Container(
            fluid=True,
            children=[
                # Header
                dbc.Row([
                        dbc.Col(html.H1(
                                "Welcome Back!", className="text-center my-5"
                                ),
                            width=12
                        )
                ]),

                # Sign up island
                dbc.Row([
                    html.Div([
                        # Sign up Header
                        dbc.Col(
                            html.H3("Log in", className="text-center my-4"),
                        ),
                        
                        # Email input
                        dbc.Col([
                            dbc.Label('Email', className='fw-bold'),
                            dbc.Input(type='text', placeholder='Enter your email address', style={"borderWidth": "2px", "borderColor": "grey"})
                        ]),
                        
                        # Password input
                        dbc.Col([
                            dbc.Label('Password', className='fw-bold mt-4'),
                            dbc.Input(type='text', placeholder='Enter your password', style={"borderWidth": "2px", "borderColor": "grey"}),
                            dbc.FormText('Forgot your password?', style={'textAlign': 'right'})
                        ]),

                        # Submit Button
                        dbc.Col([
                            dbc.Button('Log in', color='primary', className='my-3 fw-bold', style={'width':'450px', 'display': 'block', 'margin': 'auto'})
                        ])

                    ], style={'display': 'block', 'margin': 'auto', 'width': '65vh', 'height': '55vh', 'backgroundColor': '#d3d3d3', 'borderRadius': '20px'})
                ])
            ])
])