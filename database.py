import sqlite3
from sql_queries import *
from contextlib import closing

class Database:

	def __init__(self):
		self.database = sqlite3.connect('db/database')
		# self.database.row_factory = sqlite3.Row
		self.database.row_factory = self.dict_factory
		self.create_table()

	def get_cursor(self):
		return self.database.cursor()

	def dict_factory(self, cursor, row):
	    d = {}
	    for i, col in enumerate(cursor.description):
	        d[col[0]] = row[i]
	    return d

	def create_table(self):
		db = self.get_cursor()
		with closing(db) as db:
			db.execute(create_table)

	def select_endpoint(self, id=None, query=None):
		# need to get back a dict for jsoning
		# db has to return 'Rows'
		db = self.get_cursor()
		if id:
			db.execute(select_one, [id])
			return db.fetchone()
		elif query:
			db.execute(select_query, query)
			return db.fetchall()
		else:
			db.execute(select_all)
			return db.fetchall()

	def insert_endpoint(self, endpoint):
		db = self.get_cursor()
		with closing(db) as db:
			try:
				db.execute(insert, endpoint)
				return {'data': 'success message'}
			except Exception as e:
				return {'error': str(e)}

	def update_endpoint(self, endpoint):
		db = self.get_cursor()
		with closing(db) as db:
			try:
				db.execute(update, endpoint)
				return {'data': 'success message'}
			except Exception as e:
				return {'error': str(e)}

	def delete_endpoint(self, id):
		db = self.get_cursor()
		with closing(db) as db:
			try:
				db.execute(delete, [id])
				return {'data': 'success message'}
			except Exception as e:
				return {'error': str(e)}
