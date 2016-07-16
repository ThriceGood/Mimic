from flask import render_template


class UI:

	def docs_page(self):
		return render_template('docs.html')

	def logs_page(self):
		logs = []
		# add checks
		with open('logs/log.log') as log:
			for line in log:
				logs.append(line)
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
