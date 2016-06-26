from mimic_wrapper import Mimic

# POST
# generic mimic
mimic = Mimic()
url = '/service1/url'
tag = 'my service1 call'
payload = '{"key1": "value1", "key2": "value2"}'
response = mimic.post(service='service1', url=url, tag=tag, payload=payload)
print response

# GET, query
mimic = Mimic('service2')
url = '/service2/url'
tag = 'my service2 call'
query = '?name=alarm'
response = mimic.get(url=url, tag=tag, query=query)
print response

# GET, no query
mimic = Mimic('service3')
url = '/service3/url'
tag = 'my service3 call'
response = mimic.get(url=url, tag=tag)
print response