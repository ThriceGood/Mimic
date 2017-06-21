from flask import render_template
from logger import Logger

log = Logger('UI')

class UI:

	def docs_page(self):
		return render_template('docs.html')

	def logs_page(self):
		logs = log.get_logs()
		return render_template('logs.html', logs=logs)

	def test_page(self):
		return render_template('test.html')

	def index_page(self, db):
		endpoints = db.select_endpoint()
		return render_template('index.html', data=endpoints)

	def insert_endpoint_page(self):
		return render_template('insert.html')

	def update_endpoint_page(self, id, db):
		endpoint = db.select_endpoint(id=id)
		return render_template('update.html', data=endpoint)
