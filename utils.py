import json

def validate_post_data(post_data, attrs):
	if len(post_data) > attrs:
		excess = set(post_data.keys()) - set(attrs)
		return {'error': 'excess keys: {}'.format(excess)}
	for key in attrs:
		if key not in post_data:
			return {'error': 'missing key: {}'.format(key)}
	return post_data

def compare_schema(payload, schema):
	print payload
	print 'to'
	print schema
	result = get_payload_shape(payload) == get_payload_shape(schema)
	return result

def get_payload_shape(payload):
    if isinstance(payload, dict):
        return {key:get_payload_shape(payload[key]) for key in payload}
    else:
        return None
