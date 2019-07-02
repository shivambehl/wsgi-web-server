from flask import Flask

from flask import Response

flask_app = Flask('flaskapp')

@flask_app.route('/hello')
def hello_world():
	return Response(
	'Hello World!\n',
	mimetype='text/plain'
	)

app = flask_app.wsgi_app
