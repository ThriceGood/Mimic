from flask import render_template

class Mimic:

	def get(self, query):
		# get the query
		# return the data or error
		# return 'get: output or error'
		pass

	def post(self, endpoint, db):
		e = endpoint
		# will probably have to get back schema 
		# to dict it for a proper comparison
		query = (e['enpoint'], e['tag'], e['schema'])
		response = db.select_endpoint(query=query)
		# have to see some responses
		if response == 'ok':
			return response['payload']
		return {'error': 'schema was wrong or something..'}


class Endpoint:
	
	def select_endpoint(self):
		# no use for this yet
		# only selects happen from UI
		pass

	def insert_endpoint(self, post_data, db):
		# validation, add Nones etc..
		# then insert
		# i need to see the post data
		endpoint = (
			verb, service, endpoint, tag, schema, payload
		)
		return db.insert_endpoint(endpoint)

	def update_endpoint(self, post_data, db):
		# takes post data
		# validates
		# update db
		endpoint = (
			verb, service, endpoint, tag, schema, payload
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
		return render_template('index.html', endpoints)

	def insert_endpoint_page(self):
		# render endpoint definition page
		return render_template('insert.html')

	def update_endpoint_page(self, id, db):
		# render endpoint definition page
		endpoint = db.select_endpoint(id=id)
		# have to see what returns from db
		return render_template('update.html', endpoint)





















