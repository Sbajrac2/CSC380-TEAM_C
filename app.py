import dash
import dash_mantine_components as dmc
from dash import Dash, html, dcc, ctx, callback, Output, Input, State
import plotly.express as px
import plotly.io as pio
import pandas as pd
from data2 import Data
from predict import Predict
import numpy as np
from collections import deque
import random
from datetime import datetime, timedelta, date
import time
from typing import Dict
from typing import List
import matplotlib.pyplot as plt
import plotly.graph_objs as go

# queue to implement new tabs
tabsname = deque()
grapharray = deque()

# creating main data object
maindataobject = Data()

# asking for input file
maindataobject.askforinputfile()
# alldata = "sa"
# getting all of the data
alldata = maindataobject.read_file()
starttime, endtime = maindataobject.getstartandenddate()

timeHours = [
    "6 AM",
    "7 AM",
    "8 AM",
    "9 AM",
    "10 AM",
    "11 AM",
    "12 PM",
    "1 PM",
    "2 PM",
    "3 PM",
    "4 PM",
    "5 PM",
    "6 PM",
    "7 PM",
    "8 PM",
    "9 PM",
    "10 PM",
    "11 PM",
]
dropLowerThan = [
    "0 Seconds",
    "5 Seconds",
    "10 Seconds",
    "15 Seconds",
    "20 Seconds",
    "25 Seconds",
    "30 Seconds",
    "35 Seconds",
    "40 Seconds",
    "45 Seconds",
    "50 Seconds",
    "55 Seconds",
    "60 Seconds",
]

dropHigherThan = ["1 hr", "30 min", "15 min", "10 min", "5 min"]

# error_messages = dcc.Store(id='error-messages', storage_type='memory'),
# interval = dcc.Interval(id='error-interval', interval=1000, n_intervals=0),
# error_container = html.Div(id='error-container', style={'display': 'none'}),


