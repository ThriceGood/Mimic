import requests
import json

mimic_get_url = 'http://127.0.0.1:5000/mimic/get'
mimic_post_url = 'http://127.0.0.1:5000/mimic/post'

class Mimic:

	def __init__(self, service=None):
		self.service = service

	def get(self, url, tag, query=None, service=None):
		# maybe pass a dict in to be converted to query string
		service = service if self.service is None else self.service
		if service:
			data = {
				'service': service, 
				'url': url, 
				'tag': tag
				}
			if query:
				data['query'] = query
			data = json.dumps(data)
			response = requests.post(mimic_get_url, data=data)
			return response.text
		else:
			raise AttributeError(
				'service has not been set, generic service ' \
				'call requires service name as argument')

	def post(self, url, tag, payload, service=None):
		service = service if self.service is None else self.service
		if service:
			data = json.dumps({
				'service': service, 
				'url': url, 
				'tag': tag, 
				'payload': payload
				})
			response = requests.post(mimic_post_url, data=data)
			return response.text
		else:
			raise AttributeError(
				'service has not been set, generic service ' \
				'call requires service name as argument')

	def put(self):
		service = service if self.service is None else self.service
		if service:
			data = json.dumps({
				'service': service, 
				'url': url, 
				'tag': tag, 
				'payload': payload
				})
			response = requests.post(mimic_post_url, data=data)
			return response.text
		else:
			raise AttributeError(
				'service has not been set, generic service ' \
				'call requires service name as argument')

	def delete(self):
		pass
