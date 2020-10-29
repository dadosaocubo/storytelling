import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

data_canada = px.data.gapminder().query("country == 'Canada'")
bar = px.bar(data_canada, x='year', y='pop')

data_country = px.data.gapminder().query("year==2007")
bubble = px.scatter(data_country, x="gdpPercap", y="lifeExp",
                    size="pop", color="continent",
					hover_name="country", log_x=True, size_max=60)


app.layout = html.Div(children=[
		html.H1(children='Hello Dados ao Cubo'),

		html.Div(
			[
				html.H6(
					"Dash: É um framework de aplicações WEB para Python.", className="subtitle padded"
				),
				html.Img(
					src='https://dash.plotly.com/assets/images/logo-plotly.png'
				),
				html.Img(
					src='https://dash.plotly.com/assets/images/logo-seperator.png'
				),
				html.Img(
					src='https://dash.plotly.com/assets/images/logo-dash.png'
				)
			],
			className="img",
		),
		html.Div(
			[
				html.H6(
					"Aqui temos um exemplo de gráfico Bar Charts", className="subtitle padded"
				),
				dcc.Graph(
					id='example-bar',
					figure=bar
				)
			],
			className="img",
		),
		html.Div(
			[
				html.H6(
					"Aqui temos um exemplo de gráfico Bubble Charts", className="subtitle padded"
				),
				dcc.Graph(
					id='example-bubble',
					figure=bubble
				)
			],
			className="img",
		),
	])	
	
if __name__ == '__main__':
    app.run_server(debug=True)