app = Dash(__name__)
app.layout = html.Div(
    # main div
    # ===============================main div starts==============================================
    [
        # headingdiv starts
        html.Div(
            [
                html.Button(
                    "About Us",
                    id="open-popup-button",
                    n_clicks=0,
                    style={
                        "cursor": "pointer",
                        "position": "fixed",
                        "background-color": "#f2f2f2",
                        "padding": "10px",
                        "border": "1px solid gray",
                        "border-radius": "10px",
                        "box-shadow": "2px 2px 5px gray",
                        "top": "80px",
                        "left": "70px",
                        "transform": "translate(-50%, -50%)",
                        "z-index": "1000",
                    },
                ),
                html.Div(id="popup-container"),
            ]
        ),
        html.Div(
            # heading text
            [
                dmc.Image(
                    src="./assets/moditlogo.png",
                    alt="logo",
                    width="7rem",
                    className="logo",
                ),
                dmc.Text("MODIT 2.0", align="center", className="headingtext"),
            ],
            className="headingdiv",
        ),
        # heading div ends
        html.Div(
            [
                # machine layout starts
                html.Div(
                    [
                        # dmc.Text("SELECT MACHINES OR LINES", className="machinelayouttext"),
                        html.Div(
                            [
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st71checkbox",
                                            checked=True,
                                        ),
                                        dmc.Text(
                                            "ST71",
                                            className="station71name commonmachinename",
                                        ),
                                    ],
                                    className="machine71 commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st72checkbox",
                                        ),
                                        dmc.Text(
                                            "ST72",
                                            className="station72name commonmachinename",
                                        ),
                                    ],
                                    className="machine72 commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st80checkbox",
                                        ),
                                        dmc.Text(
                                            "ST80",
                                            className="station80name commonmachinename",
                                        ),
                                    ],
                                    className="machine80 commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st90checkbox",
                                        ),
                                        dmc.Text(
                                            "ST90",
                                            className="station90name commonmachinename",
                                        ),
                                    ],
                                    className="machine90 commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st91checkbox",
                                        ),
                                        dmc.Text(
                                            "ST91",
                                            className="station91name commonmachinename",
                                        ),
                                    ],
                                    className="machine91 commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st92checkbox",
                                        ),
                                        dmc.Text(
                                            "ST92",
                                            className="station92name commonmachinename",
                                        ),
                                    ],
                                    className="machine92 commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st100checkbox",
                                        ),
                                        dmc.Text(
                                            "ST100",
                                            className="station100name commonmachinename",
                                        ),
                                    ],
                                    className="machine100 commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st110checkbox",
                                        ),
                                        dmc.Text(
                                            "ST110",
                                            className="station110name commonmachinename",
                                        ),
                                    ],
                                    className="machine110 commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st120checkbox",
                                        ),
                                        dmc.Text(
                                            "ST120",
                                            className="station120name commonmachinename",
                                        ),
                                    ],
                                    className="machine120 commonmachineproperties lastline3machine",
                                ),
                            ],
                            className="line3",
                        ),
                        # ========================================
                        # =====================================================
                        html.Div(
                            [
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st60bcheckbox",
                                        ),
                                        dmc.Text(
                                            "ST60B",
                                            className="station60bname commonmachinename",
                                        ),
                                    ],
                                    className="machine6b commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st50bcheckbox",
                                        ),
                                        dmc.Text(
                                            "ST50B",
                                            className="station50bname commonmachinename",
                                        ),
                                    ],
                                    className="machine5b commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st40bcheckbox",
                                        ),
                                        dmc.Text(
                                            "ST40B",
                                            className="station40bname commonmachinename",
                                        ),
                                    ],
                                    className="machine4b commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st30bcheckbox",
                                        ),
                                        dmc.Text(
                                            "ST30B",
                                            className="station30bname commonmachinename",
                                        ),
                                    ],
                                    className="machine3b commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st20bcheckbox",
                                        ),
                                        dmc.Text(
                                            "ST20B",
                                            className="station20bname commonmachinename",
                                        ),
                                    ],
                                    className="machine2b commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st10bcheckbox",
                                        ),
                                        dmc.Text(
                                            "ST10B",
                                            className="station10bname commonmachinename",
                                        ),
                                    ],
                                    className="machine1b commonmachineproperties",
                                ),
                            ],
                            className="line2",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st60acheckbox",
                                        ),
                                        dmc.Text(
                                            "ST60A",
                                            className="station60aname commonmachinename",
                                        ),
                                    ],
                                    className="machine60a commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st50acheckbox",
                                        ),
                                        dmc.Text(
                                            "ST50A",
                                            className="station50aname commonmachinename",
                                        ),
                                    ],
                                    className="machine50a commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st40acheckbox",
                                        ),
                                        dmc.Text(
                                            "ST40A",
                                            className="station40aname commonmachinename",
                                        ),
                                    ],
                                    className="machine40a commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st30acheckbox",
                                        ),
                                        dmc.Text(
                                            "ST30A",
                                            className="station30aname commonmachinename",
                                        ),
                                    ],
                                    className="machine30a commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st20acheckbox",
                                        ),
                                        dmc.Text(
                                            "ST20A",
                                            className="station20aname commonmachinename",
                                        ),
                                    ],
                                    className="machine20a commonmachineproperties",
                                ),
                                html.Div(
                                    children=[
                                        dmc.Checkbox(
                                            className="checkbox",
                                            size="5rem",
                                            id="st10acheckbox",
                                        ),
                                        dmc.Text(
                                            "ST10A",
                                            className="station10aname commonmachinename",
                                        ),
                                    ],
                                    className="machine10a commonmachineproperties",
                                ),
                            ],
                            className="line1",
                        ),
                    ],
                    className="machinelayoutdiv",
                ),
                # machine layout ends
                # filterlayout starts
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    children=[
                                        html.Div("Select Date"),
                                        dcc.DatePickerRange(
                                            id="date-filter",
                                            month_format="MMM Do, YYYY",
                                            end_date_placeholder_text="MMM Do, YYYY",
                                            start_date=starttime,
                                            minimum_nights=0,
                                            max_date_allowed="",
                                            end_date=starttime,
                                            #     clearable=True,
                                            #     with_portal=True,
                                            #     start_date=date(2017, 6, 21)
                                        ),
                                    ],
                                    className="datemaindiv",
                                ),
                                html.Div(
                                    children=[
                                        html.Div("Start Time"),
                                        dcc.Dropdown(
                                            id="time-start-filter",
                                            style={"width": "120px"},
                                            # dmc.Timeline(),
                                            options=[
                                                {"label": timestart, "value": timestart}
                                                for timestart in timeHours
                                            ],
                                            value="7 AM",
                                        ),
                                    ],
                                    className="startimemaindiv",
                                ),
                                html.Div(
                                    children=[
                                        html.Div("End Time"),
                                        dcc.Dropdown(
                                            id="time-end-filter",
                                            style={"width": "120px"},
                                            options=[
                                                {"label": timeend, "value": timeend}
                                                for timeend in timeHours
                                            ],
                                            value="5 PM",
                                        ),
                                    ],
                                    className="endtimemaindiv",
                                ),
                            ],
                            className="dateandtimemaindiv",
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        html.Div("Throughput Interval"),
                                        dmc.NumberInput(
                                            value=0.1,
                                            precision=2,
                                            min=0.1,
                                            step=0.2,
                                            max=10,
                                            id="throughput_intervals_filter",
                                        ),
                                    ],
                                    className="throughput_interval_main_div",
                                ),
                                html.Div(
                                    children=[
                                        html.Div("Graph Content"),
                                        dcc.Dropdown(
                                            id="graph-content-filter",
                                            options=[
                                                {
                                                    "label": "Cycle Count",
                                                    "value": "Cycle Count",
                                                },
                                                {
                                                    "label": "Rate of Productivity",
                                                    "value": "Rate of Productivity",
                                                },
                                                {
                                                    "label": "Status Code Durations",
                                                    "value": "Code Durations",
                                                },
                                            ],
                                            value="Rate of Productivity",
                                        ),
                                    ],
                                    className="graphcontentmaindiv",
                                ),
                            ],
                            className="throughputandgraphmaindiv",
                        ),
                        # dcc.Dropdown(
                        #     style={"margin-right": "50px"},
                        #     id="throughput_intervals-filter",
                        #     options=[
                        #         {"label": hours, "value": hours}
                        #         for hours in throughput_intervals
                        #     ],
                        #     value='option1'
                        # ),
                        html.Div(
                            children=[
                                html.Div(
                                    children=[
                                        # Layout of the Drop Values Less Than filter
                                        html.Div(
                                            children="Drop Values Lower Than",
                                            className="menu-title",
                                        ),
                                        dcc.Dropdown(
                                            id="lower-end-filter",
                                            options=[
                                                {"label": droplower, "value": droplower}
                                                for droplower in dropLowerThan
                                            ],
                                            value="0 Seconds",
                                            clearable=False,
                                            className="dropdown",
                                        ),
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        # Layout of the Drop Values Greater Than filter
                                        html.Div(
                                            children="Drop Values Higher Than",
                                            className="menu-title",
                                        ),
                                        dcc.Dropdown(
                                            id="higher-end-filter",
                                            options=[
                                                {
                                                    "label": drophigher,
                                                    "value": drophigher,
                                                }
                                                for drophigher in dropHigherThan
                                            ],
                                            value="1 hr",
                                            clearable=False,
                                            className="dropdown",
                                        ),
                                    ]
                                ),
                            ],
                            className="dropvaluesmaindiv",
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        dmc.Image(
                                            src="./assets/bargraph.png",
                                            id="bargraphimg",
                                            alt="superman",
                                            caption="BAR CHART",
                                            width=100,
                                            className="bargraph commonimageproperty",
                                        ),
                                        dmc.Checkbox(
                                            size="sm",
                                            className="graphcheckbox",
                                            color="red",
                                            id="bargraph",
                                        ),
                                    ],
                                    className="singlegraphdiv",
                                ),
                                html.Div(
                                    [
                                        dmc.Image(
                                            src="./assets/h2.png",
                                            id="histogramimg",
                                            alt="superman",
                                            caption="HISTOGRAM",
                                            width=100,
                                            className="bargraph commonimageproperty",
                                        ),
                                        dmc.Checkbox(
                                            size="sm",
                                            className="graphcheckbox",
                                            color="red",
                                            id="histogram",
                                        ),
                                    ],
                                    className="singlegraphdiv",
                                ),
                                html.Div(
                                    [
                                        dmc.Image(
                                            src="./assets/l2.png",
                                            alt="linegraph",
                                            caption="LINE GRAPH",
                                            width=100,
                                            className="bargraph commonimageproperty",
                                        ),
                                        dmc.Checkbox(
                                            size="sm",
                                            className="graphcheckbox",
                                            color="red",
                                            id="linegraph",
                                            checked=True,
                                        ),
                                    ],
                                    className="singlegraphdiv",
                                ),
                            ],
                            className="differentgraphs",
                        ),
                        html.Div(
                            [
                                dmc.Button(
                                    "GRAPH",
                                    id="graphbutton",
                                    variant="gradient",
                                    size="xl",
                                    gradient={"from": "darkblue", "to": "blue"},
                                ),
                                dmc.Button(
                                    "PREDICT",
                                    id="predictbutton",
                                    variant="gradient",
                                    size="xl",
                                    gradient={"from": "darkred", "to": "red"},
                                ),
                                dmc.Button(
                                    "RESET TABS",
                                    id="deleteall",
                                    variant="gradient",
                                    size="xl",
                                    gradient={"from": "black", "to": "grey"},
                                ),
                                dmc.Button(
                                    "DELETE LAST TAB",
                                    id="deletelast",
                                    variant="gradient",
                                    size="xl",
                                    gradient={"from": "darkgreen", "to": "green"},
                                ),
                                dcc.Store(id='last-clicked-button', data=None),
                                dcc.Loading(id="loading-graph", children=[html.Div(id="graph-output")]),
                            ],
                            className="mainbuttondiv",
                        ),
                    ],
                    className="filtermaindiv",
                ),
                # html.Button('Apply Preset Filters', id='preset-filter-button')
            ],
            className="filterandmachinesdiv",
        ),
        html.Div(
            id="error_message",
            style={"color": "red", "margin-top": "40px", "font-size": "30px"},
        ),
        dmc.Tabs(
            [
                dmc.TabsList([dmc.Tab(x, value=x) for x in tabsname]),
                *[
                    dmc.TabsPanel(
                        dcc.Graph(figure=grapharray[a], style={"height": "80vh"}),
                        value=tabsname[a],
                    )
                    # dmc.TabsPanel(tabsname[a], value=tabsname[a])
                    for a in range(len(grapharray))
                ],
            ],
            color="red",
            orientation="horizontal",
            id="tabs",
            className="tabsmaindiv",
        ),
    ]
    # ==========================================main div ends=================================================
    ,
    # classname of main div
    className="maindiv",
)


