import json
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df_cac = pd.read_csv('../cac/df_cac.csv')

app.layout = html.Div([
    html.H1('Grupos por indicador'),
    dbc.Row([
        dbc.Col([
            html.H2('Sel. Indicador'),
            dcc.Dropdown(id='indicador',
                         options=[{'label': indicador, 'value': indicador}
                                  for indicador in df_cac.columns]),
            html.Br(),
        ]),
        dbc.Col([
            html.H2('Sel. Indicador'),
            dcc.Dropdown(id='indicador2',
                         options=[{'label': indicador, 'value': indicador}
                                  for indicador in df_cac.columns]),
            html.Br(),
        ])
    ]),
    dbc.Row([
        dbc.Col([
                dcc.Graph(id='quantity_chart1'),
                ]),
        dbc.Col([
            dcc.Graph(id='stack_events_chart1'),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='quantity_chart2'),
        ]),
        dbc.Col([
            dcc.Graph(id='stack_events_chart2'),
        ])
    ])


])

px.histogram(df_cac, x=df_cac['v45recibioquimio'], labels={
             'x': 'v45recibioquimio', 'y': 'count'})


@app.callback(Output('quantity_chart1', 'figure'),
              Input('indicador', 'value'),
              )
def plot_quantity_by_indicator(indicador):
    if not indicador:
        raise PreventUpdate
    fig = px.histogram(df_cac, x=df_cac[indicador], labels={
        'x': indicador, 'y': 'count'},  nbins=1, width=600, height=300)
    fig.update_xaxes(type='category', categoryorder='total ascending')
    return fig


@app.callback(Output('quantity_chart2', 'figure'),
              Input('indicador', 'value'))
def plot_quantity_by_indicator2(indicador):
    if not indicador:
        raise PreventUpdate
    fig = px.histogram(df_cac, x=df_cac[indicador], labels={
        'x': indicador, 'y': 'count'},  nbins=1, width=600, height=300)
    fig.update_xaxes(type='category', categoryorder='total ascending')
    return fig


@app.callback(Output('stack_events_chart1', 'figure'),
              Input('indicador', 'value'))
def plot_life_events_by_id(indicador):
    if not indicador:
        raise PreventUpdate
    # df_cac = df_cac[df_cac.indicador.eq(0)]

    fig = px.histogram(df_cac, y="id_paciente", x=['diagnostico_reportado_inicio_1er_ciclo',
                                                   'dias_informe_histopatologia_primera_consulta',
                                                   'primera_consulta_ingreso_institucion',
                                                   'finalizacion_primer_esquema_diagnostico_reportado',
                                                   'finalizacion_ultimo_esquema_inicio_ultimo_esquema',
                                                   'primera_cirugia_finalizacion_ultimo_esquema',
                                                   'ultima_cirugia_primera_cirugia',
                                                   'inicio_esquema_radio_diagnostico_reportado',
                                                   'final_esquema_radio_inicio_esquema_radio',
                                                   'incio_ultimo_esquema_radio_final_primer_esquema_radio',
                                                   'final_ultimo_esquema_radio_incio_ultimo_esquema_radio',
                                                   'cirugia_reconstructiva_diagnosticoreportado',
                                                   'primera_consulta_psiquiatriadiagnosticoreportado',
                                                   'primeraconsulta_nutricion_diagnostico_reportado',
                                                   'primera_consulta_paleativodiagnostico_reportado',
                                                   'fecha_muerte_diagnostico_reportado'], orientation='h', width=600, height=300)
    fig.show()
    return fig


@app.callback(Output('stack_events_chart2', 'figure'),
              Input('indicador', 'value'))
def plot_life_events_by_id2(indicador2):
    if not indicador2:
        raise PreventUpdate
    # df_cac = df_cac[df_cac.indicador.eq(0)]

    fig = px.histogram(df_cac, y="id_paciente", x=['diagnostico_reportado_inicio_1er_ciclo',
                                                   'dias_informe_histopatologia_primera_consulta',
                                                   'primera_consulta_ingreso_institucion',
                                                   'finalizacion_primer_esquema_diagnostico_reportado',
                                                   'finalizacion_ultimo_esquema_inicio_ultimo_esquema',
                                                   'primera_cirugia_finalizacion_ultimo_esquema',
                                                   'ultima_cirugia_primera_cirugia',
                                                   'inicio_esquema_radio_diagnostico_reportado',
                                                   'final_esquema_radio_inicio_esquema_radio',
                                                   'incio_ultimo_esquema_radio_final_primer_esquema_radio',
                                                   'final_ultimo_esquema_radio_incio_ultimo_esquema_radio',
                                                   'cirugia_reconstructiva_diagnosticoreportado',
                                                   'primera_consulta_psiquiatriadiagnosticoreportado',
                                                   'primeraconsulta_nutricion_diagnostico_reportado',
                                                   'primera_consulta_paleativodiagnostico_reportado',
                                                   'fecha_muerte_diagnostico_reportado'], orientation='h', width=600, height=300)
    fig.show()
    return fig


def run_server(self,
               port=8050,
               debug=True,
               threaded=True,
               **flask_run_options):
    self.server.run(port=port, debug=debug, **flask_run_options)


if __name__ == '__main__':
    app.run_server(debug=True)
