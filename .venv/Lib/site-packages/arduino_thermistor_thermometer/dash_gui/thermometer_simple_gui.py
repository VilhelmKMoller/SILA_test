from dash import Dash, html, dcc, Input, Output, callback
import dash_daq as daq

from sila2.client import SilaClient

app = Dash(__name__)

theme = {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#FF6600',
    'backgroundColor' : '#303030'
}

rootLayout = html.Div([
   
    daq.LEDDisplay(
        id='temp-led-display-current',
        value="3.14",
        color=theme['primary'],
        className='dark-theme-control',
        size=80
    ),
    daq.LEDDisplay(
        id='temp-led-display-set',
        value="3.14159",
        color=theme['primary'],
        className='dark-theme-control',
        size=40
    ),
     daq.LEDDisplay(
        id='light-led-display-current',
        value="3.14",
        color=theme['secondary'],
        className='dark-theme-control',
        size=80
    ),
    dcc.Slider(
        id='thermometer-slider',
        value=1.0,
        min=0,
        max=100.0,
    ),
    dcc.Interval(
            id='interval-component',
            interval=2*1000, # in milliseconds
            n_intervals=0
        )
])

app.layout = html.Div([
    html.Div(id='dark-theme-components', children=[
        daq.DarkThemeProvider(theme=theme, children=rootLayout)
    ], style={
        'border': 'solid 1px #A2B1C6',
        'border-radius': '5px',
        'padding': '50px',
        'marginTop': '20px',
        'backgroundColor':'#303030'
    })
], style={'padding': '50px'})


@callback(
    Output('temp-led-display-set', 'value'),
    Input('thermometer-slider', 'value')
)
def update_(value):
    return value

@callback(
    Output('temp-led-display-current', 'value'),
    Input('interval-component', 'n_intervals')
)
def update_thermometer(n):
    temperature =  thermometer_client.TemperatureController.CurrentTemperature.get()

    return float(f"{temperature:.2f}")

@callback(
    Output('light-led-display-current', 'value'),
    Input('interval-component', 'n_intervals')
)
def update_lightintensity(n):
    light_intensity =  thermometer_client.LightIntensityController.CurrentLightIntensity.get()

    return float(f"{light_intensity:.2f}")


if __name__ == '__main__':
    hostname = "127.0.0.1"
    thermometer_client = SilaClient(hostname, 50052, insecure=True)
    
    app.run(debug=True)