# Callback to store the last clicked button
@app.callback(
    Output('last-clicked-button', 'data'),
    [Input('graphbutton', 'n_clicks'),
     Input('predictbutton', 'n_clicks')],
)
def store_last_clicked_button(graph_clicks, predict_clicks):
    if graph_clicks:
        return 'graph'
    elif predict_clicks:
        return 'predict'
    else:
        return None


# Callback to generate graph or prediction
@app.callback(
    [
        Output("loading-graph", "children"),

    ],
    [
        Input("last-clicked-button", "data"),
    ],
)
def generate_graph_or_predict(last_clicked_button):
    if last_clicked_button is None:
        raise dash.exceptions.PreventUpdate

    loading_output = None

    if last_clicked_button == "graph":
        loading_output = "Graph Generated"

        # Call the function to generate the graph
        time.sleep(.5)  # Simulate graph generation delay
        # Replace this with your graph generation logic
        # graph_output = update_graph()
        # graph_output = create_graph()
    elif last_clicked_button == "predict":
        loading_output = "Prediction Processed"
        # Call the function to process prediction
        time.sleep(10)  # Simulate prediction processing delay
        # Replace this with your prediction logic
        # prediction_output = process_prediction()

    return loading_output


# @app.callback(
#     Output('error-message', 'children'),
#     Input('error-messages', 'data'),
#     prevent_initial_call=True
# )
# def update_error_message(error_messages):
#     error_message = html.Div(id='error-message-container')
#     for error in error_messages:
#         error_message.children.append(html.P(error, style={'color': 'red'}))
#     return error_message
@callback(
    Output("error_message", "children"),
    Input(component_id="graphbutton", component_property="n_clicks"),
    Input(component_id="predictbutton", component_property="n_clicks"),
    Input(component_id="linegraph", component_property="checked"),
    Input(component_id="bargraph", component_property="checked"),
    Input(component_id="histogram", component_property="checked"),
    Input(component_id="st71checkbox", component_property="checked"),
    Input(component_id="st72checkbox", component_property="checked"),
    Input(component_id="st80checkbox", component_property="checked"),
    Input(component_id="st90checkbox", component_property="checked"),
    Input(component_id="st91checkbox", component_property="checked"),
    Input(component_id="st92checkbox", component_property="checked"),
    Input(component_id="st100checkbox", component_property="checked"),
    Input(component_id="st110checkbox", component_property="checked"),
    Input(component_id="st120checkbox", component_property="checked"),
    Input(component_id="st60acheckbox", component_property="checked"),
    Input(component_id="st50acheckbox", component_property="checked"),
    Input(component_id="st40acheckbox", component_property="checked"),
    Input(component_id="st30acheckbox", component_property="checked"),
    Input(component_id="st20acheckbox", component_property="checked"),
    Input(component_id="st10acheckbox", component_property="checked"),
    Input(component_id="st60bcheckbox", component_property="checked"),
    Input(component_id="st50bcheckbox", component_property="checked"),
    Input(component_id="st40bcheckbox", component_property="checked"),
    Input(component_id="st30bcheckbox", component_property="checked"),
    Input(component_id="st20bcheckbox", component_property="checked"),
    Input(component_id="st10bcheckbox", component_property="checked"),
    Input(component_id="time-start-filter", component_property="value"),
    Input(component_id="time-end-filter", component_property="value"),
    Input(component_id="throughput_intervals_filter", component_property="value"),
    Input(component_id="date-filter", component_property="start_date"),
    Input(component_id="date-filter", component_property="end_date"),
    Input(component_id="graph-content-filter", component_property="value"),
    Input(component_id="lower-end-filter", component_property="value"),
    Input(component_id="higher-end-filter", component_property="value"),
)
def check_value(*args):
    global start, end
    error_messages = ""
    differentgraphs = args[2:5]

    checked_values = args[5:26]  # Extracting checked values from args

    interval_throughput = args[28]
    # startDateFormat = args[29][0]
    # startDate = str(startDateFormat)
    # endDateFormat = args[29][1]
    # endDate = str(endDateFormat)
    startDate = args[29]
    endDate = args[30]
    content = args[31]
    lowerBound = args[32]

    upperBound = args[33]

    # Extract the IDs of the checked checkboxes
    starttime = args[26]
    endtime = args[27]

    # Create a dictionary to store checked checkboxes and their values

    # Check if only 1 day is selected and start time is not more than end time

    # Check if selected date is not in the input file
    # for name in sheet_names:
    #     if startDate not in dfs[name][0] or endDate not in dfs[name][0]:
    #         error_messages.append(f'Selected date range is not available in the input file for {name}.')

    # Check if some filters are not chosen
    # if differentgraphs == (None, None, None):
    #     error_messages.append("Graphs not selected\n")
    i = 0
    aop = True
    for y in differentgraphs:
        if y is True:
            aop = False
            i += 1
    if aop is True:
        error_messages = error_messages + "Graphs not selected!    "
    elif i > 1:
        error_messages = error_messages + "Please select only one graph"
    asp = True
    for x in checked_values:
        if x is True:
            asp = False
    if asp is True:
        error_messages = error_messages + "Machine not selected!    "

    if str(starttime) == "option1" or str(starttime) == "None":
        error_messages = error_messages + "Start time must be selected!    "
    else:
        start, am_pm1 = args[26].split()
        if (start != "12") and (am_pm1 == "PM"):
            start = str(int(start) + 12)
        else:
            start = str(start)

    if str(endtime) == "option1" or str(endtime) == "None":
        error_messages = error_messages + "End time must be selected!   "
    else:
        end, am_pm2 = args[27].split()
        if (end != "12") and (am_pm2 == "PM"):
            end = str(int(end) + 12)
        else:
            end = str(end)
    if str(content) == "option1" or str(content) == "None":
        error_messages = error_messages + "Select Graph Content!    "

    if str(startDate) == str(endDate):
        if int(start) > int(end):
            error_messages = error_messages + ("Start date must be before end date")
    print(differentgraphs, startDate, endDate, starttime, endtime, content)
    print(error_messages)
    return error_messages


