""" a user based system with shared database would be cool...
"""
""" this is just an INTERFACE, very little should happen here
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

@app.route('/ui/')
def index():
	# render index page
	return ui.index_page(db)

@app.route('/ui/docs')
def docs():
	# render docs page
	return ui.docs_page()

@app.route('/insert_endpoint', methods=['POST'])
@app.route('/ui/insert_endpoint', methods=['GET'])
def insert_endpoint():
	# [POST]
	# only returning data to call from AJAX
	if request.method == 'POST':
		post_data = request.data
		reponse = endpoint.insert_endpoint(post_data, db)
		# api level can handle representation
		return json.dumps(response)
	# [GET]
	elif request.method == 'GET':
		return ui.insert_endpoint_page()
	# [other verb]
	return json.dumps({'error': 'wrong http method'})


@app.route('/update_endpoint', methods=['PUT'])
@app.route('/ui/update_endpoint/<int:id>', methods=['GET'])
def update_endpoint(id=None):
	# [PUT]
	# only returning data to call from AJAX
	error = 'wrong verb'
	if request.method == 'PUT':
		post_data = request.data
		reponse = endpoint.update_endpoint(post_data, db)
		# api level can handle representation
		return json.dumps(response)
	# [GET]
	elif request.method == 'GET':
		# i think id has to be sent because of 
		# route definition or else it just 404s
		if id:		
			return ui.update_endpoint_page(id, db)
		else:
			error = 'no id provided'
	# [other verb]
	return json.dumps({'error': error})

@app.route('/delete_endpoint/<int:id>')
def delete_endpoint(id):
	# i think id has to be sent because of 
	# route definition or else it just 404s
	if id:
		response = endpoints.delete_endpoint(id)
	else:
		response = {'error': 'no endpoint id provided'}
	return json.dumps(response)

@app.route('/mimic/get')
def mimic_get():
	# take in querys etc
	# maybe should only have a post
	# as only models get passed over
	query = 'query'
	return mimic.get(query)

@app.route('/mimic/post', methods=['POST'])
def mimic_post():
	# take in a post of the model
	# verb, service, endpoint, tag, schema, payload
	endpoint = request.data
	return mimic.post(endpoint) 

if __name__ == '__main__':
	app.run()
