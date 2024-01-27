import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

card = dbc.Card(
    [
        dbc.CardImg(src="/assets/placeholder286x180.png", top=True),  # Make sure the image path is correct
        dbc.CardBody(
            [
                html.H4("Title", className="card-title"),
                html.P(
                    "Description",
                    className="card-text",
                ),
                dbc.Button("See more", color="primary"),
            ]
        ),
    ],
    style={"width": "16rem", 'margin-left': '10px'},
)

# Define the app layout
app.layout = html.Div([
    # Top bar with Login and Sign Up
    html.Div([
        html.Div([
            # Other header content can go here
        ], className='header-left'),
        html.Div([
            dcc.Link('Login', href='/login', className='login-link', style={
            'margin-right': '20px',
            'padding': '10px 20px',  # Adjust padding to control the size
            'background-color': '#f2f2f2',  # Match the catalog item background color
            'border-radius': '5px',  # Match the catalog item border radius
            'text-decoration': 'none',  # Remove underline from link
            'color': 'black',  # Set the text color
            'box-shadow': '0 0 5px rgba(0,0,0,0.1)'  # Optional: add shadow for depth
        }),
            dcc.Link('Sign Up', href='/signup', className='signup-link', style={
            'margin-right': '20px',
            'padding': '10px 20px',  # Adjust padding to control the size
            'background-color': '#f2f2f2',  # Match the catalog item background color
            'border-radius': '5px',  # Match the catalog item border radius
            'text-decoration': 'none',  # Remove underline from link
            'color': 'black',  # Set the text color
            'box-shadow': '0 0 5px rgba(0,0,0,0.1)'  # Optional: add shadow for depth
        }),
        ], className='header-right', style={'position': 'absolute', 'top': 0, 'right': 0, 'padding': '10px', 'background-color': 'white'})
    ], className='top-bar', style={'overflow': 'hidden'}),
    
    # Main content section
    html.Div([
        html.Div([
            html.H2("Apartments for you", className='content-title'),
            html.Div(id='catalog-items', className='catalog-container')
            # ... [rest of your catalog code] ...
        ], className='catalog-section'),
        html.Div([
            html.H2("Filters", className='filter-title'),
            dcc.Dropdown(
                id='room-dropdown', 
                options=[
                    {'label': 'Studio', 'value': '1'},
                    {'label': '1 Bedroom', 'value': '2'},
                    {'label': '2 Bedrooms', 'value': '3'},
                    {'label': '3 Bedrooms', 'value': '4'},
                    # ... [rest of your options] ...
                ], 
                placeholder="Type of apartment",
                className='filter-dropdown',
                style={'height': '30px', 'width': '200px'}),
            # ... [rest of your filter code] ...
        ], className='filter-section'),
    ], className='main-content'),
],className='main-content', style={'margin-top': '100px'})


# Define callback to populate catalog items
@app.callback(
    Output('catalog-items', 'children'),
    [Input('room-dropdown', 'value')]
)

def update_catalog(selected_rooms):
    # Here you should fetch the actual listings from a database or service.
    # This function returns placeholder elements for demonstration.
    # You would replace this with your actual data retrieval and processing.
    return [
        html.Div([
            card  # Add the card to the layout
        ], className='card-container')
        for _ in range(10)  # Replace with actual number of listings
    ]

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
