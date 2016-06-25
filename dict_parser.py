# from pudb import set_trace; set_trace()

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

# myprint(dic)











def getshape(d):
    if isinstance(d, dict):
        return {k:getshape(d[k]) for k in d}
    else:
        # Replace all non-dict values with None.
        return None

def shape_equal(d1, d2):
    return getshape(d1) == getshape(d2)


d1 = {
	'a': {
		'c': 1,
		'd': 2
	},
	'b': {
		'e': 333,
		'f': 444
	},
	'1': {
		'2': 'abbbb',
		'3': {
			'aa' : 123,
			'bb' : {
				'123': 'abc'
			},
		},
	}
}


d2 = {
	'a': {
		'c': 111,
		'd': 222
	},
	'b': {
		'e': 333,
		'f': 444
	},
	'1': {
		'2': 'a',
		'3': {
			'aa' : 123,
			'bb' : {
				'11123': 'aaaaaabc'
			}
		}
	}
}

print shape_equal(d1, d2)