import json
import urlparse

def validate_post_data(post_data, attrs):
	if len(post_data) > attrs:
		excess = set(post_data.keys()) - set(attrs)
		return {'error': 'excess keys: {}'.format(excess)}
	for key in attrs:
		if key not in post_data:
			return {'error': 'missing key: {}'.format(key)}
	return post_data

def query_to_schema(query, schema):
	# any invalid querys will return false
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

def payload_to_schema(payload, schema):
	result = get_payload_shape(payload) == get_payload_shape(schema)
	return result

def get_payload_shape(payload):
    if isinstance(payload, dict):
        return {key:get_payload_shape(payload[key]) for key in payload}
    else:
        return None

"""
SIMPLE RULES:

validate schema against multiple schemas
to get different responses

get all keys and values in a dict on its own
you could do simple value checks with it

"""
