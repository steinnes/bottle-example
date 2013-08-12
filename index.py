from bottle import route, view, run

@route('/')
@route('/<urlpathdatahere>')
@view('template.html')
def index(urlpathdatahere='default value'):
	return dict(stuff=urlpathdatahere)


run(host='0.0.0.0', port=8000, debug=True)
