from mimic_wrapper import Mimic

mimic = Mimic('diary')

url = '/diary/entry'
tag = 'diary 1'
payload = '{"key": "type"}'

response = mimic.post(url=url, tag=tag, payload=payload)
print response