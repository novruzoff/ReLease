import dash
import dash_bootstrap_components as dbc
import dash_extensions as de

URL = "https://lottie.host/bf4a2e06-a24d-4c12-b635-6cc73074f211/YD7GpocDk0.json"

options = dict(loop=True, autoplay=True)

dash.register_page(__name__, path="/404", title="Not Found")


layout = dbc.Container(
    [
        de.Lottie(
            url=URL,
            options=options,
            isClickToPauseDisabled=True,
            width="700px",
        )
    ],
    style={
        "display": "flex",
        "justify-content": "center",
        "align-items": "center",
        "height": "100vh",
    },
)
