""" a user based system with shared database would be cool...
"""
from flask import Flask, render_template, request, redirect, url_for
from lib import Mimic, Endpoints, UI
from database import Database
import json

mimic = Mimic()
endpoint = Endpoints()
ui = UI()
db = Database()
app = Flask(__name__)

""" Mimic
"""

@app.route('/mimic/get')
def mimic_get():
	query = request.query_string()
	return mimic.get(query)

@app.route('/mimic/post', methods=['POST'])
def mimic_post():
	# verb, service, endpoint, tag, schema, payload
	endpoint = request.data
	response = mimic.post(endpoint, db)
	return json.dumps(response)

""" UI and DD
"""

@app.route('/ui/')
def index():
	return ui.index_page(db)

@app.route('/ui/docs')
def docs():
	return ui.docs_page()

@app.route('/insert_endpoint', methods=['POST'])
@app.route('/ui/insert_endpoint', methods=['GET'])
def insert_endpoint():
	if request.method == 'POST':
		post_data = json.loads(request.data)
		response = endpoint.insert_endpoint(post_data, db)
		return json.dumps(response)
	elif request.method == 'GET':
		return ui.insert_endpoint_page()
	return json.dumps({'error': 'wrong http method'})

@app.route('/update_endpoint', methods=['PUT'])
@app.route('/ui/update_endpoint/<int:id>', methods=['GET'])
def update_endpoint(id=None):
	error = 'wrong verb'
	if request.method == 'PUT':
		post_data = json.loads(request.data)
		response = endpoint.update_endpoint(post_data, db)
		return json.dumps(response)
	elif request.method == 'GET':
		return ui.update_endpoint_page(id, db)
	return json.dumps({'error': error})

@app.route('/delete_endpoint/<int:id>')
def delete_endpoint(id):
	response = endpoint.delete_endpoint(id, db)
	return json.dumps(response)


if __name__ == '__main__':
	app.run()