@app.callback(
    [Output(component_id="bargraph", component_property="checked"),
     Output(component_id="histogram", component_property="checked"),
     Output(component_id="bargraph", component_property="disabled"),
     Output(component_id="histogram", component_property="disabled"),
     Output(component_id="bargraphimg", component_property="opacity"),
     Output(component_id="bargraphimg", component_property="src"),
     Output(component_id="histogramimg", component_property="opacity"),
     Output(component_id="histogramimg", component_property="src")],
    Input(component_id="graph-content-filter", component_property="value"),
)
def suggest_graph_type(value):
    if (value == "Cycle Count"):
        return False, False, False, False, 1, "./assets/bargraphhighlight.png", 1, "./assets/h2highlight.png"
    else:
        return False, False, True, True, 0.4, "./assets/bargraph.png", 0.4, "./assets/h2.png"


# Callback to toggle popup content visibility
@app.callback(
    Output("popup-container", "children"),
    [Input("open-popup-button", "n_clicks")],
    [State("popup-container", "children")],
)
def toggle_popup(n_clicks, popup_content):
    if n_clicks % 2 == 1:
        # Display the popup content
        popup_content = html.Div(
            [
                html.Div(
                    html.Button(
                        "X",
                        id="close-popup-button",
                        n_clicks=0,
                        style={
                            "cursor": "pointer",
                            "font-size": "20px",
                            "color": "#707070",
                            "border": "none",
                            "background": "none",
                            "outline": "none",
                            "position": "absolute",
                            "top": "10px",
                            "right": "10px",
                        },
                    ),
                    style={"position": "relative"},

                ),
                html.H5(
                    "Our Story", style={"font-size": "30px", "font-weight": "bold"}
                ),
                html.P(
                    [
                        "As a team of college students, we have developed a predictive analytics tool that graphs and forecasts data trends to help our stakeholders make informed decisions and explore the possibilities hidden within the data. Explore our program to unlock new insights, visualize data like never before, and unleash the potential of predictive analytics!",
                        html.Hr(),
                        html.H6(
                            "Meet Our Team",
                            style={"font-size": "30px", "font-weight": "bold"},
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Span("Luke Murphy"),
                                        html.Br(),
                                        html.Span("lukemurphy472@gmail.com"),
                                        html.Br(),
                                        # html.A("Luke's LinkedIn Profile", href="https://www.linkedin.com/in/luke", target="_blank"),
                                        html.Span("LinkedIn TBA"),
                                    ],
                                    style={
                                        "display": "inline-block",
                                        "margin-right": "20px",
                                        "margin-bottom": "20px",
                                    },
                                ),
                                html.Div(
                                    [
                                        html.Span("Nidhi Patel"),
                                        html.Br(),
                                        html.Span("nidhi.patel.2326@gmail.com"),
                                        html.Br(),
                                        html.A("Nidhi's LinkedIn Profile",
                                               href="https://www.linkedin.com/in/nidhi-patel-854540220/",
                                               target="_blank"),
                                        # html.Span("https://www.linkedin.com/in/nidhi-patel-854540220/"),
                                    ],
                                    style={
                                        "display": "inline-block",
                                        "margin-right": "20px",
                                        "margin-bottom": "20px",
                                    },
                                ),
                                html.Div(
                                    [
                                        html.Span("Praneeta Pradhan"),
                                        html.Br(),
                                        html.Span("p.praneeta3@gmail.com"),
                                        html.Br(),
                                        html.A("Praneeta's LinkedIn Profile",
                                               href="https://www.linkedin.com/in/praneeta-pradhan", target="_blank"),
                                        # html.Span("https://www.linkedin.com/in/praneeta-pradhan"),
                                    ],
                                    style={
                                        "display": "inline-block",
                                        "margin-right": "20px",
                                        "margin-bottom": "20px",
                                    },
                                ),
                            ]
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Span("Shrishtika Bajracharya"),
                                        html.Br(),
                                        html.Span("shrishtika.vajra@gmail.com"),
                                        html.Br(),
                                        html.A("Shrishtika's LinkedIn Profile",
                                               href="https://www.linkedin.com/in/shrishtika-bajracharya",
                                               target="_blank"),
                                        # html.Span("https://www.linkedin.com/in/shrishtika-bajracharya"),
                                    ],
                                    style={
                                        "display": "inline-block",
                                        "margin-right": "20px",
                                        "margin-bottom": "20px",
                                    },
                                ),
                                html.Div(
                                    [
                                        html.Span("Shusanket Basyal"),
                                        html.Br(),
                                        html.Span("shusanketbasyal76@gmail.com"),
                                        html.Br(),
                                        html.A("Shusanket's LinkedIn Profile",
                                               href="https://www.linkedin.com/in/shusanket-basyal-6b8b03253/",
                                               target="_blank"),
                                        # html.Span("https://www.linkedin.com/in/shusanket-basyal-6b8b03253/"),
                                    ],
                                    style={
                                        "display": "inline-block",
                                        "margin-right": "20px",
                                        "margin-bottom": "20px",
                                    },
                                ),
                                html.Div(
                                    [
                                        html.Span("Zipporah Muse"),
                                        html.Br(),
                                        html.Span("musezipporah@gmail.com"),
                                        html.Br(),
                                        html.A("Zipporah's LinkedIn Profile",
                                               href="www.linkedin.com/in/zipporah-muse-25496724a", target="_blank"),
                                        # html.Span("www.linkedin.com/in/zipporah-muse-25496724a"),
                                    ],
                                    style={
                                        "display": "inline-block",
                                        "margin-right": "20px",
                                        "margin-bottom": "20px",
                                    },
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            style={
                "background-color": "white",
                "padding": "30px",
                "border": "2px solid gray",
                "border-radius": "10px",
                "box-shadow": "2px 2px 5px gray",
                "position": "fixed",
                "transform": "translate(-50%, -50%)",
                "top": "50%",
                "left": "50%",
                "height": "70%",
                "width": "40%",
                "font-size": "20px",
                "z-index": "1000",
                "text-align": "center",
                "overflow": "auto"
            },
        )
    else:
        # Hide the popup content
        popup_content = None

    return popup_content


# Callback to close the popup
@app.callback(
    Output("open-popup-button", "n_clicks"), [Input("close-popup-button", "n_clicks")]
)
def close_popup(n_clicks):
    if n_clicks:
        return 0
    return dash.callback_context.triggered[0]["prop_id"]


