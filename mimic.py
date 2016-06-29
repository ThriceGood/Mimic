from utils import validate_query, validate_payload
import json


class Mimic:

	def get(self, endpoint, db):
		endpoint = json.loads(endpoint)
		url = endpoint['url']
		tag = endpoint['tag']
		query = endpoint.get('query')
		response = db.select_endpoint(where=(url, tag))
		if type(response) is dict and response.get('error'):
			return {'error': response['error']}
		elif response:
			schema = response['schema']
			result = validate_query(query, schema)
			if result:
				return response['payload']			
			error = 'query does not match schema: [{}] != [{}]'.format(query, schema)
			return {'exceptions': error}
		return {'error': 'no endpoint matching url or tag'}

	def post(self, endpoint, db):
		endpoint = json.loads(endpoint)
		url = endpoint['url']
		tag = endpoint['tag']
		payload = endpoint['payload']
		try:
		    payload = json.loads(payload)
		except Exception as e:
			return {'error': 'invalid json in payload: {}'.format(e)}
		response = db.select_endpoint(where=(url, tag))
		if type(response) is dict and response.get('error'):
			return {'error': response['error']}
		elif response:
			schema = json.loads(response['schema'])
			result = validate_payload(payload, schema)
			if result.get('exceptions'):
				return result	
			else:			
				return response['payload']
		return {'error': 'no endpoint matching url or tag'}