import dash
import dash_bio as dashbio
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# Read the FASTA file from the local working directory
with open('alignment_viewer_p53.fasta', 'r') as file:
    data = file.read()

app.layout = html.Div([
    dashbio.AlignmentChart(
        id='my-default-alignment-viewer',
        data=data,
        # colorscale='hydro',   # for changing color
        # conservationcolorscale='blackbody',  # for changing color
        # showconsensus=False,      # for adding/removing consensus
        # showconservation=False,  # for adding/removing bar plot
        # showgap=False,           # for adding/removing bar plot
        height=900,
        tilewidth=30,
    ),
    html.Div(id='default-alignment-viewer-output')
])

@app.callback(
    Output('default-alignment-viewer-output', 'children'),
    Input('my-default-alignment-viewer', 'eventDatum')
)
def update_output(value):
    if value is None:
        return 'No data.'
    return str(value)

if __name__ == '__main__':
    app.run_server(debug=True)
