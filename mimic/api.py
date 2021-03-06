from flask import Flask, request
from mimic import Mimic
from endpoint import Endpoint
from ui import UI
from database import Database
from logger import Logger
import json
import os

mimic = Mimic()
endpoint = Endpoint()
ui = UI()
log = Logger('API')
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
	if type(response) is dict:
		return json.dumps(response)
	return response

@app.route('/mimic/post', methods=['POST'])
def mimic_post():
	""" Mimic generic POST endpoint """
	db = get_db()
	endpoint = request.data
	response = mimic.post(endpoint, db)
	if type(response) is dict:
		return json.dumps(response)
	return response

""" UI and DB
"""

@app.route('/ui/')
def index():
	db = get_db()
	print os.path.dirname(os.path.realpath(__file__))
	return ui.index_page(db)

@app.route('/ui/docs')
def docs():
	return ui.docs_page()

@app.route('/ui/test')
def test():
	return ui.test_page()

@app.route('/ui/logs')
def logs():
	return ui.logs_page()

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

@app.route('/delete_endpoint/<int:id>' )
def delete_endpoint(id):
	db = get_db()
	response = endpoint.delete_endpoint(id, db)
	return json.dumps(response)


""" app
"""

@app.route('/logs')
@app.route('/logs/<level>')
def get_logs(level=None):
	logs = log.get_logs(level)
	return json.dumps({'logs': logs})

def run():
	app.run(debug=True)
	# app.run()

if __name__ == '__main__':
	app.run(debug=True)
