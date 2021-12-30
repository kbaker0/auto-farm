from re import T
from dash.dcc.Slider import Slider
from dash.html.Label import Label
from dash_bootstrap_components._components.CardBody import CardBody
from dash_bootstrap_components._components.CardHeader import CardHeader
from dash_bootstrap_components._components.Row import Row
from numpy import True_
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_daq as daq
import pandas as pd
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import dash_html_components as html
import datetime
# from warnings import alert

# TODO: use req to update threshold values in rasperry pie>arduino>growth station

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions = True)


# Using the server to get values
data_url = 'http://192.168.5.220:8246/ph'
# df_receiver = pd.read_json(data_url)

# Parsing the server values

# df_receiver['new_date'] = [datetime.datetime.strptime(d, '%Y-%m-%dT%H:%M:%S.%f%z').date() for d in df_receiver['tstamp']]
# df_receiver['new_time'] = [datetime.datetime.strptime(d, '%Y-%m-%dT%H:%M:%S.%f%z').time() for d in df_receiver['tstamp']]
# available_indicators_new = df_receiver.sensor.unique()
# reading = df_receiver.sensor
# latest_values = {}

# for i in available_indicators_new:
#     latest_values[i] = df_receiver[reading == i].tail(1)
#     print(latest_values)

## Test
with open('sample_data.json') as json_file:
    df = pd.read_json(json_file)

## Test
with open('tstamp_data.json') as json_file:
    df_tstamp = pd.read_json(json_file)
    df_tstamp['new_date'] = [datetime.datetime.strptime(d, '%Y-%m-%dT%H:%M:%S.%f%z').date() for d in df_tstamp['tstamp']]
    df_tstamp['new_time'] = [datetime.datetime.strptime(d, '%Y-%m-%dT%H:%M:%S.%f%z').time() for d in df_tstamp['tstamp']]
    available_indicators = df_tstamp.sensor.unique()
    reading = df_tstamp.sensor
    latest_values = {}
    for i in available_indicators:
        latest_values[i] = df_tstamp[reading == i].tail(1)

# Tabs styling 
tabs_style= {
    # 'margin-bottom': '-1px',
    'background-color': 'none',
    'color' : 'black',
    'border':'none'
}
tabs_style_active= {
    # 'margin-bottom': '-1px',
    'background-color': 'none',
    'padding-left': '15px',
    'border-left':'3px solid royalblue',
    'color': 'black' 
}

# Setting up layout for tab 2 date picker
date_picker = html.Div([
    dcc.DatePickerSingle(
        id='my-date-picker-single',
        min_date_allowed=datetime.date(1969, 12, 31),
        max_date_allowed=datetime.date(3000, 12, 31),
        initial_visible_month=datetime.date(1970, 1, 1),
        display_format='YYYY-MM-DD',
        date=df_tstamp['new_date'][0],
        persistence=True                           
        ),
    ])

#Not used--Old graph calls
# fig = px.line(df_tstamp, x="tstamp", y=df_tstamp.reading, title='PH LEVELS')
# fig_2 = px.line(df, x="tstamp", y="temperature", title='TEMPERATURE')
# fig_3 = px.line(df, x="tstamp", y="humidity", title='HUMIDITY')
# fig_4 = px.line(df, x="tstamp", y="water_level", title='WATER LEVEL')


# Alert layout
alerts = html.Div([
        dbc.Alert([
                html.I(className="bi bi-exclamation-triangle-fill me-2"),
                "An example warning \[^-^]/"],
                color="warning",
                className="d-flex align-items-center",
            ),
        dbc.Alert([
                html.I(className="bi bi-x-octagon-fill me-2"),
                "Ope!",
            ],
            color="danger",
            className="d-flex align-items-center")
            ])
card_style = {
            #  'width':'100%',
            #  'height' : '100%',
             'margin-left' : '10px',
             'text-align' : 'center'
            }
