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

layout = html.Div([
        dbc.Container(
            fluid=True,
            children=[
                # Header
                dbc.Row([
                        dbc.Col(
                            html.H1(
                                "Create Your Listing", className="text-center my-5"
                            ),
                            width=12,
                        )
                    ]),
                
                # Image row section
                dbc.Row([
                        
                        # Image upload column
                        dbc.Col(html.Div([
                                    dcc.Upload(
                                        id="upload-image",
                                        children=html.Div([
                                                "Drag and Drop or ",
                                                html.A("Select Files", className='fw-bold'),
                                            ]),
                                        style={
                                            "width": "100%",
                                            "padding": "auto",
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
                                ]),
                            width=4
                        ),
                        
                        # Listing information column
                        dbc.Col(
                            html.Div([
                                    # Listing title input
                                    dbc.Label("Listing Title", className='mb-3 fw-bold'),
                                    dbc.Input(
                                        type="text",
                                        style={
                                            "borderWidth": "2px",
                                            "borderColor": "grey",
                                        },
                                        placeholder="Enter listing title"
                                    ),
                                    
                                    # Rent price input
                                    dbc.Label("Rent Price", className='mb-3 mt-3 fw-bold'),
                                    dbc.Input(
                                        type="number",
                                        style={
                                            "borderWidth": "2px",
                                            "borderColor": "grey",
                                        },
                                        placeholder="$"
                                    ),
                                    
                                    # Address input
                                    dbc.Label("Address", className='mb-3 mt-3 fw-bold'),
                                    dbc.Input(
                                        type="text",
                                        style={
                                            "borderWidth": "2px",
                                            "borderColor": "grey",
                                        },
                                        placeholder='Enter your address'
                                    ),
                                    
                                    # Transfer date input
                                    dbc.Label("Transfer Date", className='d-inline-flex mr-4 mt-4 fw-bold'),
                                    dcc.DatePickerSingle(
                                        id="my-date-picker-single",
                                        min_date_allowed=date(2024, 1, 1),
                                        max_date_allowed=date(2050, 9, 19),
                                        initial_visible_month=date(2024, 1, 28),
                                        date=date(2024, 1, 28),
                                        className="d-inline-flex m-4",
                                    ),
                                    
                                    # Lease end date input
                                    dbc.Label("Lease End Date", className='d-inline-flex mr-4 mt-4 ml-6 fw-bold'),
                                    dcc.DatePickerSingle(
                                        id="my-date-picker-single",
                                        min_date_allowed=date(2024, 1, 1),
                                        max_date_allowed=date(2050, 9, 19),
                                        initial_visible_month=date(2024, 1, 28),
                                        date=date(2024, 1, 28),
                                        className="d-inline-flex m-4",
                                    ),
                                ], style={'marginLeft': '10px'})
                        )
                    ]),
                
                # Decription row section
                dbc.Row([
                        dbc.Col(html.Div([
                                    dbc.Label('Description'),
                                    dbc.Textarea(
                                        placeholder="Briefly describe your listing",
                                        style={'height': '200px',
                                               'borderWidth': '2px',
                                                'borderColor': 'grey'
                                               }

                                    )
                                ], style={'marginLeft': '10px', 'marginTop': '10px'})
                        )
                ]),

                # Contact information row section
                dbc.Row([
                        dbc.Col(html.Div([
                                    dbc.Label('Contact Information'),
                                    dbc.Textarea(
                                        placeholder="Enter contact information",
                                        style={'height': '75px',
                                               'borderWidth': '2px',
                                                'borderColor': 'grey'
                                               }

                                    )
                                ], style={'marginLeft': '10px', 'marginTop': '10px'})
                        )
                ]),
                
                # Submit button
                dbc.Row([
                    dbc.Col(html.Div([
                        dbc.Button('Post Listing', color='primary', className='mt-4 mb-5 fw-bold fs-60')
                    ], className='d-grid'))
                ])
        ])
])