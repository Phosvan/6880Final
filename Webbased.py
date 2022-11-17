from dash import Dash, html, Input, Output, dcc
import dash_cytoscape as cyto

app = Dash(__name__)
# This is going to be an alternate data style to facilatate a more node spicific
# data stream. Each node will have its own values, the user will affect pressure.


# app.layout = html.Div([
#     cyto.Cytoscape(
#         id='cytoscape-elements-boolean',
#         layout={'name': 'preset'},
#         style={'width': '100%', 'height': '400px'},
#         elements=[
#             {
#                 'data': {'id': 'one', 'label': 'Locked'},
#                 'position': {'x': 75, 'y': 75},
#                 'locked': True
#             },
#             {
#                 'data': {'id': 'two', 'label': 'Selected'},
#                 'position': {'x': 75, 'y': 200},
#                 'selected': True
#             },
#             {
#                 'data': {'id': 'three', 'label': 'Not Selectable'},
#                 'position': {'x': 200, 'y': 75},
#                 'selectable': False
#             },
#             {
#                 'data': {'id': 'four', 'label': 'Not grabbable'},
#                 'position': {'x': 200, 'y': 200},
#                 'grabbable': False
#             },
#             {'data': {'source': 'one', 'target': 'two'}},
#             {'data': {'source': 'two', 'target': 'three'}},
#             {'data': {'source': 'three', 'target': 'four'}},
#             {'data': {'source': 'two', 'target': 'four'}},
#         ]
#     )
# ])

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

nodes = [
    {
        'data': {'id': short, 'label': label},
        'position': {'x': 20 * lat, 'y': -20 * long}
    }
    for short, label, long, lat in (
        ('N1', '1st Node', 34.03, -118.25),
        ('N2', '2nd Node', 40.71, -74),
        ('N3', '3rd Node', 43.65, -79.38),
        ('N4', '4th Node', 45.50, -73.57),
        ('N5', '5th Node', 49.28, -123.12),
        ('N6', '6th Node', 41.88, -87.63),
        ('N7', '7th Node', 42.36, -71.06),
        ('N8', '8th Node', 29.76, -95.37)
    )
]

edges = [
    {'data': {'source': source, 'target': target}}
    for source, target in (
        ('N5', 'N1'),
        ('N1', 'N6'),
        ('N8', 'N6'),
        ('N3', 'N4'),
        ('N4', 'N7'),
        ('N2', 'N7'),
        ('N3', 'N8'),
        ('N3', 'N2'),
        ('N1', 'N2'),
        ('N2', 'N7')
    )
]

default_stylesheet = [
    {
        'selector': 'node',
        'style': {
            'background-color': '#BFD7B5',
            'label': 'data(label)'
        }
    }
]

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-event-callbacks-2',
        layout={'name': 'preset'},
        elements=edges + nodes,
        stylesheet=default_stylesheet,
        style={'width': '100%', 'height': '450px'}
    ),
    html.P(id='cytoscape-tapNodeData-output'),
    html.P(id='cytoscape-tapEdgeData-output'),
    html.P(id='cytoscape-mouseoverNodeData-output'),
    html.P(id='cytoscape-mouseoverEdgeData-output')
])


# callbacks are needed to ensurea app is updateing on the backend when the nodes are being minupulated
@app.callback(Output('cytoscape-tapNodeData-output', 'children'),
              Input('cytoscape-event-callbacks-2', 'tapNodeData'))
def displayTapNodeData(data):
    if data:
        return "You recently clicked/tapped the node: " + data['label']


@app.callback(Output('cytoscape-tapEdgeData-output', 'children'),
              Input('cytoscape-event-callbacks-2', 'tapEdgeData'))
def displayTapEdgeData(data):
    if data:
        return "You recently clicked/tapped the edge between " + \
               data['source'].upper() + " and " + data['target'].upper()


@app.callback(Output('cytoscape-mouseoverNodeData-output', 'children'),
              Input('cytoscape-event-callbacks-2', 'mouseoverNodeData'))
def displayTapNodeData(data):
    if data:
        return "You recently hovered over the node: " + data['label']


@app.callback(Output('cytoscape-mouseoverEdgeData-output', 'children'),
              Input('cytoscape-event-callbacks-2', 'mouseoverEdgeData'))
def displayTapEdgeData(data):
    if data:
        return "You recently hovered over the edge between " + \
               data['source'].upper() + " and " + data['target'].upper()


if __name__ == '__main__':
    app.run_server(debug=True)
