import sqlite3
from sql_queries import *
from contextlib import closing

class Database:

	def __init__(self):
		self.database = sqlite3.connect('db/database')
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
		db.execute(create_table)
		self.database.commit()

	def select_endpoint(self, id=None, query=None):
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
		try:
			db.execute(insert, endpoint)
			self.database.commit()
			return {'data': 'success inserted'}
		except Exception as e:
			return {'error': 'error: {}'.format(e)}

	def update_endpoint(self, endpoint):
		db = self.get_cursor()
		try:
			db.execute(update, endpoint)
			self.database.commit()
			return {'data': 'endpoint updated'}
		except Exception as e:
			return {'error': 'error: {}'.format(e)}

	def delete_endpoint(self, id):
		db = self.get_cursor()
		try:
			db.execute(delete_one, (id,))
			self.database.commit()
			return {'data': 'endpoint delete'}
		except Exception as e:
			return {'error': 'error: {}'.format(e)}
