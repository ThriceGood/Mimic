from flask import render_template
from utils import payload_to_schema, validate_post_data

class Mimic:

	def get(self, query):
		pass

	def post(self, endpoint, db):
		url = endpoint['endpoint']
		tag = endpoint['tag']
		payload = endpoint['payload']
		# convert passed in payload to schema format
		# a dict of the payloads keys with values
		# representing the types of payload values
		# then query db with that schema
		# some kind of recursive method to go
		# down through the tree structure
		# i need at least valid json for the schema converter
		try:
		    schema = json.loads(schema)
		except Exception as e:
			return {'error': 'invalid json in payload: {}'.format(e)}
		schema = payload_to_schema(payload) # not implemented
		query = (endpoint, tag, schema)
		response = db.select_endpoint(query=query)
		# have to see some responses
		if response == 'ok':
			return response['payload']
		return {'error': 'schema was wrong or something..'}


class Endpoints:

	attrs = ['verb', 'service', 'url', 'tag', 'schema', 'payload']

	def select_endpoint(self):
		# no use for this yet
		# only selects happen from UI
		pass

	def insert_endpoint(self, post_data, db):
		e = validate_post_data(post_data, Endpoint.attrs)
		if e.get('error'):
			return {'error': endpoint['error']}
		endpoint = (
			e['verb'], e['service'], 
		    e['endpoint'], e['tag'], 
		    e['schema'], e['payload']
		)
		return db.insert_endpoint(endpoint)

	def update_endpoint(self, post_data, db):
		attrs = Endpoint.attrs
		attrs.append('id')
		e = validate_post_data(post_data, attrs)
		if e.get('error'):
			return {'error': endpoint['error']}
		endpoint = (
			e['id'], e['verb'], e['service'], 
		    e['endpoint'], e['tag'], 
		    e['schema'], e['payload']
		)
		return db.update_endpoint(endpoint)

	def delete_endpoint(self, id):
		# calls delete query
		# delete logic goes here
		return db.delete_endpoint(id)


class UI:

	def docs_page(self):
		# render documentation page
		return render_template('docs.html')

	def index_page(self, db):
		# render endpoint display
		endpoints = db.select_endpoint()
		# have to see what returns from db
		# return render_template('index.html', endpoints)
		return render_template('index.html')

	def insert_endpoint_page(self):
		# render endpoint definition page
		return render_template('insert.html')

	def update_endpoint_page(self, id, db):
		# render endpoint definition page
		endpoint = db.select_endpoint(id=id)
		# have to see what returns from db
		# return render_template('update.html', endpoint)
		return render_template('update.html')





















