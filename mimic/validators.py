import json
import urlparse
from logger import Logger
from deepdiff import DeepDiff

log = Logger('Validation')

def validate_post_data(post_data, attrs):
	log.debug('validating: {}'.format(post_data))
	if len(post_data) > attrs:
		excess = set(post_data.keys()) - set(attrs)
		return {'error': 'excess keys: {}'.format(excess)}
	for key in attrs:
		if key not in post_data:
			return {'error': 'missing key: {}'.format(key)}
	for key, value in post_data.items():
		if not value:
			error = 'value for {} is empty'.format(key)
			log.error(error)
			return {'error': error}
	return post_data

def validate_query(query, schema):
	# query strings to dicts, any invalid querys will equal false
	query = dict(urlparse.parse_qsl(urlparse.urlsplit(query).query))
	schema = dict(urlparse.parse_qsl(urlparse.urlsplit(schema).query))
	try:
		if len(query) != len(schema):
			return False
	except:
		return False
	for key in query:
		if key not in schema:
			return False
	return True

def validate_payload(payload, schema):
	diff = DeepDiff(payload, schema)
	result = {'exceptions': []}	
	not_allowed = ['dic_item_added', 'dic_item_removed']
	for exception, details in diff.iteritems():
		if exception in not_allowed:
			result['exceptions'].append({exception: str(details)})
	return result


