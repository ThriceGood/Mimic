from pudb import set_trace; set_trace()

def myprint(d):

	if isinstance(d, dict):

		for k, v in d.iteritems():
			if isinstance(v, dict):
				# DICT
				myprint(v)
			elif isinstance(v, list):
				# LIST
				myprint(v)
			else:
				# VALUE
				d[k] = 'values_type'
				print '1'
		  		print "{0}".format(v)		  		
		  		pass

	elif isinstance(d, list):

		for v in d:
			if isinstance(v, dict):
				# print v
				myprint(v)
			elif isinstance(v, list):
				myprint(v)
			else:
				v = 'values_type'
				print '2'
		  		print "{0}".format(v)
		  		pass

	else:

		print '3'
		v = 'values_type'
		print "{0}".format(v)


dic = {
	'first_level': {
		'first_1': {
			'1down_1' : 'hi!'
		},
		'first_2': {
			'1down_2': 'hello!',
			'2down_list': [
				'1111',
				'2222',
				{'key1': 'value1', 'key2': 'value2'}
			]
		}
	},
	# 'second_level': {
	# 	'second_1': {
	# 		'2down_1' : 'by!'
	# 	},
	# 	'second_2': {
	# 		'2down_2': 'bylo!'
	# 	}
	# }
}

myprint(dic)