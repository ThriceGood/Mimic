from mimic_wrapper import Mimic

# POST
mimic = Mimic()
# generic mimic
url = '/orchestration/run'
tag = 'orch run'
payload = '{"go": 1, "for it": 2}'
response = mimic.post(service='orchestration', url=url, tag=tag, payload=payload)
print response

# GET, query
mimic = Mimic('alarm')
url = '/alarm/query'
tag = 'alarm query2'
query = '?name=alarm'
response = mimic.get(url=url, tag=tag, query=query)
print response

# GET, no query
mimic = Mimic('alarm')
url = '/alarm/raise'
tag = 'alarm no query'
response = mimic.get(url=url, tag=tag)
print response