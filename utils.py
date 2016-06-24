

def validate_post_data(post_data, attrs):
	if len(post_data) > attrs:
		excess = set(post_data.keys()) - set(attrs)
		return {'error': 'excess keys: {}'.format(excess)}
	for key in attrs:
		if key not in post_data:
			return {'error': 'missing key: {}'.format(key)}
	return post_data


def payload_to_schema():
	pass	