@callback(
    Output(component_id="tabs", component_property="children"),
    Input(component_id="graphbutton", component_property="n_clicks"),
    Input(component_id="predictbutton", component_property="n_clicks"),
    Input(component_id="deleteall", component_property="n_clicks"),
    Input(component_id="deletelast", component_property="n_clicks"),
    State(component_id="linegraph", component_property="checked"),
    State(component_id="bargraph", component_property="checked"),
    State(component_id="histogram", component_property="checked"),
    State(component_id="st71checkbox", component_property="checked"),
    State(component_id="st72checkbox", component_property="checked"),
    State(component_id="st80checkbox", component_property="checked"),
    State(component_id="st90checkbox", component_property="checked"),
    State(component_id="st91checkbox", component_property="checked"),
    State(component_id="st92checkbox", component_property="checked"),
    State(component_id="st100checkbox", component_property="checked"),
    State(component_id="st110checkbox", component_property="checked"),
    State(component_id="st120checkbox", component_property="checked"),
    State(component_id="st60acheckbox", component_property="checked"),
    State(component_id="st50acheckbox", component_property="checked"),
    State(component_id="st40acheckbox", component_property="checked"),
    State(component_id="st30acheckbox", component_property="checked"),
    State(component_id="st20acheckbox", component_property="checked"),
    State(component_id="st10acheckbox", component_property="checked"),
    State(component_id="st60bcheckbox", component_property="checked"),
    State(component_id="st50bcheckbox", component_property="checked"),
    State(component_id="st40bcheckbox", component_property="checked"),
    State(component_id="st30bcheckbox", component_property="checked"),
    State(component_id="st20bcheckbox", component_property="checked"),
    State(component_id="st10bcheckbox", component_property="checked"),
    State(component_id="time-start-filter", component_property="value"),
    State(component_id="time-end-filter", component_property="value"),
    State(component_id="throughput_intervals_filter", component_property="value"),
    State(component_id="date-filter", component_property="start_date"),
    State(component_id="date-filter", component_property="end_date"),
    State(component_id="graph-content-filter", component_property="value"),
    State(component_id="lower-end-filter", component_property="value"),
    State(component_id="higher-end-filter", component_property="value"),
    prevent_initial_call=True,
)
def update_graph(*args):
    global tabsname, grapharray, tabCount

    # selecting arguments: they will be in order as in the callback function
    differentgraphs = args[4:7]

    checked_values = args[7:28]  # Extracting checked values from args

    startTime, am_pm1 = args[28].split()
    if (startTime != "12") and (am_pm1 == "PM"):
        startTime = str(int(startTime) + 12)
    else:
        startTime = str(startTime)
    endTime, am_pm2 = args[29].split()
    if (endTime != "12") and (am_pm2 == "PM"):
        endTime = str(int(endTime) + 12)
    else:
        endTime = str(endTime)

    interval_throughput = args[30]
    # startDateFormat = args[29][0]
    # startDate = str(startDateFormat)
    # endDateFormat = args[29][1]
    # endDate = str(endDateFormat)
    startDate = args[31]
    endDate = args[32]
    content = args[33]
    lowerBound = int(args[34].split()[0])
    if args[34].split()[1] == "min":
        lowerBound *= 60
    elif args[34].split()[1] == "hr":
        lowerBound *= 3600
    upperBound = int(args[35].split()[0])
    if args[35].split()[1] == "min":
        upperBound *= 60
    elif args[35].split()[1] == "hr":
        upperBound *= 3600

    # Extract the IDs of the checked checkboxes

    checked_ids = [
        ("st71checkbox", "ST71"),
        ("st72checkbox", "ST72"),
        ("st80checkbox", "ST80"),
        ("st90checkbox", "ST90"),
        ("st91checkbox", "ST91"),
        ("st92checkbox", "ST92"),
        ("st100checkbox", "ST100"),
        ("st110checkbox", "ST110"),
        ("st120checkbox", "ST120"),
        ("st60acheckbox", "ST60A"),
        ("st50acheckbox", "ST50A"),
        ("st40acheckbox", "ST40A"),
        ("st30acheckbox", "ST30A"),
        ("st20acheckbox", "ST20A"),
        ("st10acheckbox", "ST10A"),
        ("st60bcheckbox", "ST60B"),
        ("st50bcheckbox", "ST50B"),
        ("st40bcheckbox", "ST40B"),
        ("st30bcheckbox", "ST30B"),
        ("st20bcheckbox", "ST20B"),
        ("st10bcheckbox", "ST10B"),
    ]

    checked_graphs = ["linegraph", "bargraph", "histogram"]
    # Create a dictionary to store checked checkboxes and their values
    checked_data = {}
    for i, checked in enumerate(checked_values):
        if checked:
            checked_data[checked_ids[i][0]] = checked_ids[i][1]

    listOfNames = []
    for i, checked in enumerate(checked_values):
        if checked:
            listOfNames.append(checked_ids[i][1])

    graphtype = ""

    # Check if only 1 day is selected and start time is not more than end time
    # if startDate == endDate:
    #     if int(startTime) > int(endTime):
    #         error_messages.append("Start date must be before end date")

    # Check if selected date is not in the input file
    # for name in sheet_names:
    #     if startDate not in dfs[name][0] or endDate not in dfs[name][0]:
    #         error_messages.append(f'Selected date range is not available in the input file for {name}.')

    # Check if some filters are not chosen
    # if listOfNames is None:
    #     error_messages.append("Machine not selected")
    # if startDate is None:
    #     error_messages.append("Start date must be selected")
    # if endDate is None:
    #     error_messages.append("End date must be selected")
    # if startTime is None:
    #     error_messages.append("Start time must be selected")
    # if endTime is None:
    #     error_messages.append("End time must be selected")
    # if content is None:
    #     error_messages.append("Select Graph Content")
    # if graphtype is None:
    #     error_messages.append("Select Graph type")

    #
    # @callback(Output(component_id="tabs", component_property="children"),
    #           Input("error_messages")
    #
    # )

    if ctx.triggered_id == "deleteall":
        tabsname.clear()
        grapharray.clear()
        tabCount = 0
        a = update_tabs()

        return a
    
    if ctx.triggered_id == "deletelast":
        if len(tabsname) > 0:
            del tabsname[-1]
            del grapharray[-1]
            tabCount-= 1
            a = update_tabs()
            return a

    # if user hits graphbutton
    if ctx.triggered_id == "graphbutton":
        for j, checked in enumerate(differentgraphs):
            if checked:
                graphtype = checked_graphs[j]
        # if linegraph
        if graphtype == "linegraph":
            # dataframearrays = []
            # for keys, values in checked_data.items():
            #    dataframearrays.append(createsingledataframes(values))
            # createlinegraphs(dataframearrays)

            if content == "Cycle Count":
                createGraph(
                    "line",
                    "productiveCount",
                    listOfNames,
                    startDate,
                    endDate,
                    startTime,
                    endTime,
                    interval_throughput,
                    upperBound,
                    lowerBound,
                )
                a = update_tabs()
                return a
            elif content == "Rate of Productivity":
                createGraph(
                    "line",
                    "rate",
                    listOfNames,
                    startDate,
                    endDate,
                    startTime,
                    endTime,
                    interval_throughput,
                    upperBound,
                    lowerBound,
                )
                a = update_tabs()
                return a
            elif content == "Code Durations":
                createGraph(
                    "line",
                    "times",
                    listOfNames,
                    startDate,
                    endDate,
                    startTime,
                    endTime,
                    interval_throughput,
                    upperBound,
                    lowerBound,
                )
                a = update_tabs()
                return a

        # if bargraph
        if graphtype == "bargraph":
            # dataframearrays = []
            # for keys, values in checked_data.items():
            #     dataframearrays.append(createsingledataframes(values))
            # createbargraphs(dataframearrays)
            createGraph(
                "bar",
                "productiveCount",
                listOfNames,
                startDate,
                endDate,
                startTime,
                endTime,
                interval_throughput,
                upperBound,
                lowerBound,
            )

            a = update_tabs()
            return a
        # if histogram
        if graphtype == "histogram":
            # dataframearrays = []
            # for keys, values in checked_data.items():
            #     dataframearrays.append(createsingledataframes(values))

            # createhistogramgraphs(dataframearrays)
            createGraph(
                "histo",
                "productiveCount",
                listOfNames,
                startDate,
                endDate,
                startTime,
                endTime,
                interval_throughput,
                upperBound,
                lowerBound,
            )

            a = update_tabs()
            return a
    else:
        # if user hits predict button
        predict_graph(checked_data)
        a = update_tabs()
        return a