growth_station_select = html.Div([
    html.Div(
        dbc.Select(
            id='growth-station-dropdown',
            options=[
                {'label': 'Growth Station 1', 'value': 'GS01'},
                {'label': 'Growth Station 2', 'value': 'GS02'}],
            value='GS01', 
            style={'width': '50%', 'float': 'right'}),
        )   
    ])

# available_indicators = df['ph']
# print("Available indicators: ", available_indicators)

# Temporarily setting the latest value to display below

current_ph = df['ph'][0] 
params = list(df)
max_length = len(df)

# Defining the layout
app.layout = dbc.Container(className='bg-dark mb-10', style={'padding':'10px'}, children=[
    dbc.Row([
        dbc.Col(html.H3('Farmer Hub \[^-^]/', className= 'text-white'), width=6),
        # dbc.Col(html.H3(id='gs-output-container', className= 'text-white'), width=4),
        dbc.Col(growth_station_select, width=6)]),
    # Tabs Sidebar
    html.Div([
            dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[
            dcc.Tab(label='Dashboard', value='tab-1-example-graph', style=tabs_style, selected_style=tabs_style_active),
            dcc.Tab(label='Reports', value='tab-2-example-graph', style=tabs_style, selected_style=tabs_style_active),
            dcc.Tab(label='Control Panel', value='tab-3-example-graph', style=tabs_style, selected_style=tabs_style_active),
            dcc.Tab(label='Notifications', value='tab-4-example-graph', style=tabs_style, selected_style=tabs_style_active),
            dcc.Tab(label='Beep', value='', style=tabs_style, selected_style=tabs_style_active),
            dcc.Tab(label='Boop', value='', style=tabs_style, selected_style=tabs_style_active),
            ],
        vertical = True,
        parent_style={'float': 'left', 'margin-top': '10px', 'margin-left': '0px'})
    ]),

    # Reload intervals to update dashboard
    html.Div(id='tabs-content-example-graph', style={'float' : 'left'}, className='mt-2'),
    dcc.Interval(
                id='interval-component2',
                interval=1000, # in milliseconds
                n_intervals=-1
                )],
    fluid=True
)

# Callback to update growth container selector
@app.callback(
    Output('gs-output-container', 'children'),
    Input('growth-station-dropdown', 'value')
    )
def update_output(value):
    return '{}'.format(value)

# Callback to update Graphing tab
@app.callback(
    Output('tabs-content-example-graph', 'children'),
    Input('tabs-example-graph', 'value'),
    Input('interval-component2', 'n_intervals')
    )

