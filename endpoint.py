from utils import validate_post_data


class Endpoint:

	attrs = ['verb', 'service', 'url', 'tag', 'schema', 'payload']

	def select_endpoint(self):
		pass

	def insert_endpoint(self, post_data, db):
		e = validate_post_data(post_data, Endpoint.attrs)
		if e.get('error'):
			return {'error': e['error']}
		endpoint = (
			e['verb'], e['service'], 
		    e['url'], e['tag'], 
		    e['schema'], e['payload'])
		return db.insert_endpoint(endpoint)

	def update_endpoint(self, post_data, db):
		attrs = Endpoint.attrs
		attrs.append('id')
		e = validate_post_data(post_data, attrs)
		attrs.remove('id')
		if e.get('error'):
			return {'error': e['error']}
		endpoint = (
			e['verb'], e['service'], 
		    e['url'], e['tag'], 
		    e['schema'], e['payload'], int(e['id']))
		return db.update_endpoint(endpoint)

	def delete_endpoint(self, id, db):
		return db.delete_endpoint(id)