def update_tabs():
    # function to add new tabs
    global tabsname, grapharray
    # # creates a table list based on the queue tabsname
    # tabs_list = [dmc.Tab(x, value=x) for x in tabsname]
    # # creates tabs_panles based on grapharray
    # tabs_panels = [
    #     dmc.TabsPanel(dcc.Graph(figure=y), value=tabsname[a])
    #     for a in range(len(grapharray))
    #     for y in grapharray[a]
    # ]

    # # updated_tabs
    # updated_tabs = dmc.Tabs(
    #     id="tabs",
    #     color="red",
    #     orientation="horizontal",
    #     children=[dmc.TabsList(tabs_list), *tabs_panels],
    # )

    tabs_list = [dmc.Tab(x, value=x) for x in tabsname]

    # Create TabsPanels with buttons and graphs
    tabs_panels = [
        dmc.TabsPanel(
            dcc.Graph(figure=y),
            value=tabsname[a],
        )
        for a in range(len(grapharray))
        for i, y in enumerate(grapharray[a])
    ]

    # Create the updated Tabs component
    updated_tabs = dmc.Tabs(
        id="tabs",
        color="red",
        orientation="horizontal",
        children=[dmc.TabsList(tabs_list), *tabs_panels],
    )
    return updated_tabs


#
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################
############################################################################################################################################################


global dfs

sheet_names = [
    "ST10A",
    "ST10B",
    "ST20A",
    "ST20B",
    "ST30A",
    "ST30B",
    "ST40A",
    "ST40B",
    "ST50A",
    "ST50B",
    "ST60A",
    "ST60B",
    "ST71",
    "ST72",
    "ST80",
    "ST90",
    "ST91",
    "ST92",
    "ST100",
    "ST110",
    "ST120",
]

dfs = maindataobject.createDictionary(sheet_names)


def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(":"))
    return hours * 3600 + minutes * 60 + seconds


def makeColumns4567():
    for name in sheet_names:
        if pd.api.types.is_datetime64_any_dtype(dfs[name][1]):
            dfs[name][4] = dfs[name][1].dt.time
            dfs[name] = dfs[name].astype({4: "string"})
            dfs[name][6] = dfs[name][4].apply(time_to_seconds)

        if pd.api.types.is_datetime64_any_dtype(dfs[name][2]):
            dfs[name][5] = dfs[name][2].dt.time
            dfs[name] = dfs[name].astype({5: "string"})
            dfs[name][7] = dfs[name][5].apply(time_to_seconds)

    for name in sheet_names:
        dfs[name][8] = dfs[name][7].subtract(dfs[name][6])


makeColumns4567()


def countproductivity(
        df: pd.DataFrame, startime: pd.Timestamp, secondtime: pd.Timestamp
):
    return len(
        df[(df[1] >= startime) & (df[1] < secondtime) & (df[3] == "1 - Productive")]
    )


def createProductivityArray(
        df: pd.DataFrame, startime: pd.Timestamp, endtime: pd.Timestamp, intervals: float
) -> List[int]:
    # INITIALIZING AN ARRAY
    productivityarray = []
    timearray = []

    while startime < endtime:
        # SECOND TIME IS STARTIME + 1 HOUR
        secondtime = startime + pd.Timedelta(hours=intervals)
        # USING THE FUNCTION TO GET THE COUNT
        count = countproductivity(df, startime, secondtime)
        # INCREMENTING STARTIME BY 1 HOUR
        startime += pd.Timedelta(hours=intervals)
        # IF COUNT ==0 THEN SKIP

        if count != 0:
            productivityarray.append(count)
            timearray.append(startime)
    return productivityarray, timearray


global tabCount
tabCount = 0


def lineGraphProductivity(data_dict: Dict[str, List[int]], timearray: List):
    global tabCount
    # Generate an array of 20 distinct colors
    colors = plt.cm.tab20(np.linspace(0, 1, 20))

    labels = list(data_dict.keys())  # Use keys as labels

    names = ""
    fig = go.Figure()
    for label, lst in data_dict.items():
        hours = list(range(len(lst)))
        names += label + ", "
        fig.add_trace(go.Scatter(x=timearray, y=lst, mode="lines", name=label))

    fig.update_layout(
        xaxis_title="Hour of the Day",
        yaxis_title="Productive Counts",
        title="Throughput",
        hovermode="closest",
        height=700,
        xaxis=dict(
            title_font=dict(size=18),
            tickfont=dict(size=14)
        ),
        yaxis=dict(
            title_font=dict(size=18),
            tickfont=dict(size=14)
        ),
        title_font=dict(size=24),
        legend=dict(
            font=dict(size=16)
        )
    )

    fig.update_xaxes(rangeslider_visible=True)

    # creating a random value for tabsname
    a = random.randint(2, 1000)
    names = names[:-2]
    if len(data_dict) > 2:
        parts = names.split(",")
        # Combine the first part (up to the first comma) with the last part (after the last comma)
        names = f"{parts[0]}...{parts[-1].strip()}"
    # adding it to tabsname queue
    tabCount += 1
    tabsname.append(str(tabCount) + ". " + names + " THROUGHPUT GRAPH")
    # adding fig to grapharray queue
    grapharray.append([fig])