def render_content(tab, intervals):
    # First tab view, dashboard displaying current readings
    if tab == 'tab-1-example-graph':
        return [        
        html.Div(style={'margin-left' : '50px', 'margin-top':'30px'}, children=[
            html.H3('Dashboard', style={'margin-bottom':'30px'}),
            dbc.Row([
                dbc.Col(
                    dbc.Card([
                        dbc.CardBody([
                            html.H4('Temperature'),
                            # html.H5(datetime.datetime.now())
                            # html.H5(latest_values['temperature']['reading'].to_string(index=False), u"\N{DEGREE SIGN}")
                        ])
                    ],
                    style = card_style,
                    className='shadow p-3 mb-5 bg-body rounded'
                    )
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            html.H4('Humidity'),
                            html.H5(df['humidity'][0].round(decimals=1))
                            ]),
                        style = card_style,
                        className='shadow p-3 mb-5 bg-body rounded'
                        )
                    ),
                dbc.Col(
                    dbc.Card([
                        # dbc.CardHeader('Light Cycle'),
                        dbc.CardBody([
                            html.H4('Light Cycle'),
                            html.H5('White: on, 100%'),
                            html.H6('Time remaining: 00:10:20:30'),
                            ])
                        ],
                        style = card_style,
                        className='shadow p-3 mb-5 bg-body rounded')
                    ),
                dbc.Col(
                    dbc.Card([
                        # dbc.CardHeader('Conductivity'),
                        dbc.CardBody([
                            html.H4('Conductivity'),
                            html.H5(latest_values['electroconductivity']['reading'].to_string(index=False)) 
                        ]),
                    
                        ],
                        style = card_style,
                        className='shadow p-3 mb-5 bg-body rounded'
                        )
                    )
                ],
                className='mb-3'
            ),
            dbc.Row([
                dbc.Col(
                    dbc.Card([
                        # dbc.CardHeader('pH'),
                        dbc.CardBody([
                            html.H4('pH'),
                            html.H5(latest_values['pH']['reading'].to_string(index=False))
                            ])
                        ],
                        style = card_style,
                        className='shadow p-3 mb-5 bg-body rounded')
                        ),
                dbc.Col( 
                    dbc.Card([
                        # dbc.CardHeader('Water Level'),
                        dbc.CardBody([
                            html.H3('Water Level'),
                            html.H4(df['water_level'][0].round(decimals=1))                  
                            ]),
                        ],
                        style = card_style,
                        className='shadow p-3 mb-5 bg-body rounded'),
                    ),
                dbc.Col(
                    dbc.Card([
                        # dbc.CardHeader('Temperature'),
                        dbc.CardBody([
                            html.H3('Temperature'),
                            html.H4(latest_values['temperature']['reading'].to_string(index=False))
                        ])
                    ],
                    style = card_style,
                    className='shadow p-3 mb-5 bg-body rounded'
                        )
                    )
                ])
            ])
        ]
    # Case for Graph tab
    elif tab == 'tab-2-example-graph':
        return html.Div([
            
                # html.Div(
                    # dcc.Tabs([
                        
                    #     dcc.Tab(label='pH', children=[
                            html.Div([
                                html.H5(datetime.datetime.now()),
                                html.H3('Reports', style={'margin-bottom': '30px'}),
                                dbc.Row([
                                    dbc.Col(
                                            # dcc.Dropdown(
                                            
                                            # id='sensor-type',
                                            # options=[{'label': i, 'value': i} for i in available_indicators_new],
                                            # placeholder="Select a sensor",
                                            # value='pH',
                                            # style= {
                                            #     'color':'black',
                                            #     'width':'70%',
                                            # }
                                            # ),

                                            # Choose which graph to display as base
                                            dcc.Dropdown(
                                            
                                            id='sensor-type',
                                            options=[{'label': i, 'value': i} for i in available_indicators],
                                            placeholder="Select a sensor",
                                            value='pH',
                                            style= {
                                                'color':'black',
                                                'width':'70%',
                                            }),
                                        ),

                                # dbc.Col(date_picker),
                                    ]),
                                # dcc.Checklist(
                                #     id="checklist",
                                #     options=[{"label": x, "value": x} 
                                #             for x in available_indicators_new],
                                #     value=available_indicators_new[:0],
                                #     labelStyle={'display': 'inline-block', 'margin-left': '5px'},
                                    
                                # ),
                                # Choose the graph to add 
                                dcc.Checklist(
                                    id="checklist",
                                    options=[{"label": x, "value": x} for x in available_indicators],
                                    value=available_indicators[:0],
                                    labelStyle={'display': 'inline-block', 'margin-left': '5px'},
                                    
                                ),
                                dcc.Graph(id='ph-graph'),
                            ]),
                        # ],
                        # style=tabs_style, selected_style=tabs_style_active),
                    #     dcc.Tab(label='Temperature', children=[
                    #         # date_picker,

                    #         # dcc.Checklist(
                    #         #     id="checklist",
                    #         #     options=[{"label": x, "value": x} 
                    #         #             for x in params],
                    #         #     value=params[:0],
                    #         #     labelStyle={'display': 'inline-block'}
                    #         # ),


                    #         dcc.Graph(id="line-chart", figure=fig_2)
                    #     ],style=tabs_style, selected_style=tabs_style_active),
                    #     dcc.Tab(label='Humidity', children=[
                    #         # date_picker,
                    #         dcc.Graph(figure=fig_3)
                    #     ],style=tabs_style, selected_style=tabs_style_active),
                    #     dcc.Tab(label='Water Level', children=[
                    #         # date_picker,
                    #         dcc.Graph(figure=fig_4)
                    #     ],style=tabs_style, selected_style=tabs_style_active),
                    #     # dcc.Tab(label='Light Cycle', children=[
                    #     #     dcc.Graph(figure=fig_5)
                    #     # ]),
                    #   ],
                    

                    
                   
                # ),
              
            #  ),
            
            
         ],
        style={'width':'950px', 'margin-left':'50px', 'margin-top':'30px'})

    # Tab for updating the settings--limited to temp, lights
    elif tab == 'tab-3-example-graph':
        return html.Div([
                html.H3('Settings', style={'margin-bottom': '30px'}),
                dbc.Row([
                    dbc.Col(
                        dbc.Card(
                            dbc.CardBody([
                                html.H4('Temperature'),
                                    daq.NumericInput(
                                        id='my-temperature-input-1',
                                        value=df['temperature'][0].round(decimals=1),
                                        size=100
                                        )
                                    ]),
                                style=card_style,
                                className='shadow p-3 mb-5 bg-body rounded'
                            ),
                        ),
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H4('Humidity'),
                        daq.NumericInput(
                            id='my-temperature-input-1',
                            value=df['humidity'][0].round(decimals=1),
                            size=100
                        ),
                        ]),
                        style=card_style,
                        className='shadow p-3 mb-5 bg-body rounded'
                    )
                ),
                    
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H4('Light Cycle'),
                    dbc.Row([
                        dbc.Col(daq.BooleanSwitch(
                            id='my-boolean-switch-red', 
                            on=False,
                            label="Red",
                            labelPosition="bottom",
                        )),
                    dbc.Col(
                        daq.BooleanSwitch(
                            id='my-boolean-switch-blue', 
                            on=False,
                            label="Blue",
                            labelPosition="bottom"
                        )),
                            
                        dbc.Col(
                            daq.BooleanSwitch(
                                id='my-boolean-switch-white', 
                                on=True,
                                label="White",
                                labelPosition="bottom"
                                )                    
                            )
                        ])
                    ])  
                ],
            style=card_style,
            className='shadow p-3 mb-5 bg-body rounded'
            )   
            ),
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H4('Electroconductivity'),
                        daq.NumericInput(
                        id='my-temperature-input-1',
                        value=df['humidity'][0].round(decimals=1),
                        size=100
                        )
                    ])
                ],
                style=card_style,
                className='shadow p-3 mb-5 bg-body rounded')
                )
            ])     
        ],
        style={'margin-left' : '50px', 'margin-top':'30px'}
        )

    elif tab == 'tab-4-example-graph':
        return html.Div(style={'margin-left' : '50px', 'margin-top':'30px'},children=[
            alerts
        ])
    
