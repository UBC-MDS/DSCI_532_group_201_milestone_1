import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import altair as alt
import vega_datasets
app = dash.Dash(__name__, assets_folder='assets')
server = app.server
app.title = 'Dash app with pure Altair HTML'
# Boostrap CSS.
app.css.append_css({'external_url': 'https://codepen.io/amyoshino/pen/jzXypZ.css'})
## Magic happens here
app.layout = html.Div([
    ### ADD CONTENT HERE like: html.H1('text'),
    html.H1('Natural Disasters And Their Impact Across The World'),
    html.H2('Total Number of Deaths So Far: ____'),
    html.H3('Plot 1'),
    html.Iframe(
        sandbox='allow-scripts',
        id='plot',
        height='470',
        width='655',
        style={'border-width': '0'},
        ################ The magic happens here
        src='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Unico_Anello.png/1920px-Unico_Anello.png',
        ################ The magic happens here
        ),
])
# html.Div([
#     ### ADD CONTENT HERE like: html.H1('text'),
#     html.H3('Plot 2'),
#     html.Iframe(
#         sandbox='allow-scripts',
#         id='plot',
#         height='470',
#         width='1000',
#         style={'border-width': '0'},
#         ################ The magic happens here
#         src='https://images.unsplash.com/photo-1508138221679-760a23a2285b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80'
#         ################ The magic happens here
#         ),
# ])
if __name__ == '__main__':
    app.run_server(debug=True)