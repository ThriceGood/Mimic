import os
import sqlite3
from sql_queries import *

class Database:

	def __init__(self):
		self.create_db_dir()
		db_path = os.path.join(self.db_dir, 'database')		
		self.database = sqlite3.connect(db_path)
		self.database.row_factory = self.dict_factory
		self.create_table()

	def create_db_dir(self):
		root = os.path.dirname(os.path.realpath(__file__))
		self.db_dir = os.path.join(root, 'db')
		if not os.path.isdir(self.db_dir):
			os.mkdir(self.db_dir)

	def get_cursor(self):
		return self.database.cursor()

	def dict_factory(self, cursor, row):
	    results_dict = {}
	    for index, column in enumerate(cursor.description):
	        results_dict[column[0]] = row[index]
	    return results_dict

	def create_table(self):
		db = self.get_cursor()
		db.execute(create_table)
		self.database.commit()

	def select_endpoint(self, id=None, where=None):
		db = self.get_cursor()
		try:
			if id:
				db.execute(select_one, [id])
				return db.fetchone()
			elif where:
				db.execute(select_query, where)
				return db.fetchone()
			else:
				db.execute(select_all)
				return db.fetchall()
		except Exception as e:
			return {'error': 'error: {}'.format(e)}

	def insert_endpoint(self, endpoint):
		db = self.get_cursor()
		try:
			db.execute(insert, endpoint)
			self.database.commit()
			return {'success': 'endpoint inserted'}
		except Exception as e:
			return {'error': 'error: {}'.format(e)}

	def update_endpoint(self, endpoint):
		db = self.get_cursor()
		try:
			db.execute(update, endpoint)
			self.database.commit()
			return {'success': 'endpoint updated'}
		except Exception as e:
			return {'error': 'error: {}'.format(e)}

	def delete_endpoint(self, id):
		db = self.get_cursor()
		try:
			db.execute(delete_one, (id,))
			self.database.commit()
			return {'success': 'endpoint deleted'}
		except Exception as e:
			return {'error': 'error: {}'.format(e)}