def lineGraphRates(data_dict: Dict[str, List[int]], timearray: List):
    global tabCount
    # Generate an array of 20 distinct colors
    colors = plt.cm.tab20(np.linspace(0, 1, 20))

    labels = list(data_dict.keys())  # Use keys as labels

    names = ""
    fig = go.Figure()
    for label, lst in data_dict.items():
        hours = list(range(len(lst)))
        names += label + ", "
        fig.add_trace(go.Scatter(x=timearray, y=lst, mode="lines", name=label))

    fig.update_layout(
        xaxis_title="Hour",
        yaxis_title="Rate per Hour",
        title="Rate of Production vs Hours",
        hovermode="closest",
        height=700,
        xaxis=dict(
            title_font=dict(size=18),
            tickfont=dict(size=14)
        ),
        yaxis=dict(
            title_font=dict(size=18),
            tickfont=dict(size=14)
        ),
        title_font=dict(size=24),
        legend=dict(
            font=dict(size=16)
        )
    )

    fig.update_xaxes(rangeslider_visible=True)
    # creating a random value for tabsname
    a = random.randint(2, 1000)
    names = names[:-2]
    if len(data_dict) > 2:
        parts = names.split(",")
        # Combine the first part (up to the first comma) with the last part (after the last comma)
        names = f"{parts[0]}...{parts[-1].strip()}"
    # adding it to tabsname queue
    tabCount += 1
    tabsname.append(str(tabCount) + ". " + names + " RATE LINE")
    # adding fig to grapharray queue
    grapharray.append([fig])


def graphTimes(data_dict: Dict[str, List[int]]):
    global tabCount
    colors = plt.cm.tab20(np.linspace(0, 1, 20))

    labels = list(data_dict.keys())  # Use keys as labels

    names = ""
    fig = go.Figure()
    for label, lst in data_dict.items():
        names += label + ", "
        fig.add_trace(go.Scatter(x=lst[1], y=lst[8], mode="lines", name=label))

    fig.update_layout(
        xaxis_title="Time of the Day",
        yaxis_title="Duration between Machine Status (seconds)",
        title="Duration of Machine Status vs Time",
        hovermode="closest",
        height=700,
        xaxis=dict(
            title_font=dict(size=18),
            tickfont=dict(size=14)
        ),
        yaxis=dict(
            title_font=dict(size=18),
            tickfont=dict(size=14)
        ),
        title_font=dict(size=24),
        legend=dict(
            font=dict(size=16)
        )
    )
    fig.update_xaxes(rangeslider_visible=True)
    # creating a random value for tabsname
    a = random.randint(2, 1000)
    names = names[:-2]
    if len(data_dict) > 2:
        parts = names.split(",")
        # Combine the first part (up to the first comma) with the last part (after the last comma)
        names = f"{parts[0]}...{parts[-1].strip()}"
    # adding it to tabsname queue
    tabCount += 1
    tabsname.append(str(tabCount) + ". " + names + " STATUS CODES LINE")
    # adding fig to grapharray queue
    grapharray.append([fig])


def barGraphProductivity(data_dict: Dict[str, List[int]], timearray: List):
    global tabCount
    # Generate an array of 20 distinct colors
    colors = plt.cm.tab20(np.linspace(0, 1, 20))

    labels = list(data_dict.keys())  # Use keys as labels

    names = ""
    fig = go.Figure()
    for label, lst in data_dict.items():
        hours = list(range(len(lst)))
        names += label + ", "
        fig.add_trace(go.Bar(x=timearray, y=lst, name=label))

    fig.update_layout(
        xaxis_title="Time of Day/Day",
        yaxis_title="Throughput",
        title="Throughput",
        barmode="group",
        hovermode="closest",
        height=700,
        xaxis=dict(
            title_font=dict(size=18),
            tickfont=dict(size=14)
        ),
        yaxis=dict(
            title_font=dict(size=18),
            tickfont=dict(size=14)
        ),
        title_font=dict(size=24),
        legend=dict(
            font=dict(size=16)
        )
    )

    fig.update_xaxes(rangeslider_visible=True)
    # creating a random value for tabsname
    a = random.randint(2, 1000)
    names = names[:-2]
    if len(data_dict) > 2:
        parts = names.split(",")
        # Combine the first part (up to the first comma) with the last part (after the last comma)
        names = f"{parts[0]}...{parts[-1].strip()}"
    # adding it to tabsname queue
    tabCount += 1
    tabsname.append(str(tabCount) + ". " + names + " THROUGHPUT BAR CHART")
    # adding fig to grapharray queue
    grapharray.append([fig])


def histogramProductivity(data_dict: Dict[str, List[int]]):
    global tabCount
    # Generate an array of 20 distinct colors
    colors = plt.cm.tab20(np.linspace(0, 1, 20))

    labels = list(data_dict.keys())  # Use keys as labels
    num_dataframes = len(data_dict)

    names = ""
    fig = go.Figure()
    for label, lst in data_dict.items():
        names += label + ", "
        fig.add_trace(go.Histogram(x=lst, name=label))

    fig.update_layout(
        xaxis_title="Throughput",
        yaxis_title="Frequency",
        title="Throughput Distribution",
        hovermode="closest",
        height=700,
        xaxis=dict(
            title_font=dict(size=18),
            tickfont=dict(size=14)
        ),
        yaxis=dict(
            title_font=dict(size=18),
            tickfont=dict(size=14)
        ),
        title_font=dict(size=24),
        legend=dict(
            font=dict(size=16)
        )
    )
    fig.update_xaxes(rangeslider_visible=True)
    # creating a random value for tabsname
    a = random.randint(2, 1000)
    names = names[:-2]
    if len(data_dict) > 2:
        parts = names.split(",")
        # Combine the first part (up to the first comma) with the last part (after the last comma)
        names = f"{parts[0]}...{parts[-1].strip()}"
    # adding it to tabsname queue
    tabCount += 1
    tabsname.append(str(tabCount) + ". " + names + " THROUGHPUT HISTOGRAM")
    # adding fig to grapharray queue
    grapharray.append([fig])


###get data with a start, end date, start, end time
def filter_dataframe(
        df: pd.DataFrame, start_date: str, end_date: str, start_time: str, end_time: str
) -> pd.DataFrame:
    # Create start and end datetime objects
    start_datetime = pd.to_datetime(start_date + " " + start_time)
    end_datetime = pd.to_datetime(end_date + " " + end_time)

    # Get the last value of the first column in the DataFrame
    last_value = pd.to_datetime(df.iloc[-1, 0])

    # If end_datetime is greater than the last value, set it to the last value
    if end_datetime > last_value:
        end_datetime = last_value

    # Filter the DataFrame based on the datetime range
    filtered_df = df[(df[1] >= start_datetime) & (df[1] <= end_datetime)]

    return filtered_df


