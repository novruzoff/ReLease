import dash
from dash import html
from dash import dcc


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://emiliakrichevsky:<>@release0.dg5ey5q.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db = client["ReLease"]
collection = db["SampleData"] 

c = collection.count_documents({})
   
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Welcome to My Dash App"),
        html.H2(c),
        dcc.Graph(
            figure={
                "data": [
                    {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "First Chart"},
                    {"x": [1, 2, 3], "y": [2, 4, 5], "type": "bar", "name": "Second Chart"},
                ],
                "layout": {"title": "Dash Data Visualization"},
            }
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
