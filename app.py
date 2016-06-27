""" a user based system with shared database would be cool...
"""
from flask import Flask, request
from mimic import Mimic
from endpoint import Endpoint
from ui import UI
from database import Database
import json

mimic = Mimic()
endpoint = Endpoint()
ui = UI()
app = Flask(__name__)

def get_db():
	return Database()


""" Mimic
"""

@app.route('/mimic/get', methods=['POST'])
def mimic_get():
	""" Mimic generic GET endpoint """
	db = get_db()
	endpoint = request.data
	response = mimic.get(endpoint, db)
	return json.dumps(response)

@app.route('/mimic/post', methods=['POST'])
def mimic_post():
	""" Mimic generic POST endpoint """
	db = get_db()
	endpoint = request.data
	response = mimic.post(endpoint, db)
	return json.dumps(response)

""" UI and DB
"""

@app.route('/ui/')
def index():
	db = get_db()
	return ui.index_page(db)

@app.route('/ui/docs')
def docs():
	return ui.docs_page()

@app.route('/ui/test')
def test():
	return ui.test_page()

@app.route('/insert_endpoint', methods=['POST'])
@app.route('/ui/insert_endpoint', methods=['GET'])
def insert_endpoint():
	db = get_db()
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
	db = get_db()
	if request.method == 'PUT':
		post_data = json.loads(request.data)
		response = endpoint.update_endpoint(post_data, db)
		return json.dumps(response)
	elif request.method == 'GET':
		return ui.update_endpoint_page(id, db)
	return json.dumps({'error': error})

@app.route('/delete_endpoint/<int:id>' )
def delete_endpoint(id):
	db = get_db()
	response = endpoint.delete_endpoint(id, db)
	return json.dumps(response)


""" app
"""

@app.before_request
def before_request():
	pass

@app.teardown_request
def teardown_request(exception):
	pass

def run():
	app.run(debug=True)

if __name__ == '__main__':
	# app.run()
	app.run(debug=True)