def convertToTimeFormat(time: str):
    if len(time) == 1:
        return "0" + time + ":00:00"
    else:
        return time + ":00:00"


def rateArray(arrayProductivity: List[int], name: str, interval: int):
    percentOfMaxProduction = []
    ##machines with producitvity split between two machines
    if ('A' in name or 'B' in name or '71' in name or '72' in name or '91' in name or '92' in name):

        for x in arrayProductivity:
            capped_value = min(x, (265 * interval))

            res = (capped_value / (265 * interval)) * 100
            percentOfMaxProduction.append(res)
    ##machines with full producitvity
    else:

        for x in arrayProductivity:
            capped_value = min(x, (530 * interval))

            res = (capped_value / (530 * interval)) * 100
            percentOfMaxProduction.append(res)
    return percentOfMaxProduction


def dropHigherThan(df: pd.DataFrame, upper_threshold: int):
    dropHigherThanValues = ["1 hr", "30 min", "15 min", "10 min", "5 min"]
    df = df[df[8] < upper_threshold]
    return df


def dropLowerThan(df: pd.DataFrame, lower_threshold: int):
    dropLowerThanValues = [
        "0 Seconds",
        "5 Seconds",
        "10 Seconds",
        "15 Seconds",
        "20 Seconds",
        "25 Seconds",
        "30 Seconds",
        "35 Seconds",
        "40 Seconds",
        "45 Seconds",
        "50 Seconds",
        "55 Seconds",
        "60 Seconds",
    ]
    df = df[df[8] > lower_threshold]
    return df


def createGraph(
        type: str,
        variable: str,
        machineNames: List[str],
        startDay: str,
        endDay: str,
        startHour: str,
        endHour: str,
        intervals: float,
        higherThan: int,
        lowerThan: int,
):
    startTime = convertToTimeFormat(startHour)
    endTime = convertToTimeFormat(endHour)
    machine_dfs = {}
    for name in machineNames:
        df_copy = dfs[name].copy()
        dataframe = filter_dataframe(df_copy, startDay, endDay, startTime, endTime)
        machine_dfs[name] = dataframe

    if variable == "productiveCount":
        listProductivityArrays = {}
        for df in machine_dfs:
            productivityarray1, timearray1 = createProductivityArray(
                machine_dfs[df],
                machine_dfs[df].iloc[0, 0],
                machine_dfs[df].iloc[len(machine_dfs[df]) - 1, 0],
                intervals,
            )
            listProductivityArrays[df] = productivityarray1

        if type == "line":
            name = "line"
            lineGraphProductivity(listProductivityArrays, timearray1)
        elif type == "bar":
            barGraphProductivity(listProductivityArrays, timearray1)


        elif type == "histo":
            histogramProductivity(listProductivityArrays)


    elif variable == "rate":
        listRates = {}
        listProductivityArrays = {}
        for df in machine_dfs:
            productivityarray1, timearray1 = createProductivityArray(machine_dfs[df], machine_dfs[df].iloc[0, 0],
                                                                     machine_dfs[df].iloc[len(machine_dfs[df]) - 1, 0],
                                                                     intervals
                                                                     )

            listRates[df] = rateArray(productivityarray1, df, intervals)

        lineGraphRates(listRates, timearray1)


    elif variable == "times":
        for name in machineNames:
            if higherThan != -1:
                machine_dfs[name] = dropHigherThan(machine_dfs[name], higherThan)
            if lowerThan != -1:
                machine_dfs[name] = dropLowerThan(machine_dfs[name], lowerThan)

        graphTimes(machine_dfs)


###########################################################################################################################################################
###########################################################################################################################################################
###########################################################################################################################################################
###########################################################################################################################################################
###########################################################################################################################################################
###########################################################################################################################################################


def predict_graph(checked_data):
    global maindataobject, tabsname, grapharray, tabCount
    # getting the id/key of the machine that user has selected
    a = list(checked_data.values())

    key = a[0]
    maindataobject.create_dataframeforsinglemachine(key)
    # extracting necessay infromation  from data.py and passing it to MlModel
    pa, ta = maindataobject.dataforml()
    predict = Predict(pa, ta, key)

    # getting results, time_valid and x_valid
    [results, time_valid, x_valid] = predict.model_forecast(48)
    print(len(time_valid))
    print(len(x_valid))
    print(results.shape)

    # converting time_valid and x_valid to np.array()
    time_valid = np.array(time_valid)
    x_valid = np.array(x_valid)
    # creating a dataframe
    df = pd.DataFrame(
        {"Time": time_valid, "Testing Set": x_valid, "Prediction": results}
    )

    a = random.randint(2, 1000)
    fig1, trend = plot_moving_average(df["Time"], df["Prediction"], 10, a)
    # plotting the dataframe
    fig = px.line(df, x="Time", y=["Testing Set", "Prediction"], title="PREDICTION")

    fig.update_xaxes(rangeslider_visible=True)
    # adding tabname to tabsname queue

    tabCount += 1
    tabsname.append(str(tabCount) + ". PREDICTION FOR " + key)

    # adding fig to graph array
    b = [fig, fig1]
    grapharray.append(b)


def plot_moving_average(x_values: list, y_values: list, window_size: int, a):
    global maindataobject, tabsname, grapharray
    # Calculate the moving average
    moving_average = pd.Series(y_values).rolling(window=window_size).mean()

    # Plot the original data and the moving average
    fig = go.Figure()

    # Add moving average trace
    fig.add_trace(
        go.Scatter(
            x=x_values,
            y=moving_average,
            mode="lines",
            name=f"Moving Average ({window_size} periods)",
        )
    )

    # Add original data trace
    fig.add_trace(
        go.Scatter(x=x_values, y=y_values, mode="lines", name="Predicted Data")
    )

    differences = moving_average.diff()
    cumulative_sum = differences.cumsum()

    # Determine the overall trend
    overall_trend = (
        "Increasing -> Machine is Working OK"
        if cumulative_sum.dropna().iloc[-1] > 0
        else "Decreasing-> Machine is Slowing Down"
    )
    # Update layout
    fig.update_layout(
        title=f"Predicted Data and Moving Average ({window_size} periods )\n Overall Trend of Moving Averages: {overall_trend}",
        xaxis_title="Time of the Day",
        # yaxis_title="Duration between Machine Statuses (seconds)",
        legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99),
        showlegend=True,
    )
    # print(cumulative_sum.dropna().iloc[-1])
    print("Overall Trend of Moving Averages: " + overall_trend)
    return [fig, overall_trend]


if __name__ == "__main__":
    app.run_server()
