import sqlite3
from sql_queries import *

class Database:

	def __init__(self):
		database = sqlite3.connect('db/database')
		self.db = database.cursor()		
		with self.db as db:
			db.execute(create_table)

	def select_endpoint(self, id=None, query=None):
		# need to get back a dict for jsoning
		# db has to return 'Rows'
		if id:
			self.db.execute(select_one, [id])
			return db.fetchone()
		elif query:
			self.db.execute(select_query, query)
			return db.fetchall()
		else:
			self.db.execute(select_all)
			return db.fetchall()

	def insert_endpoint(self, endpoint):
		with self.db as db:
			try:
				db.execute(insert, endpoint)
				return {'data': 'success message'}
			except Exception as e:
				return {'error': str(e)}

	def update_endpoint(self, endpoint):
		with self.db as db:
			try:
				db.execute(update, endpoint)
				return {'data': 'success message'}
			except Exception as e:
				return {'error': str(e)}

	def delete_endpoint(self, id):
		with self.db as db:
			try:
				db.execute(delete, [id])
				return {'data': 'success message'}
			except Exception as e:
				return {'error': str(e)}
