import json
import urlparse
from deepdiff import DeepDiff

def validate_post_data(post_data, attrs):
	if len(post_data) > attrs:
		excess = set(post_data.keys()) - set(attrs)
		return {'error': 'excess keys: {}'.format(excess)}
	for key in attrs:
		if key not in post_data:
			return {'error': 'missing key: {}'.format(key)}
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