@app.callback(
    Output('ph-graph', 'figure'),
    # Input('my-date-picker-single', 'date'),
    Input('sensor-type', 'value')
    # Input('checklist', 'value')
    )

# Test update graph with server data--only reading ph
# def update_graph(my_date_picker, sensor_type, checklist_value):
    
    # input_date = datetime.datetime.strptime(my_date_picker, '%Y-%m-%d').date()
    # print(input_date)
    # print(df_receiver)
    # dff = df_receiver[df_receiver['sensor'] == sensor_type][df_receiver.new_date == input_date]
    # # mask = df_tstamp.sensor.isin(checklist_value)
    # print(dff)
    # fig = px.line(dff, x=dff['new_time'], y=dff['reading'], title=str(sensor_type + " readings for " + my_date_picker), markers=True,)

    # return fig

# Update graph with server data--only reading ph
def update_graph(sensor_type):
    # input_date = datetime.datetime.strptime(my_date_picker, '%Y-%m-%d').date()
    dff = df_receiver[df_receiver['sensor'] == 'pH'][df_receiver.new_date == '1970-01-01']
    print("dff: ", df_receiver['new_time'], df_receiver['reading'])
    fig = px.line(df_receiver, x=df_receiver['new_time'], y=df_receiver['reading'], title=str(sensor_type), markers=True,)
    return fig
        
def update_output(on):
    return 'The switch is {}.'.format(on)
    
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)