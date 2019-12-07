import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


body = dbc.Container(

    [   dbc.Row([html.H2("Impact of Disasters on Human Lives", style={'font-family':'Helvetica','color':'darkblue'},className  = "mt-4")]),
        dbc.Row(
            [
                dbc.Col(
                    [
                        
                        html.Iframe(
                                          sandbox='allow-scripts',
                                          id='plot_a',
                                          height = '480',
                                          width = '1350',
                                          style={'border':'light', 'position':'relative', 'float':'center'},

                                          ################ The magic happens here
                                          srcDoc=open('charts/world_combined_plots.html').read()
                                          ################ The magic happens here
                                          )
                    ]
                )
            ]
        , className = "mt-4 mr-0"),
        
      dbc.Row(
      [
          dbc.Col(
              [
                  
                  html.Iframe(
                                    sandbox='allow-scripts',
                                    id='plot_b',
                                    height = '600',
                                    width = '1350',
                                    style={'border':'light'},

                                    ################ The magic happens here
                                    srcDoc=open('charts/world_map_line.html').read()
                                    ################ The magic happens here
                                    )
                  
                  
              ]
          )
      ]
  )
    ],
    className="ml-5 mt-1",
)

footer = dbc.Container([

        dbc.Row([dbc.Button("Data Source", href = "https://ourworldindata.org/natural-disasters#summary", color = "link")]),
        dbc.Row(html.H6("   This Dash app is collaborative work of (alphabetically): Gaurav Sinha, Jack Tan, Jasmine Qin & Karanpal Singh (Group 201)"))

        ],  className="ml-5 mt-1")




app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Natural Disaster"
server = app.server

app.layout = html.Div([body,footer])

if __name__ == "__main__":
    app.run_server()
