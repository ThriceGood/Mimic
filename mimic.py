from utils import query_to_schema, payload_to_schema
import json


class Mimic:

	def get(self, endpoint, db):
		endpoint = json.loads(endpoint)
		url = endpoint['url']
		tag = endpoint['tag']
		query = endpoint.get('query')
		response = db.select_endpoint(query=(url, tag))
		if type(response) is dict and response.get('error'):
			return {'error': response['error']}
		elif response:
			schema = response['schema']
			result = query_to_schema(query, schema)
			if result:
				return response['payload']				
			return {'error': 'bad query string'}
		return {'error': 'no matching url or tag'}

	def post(self, endpoint, db):
		""" algorithm doesnt work if there are lists
		"""
		endpoint = json.loads(endpoint)
		url = endpoint['url']
		tag = endpoint['tag']
		payload = endpoint['payload']
		try:
		    payload = json.loads(payload)
		except Exception as e:
			return {'error': 'invalid json in payload: {}'.format(e)}
		response = db.select_endpoint(query=(url, tag))
		if type(response) is dict and response.get('error'):
			return {'error': response['error']}
		elif response:
			schema = json.loads(response['schema'])
			result = payload_to_schema(payload, schema)
			if result:				
				return response['payload']				
			return {'error': 'bad request schema'}
		return {'error': 'no matching url or tag'}