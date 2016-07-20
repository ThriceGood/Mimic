import logging
import os

log_weights = {
	'info': 1,
	'warning': 2,
	'error': 3,
	'debug': 4
}

class Logger:

	def __init__(self, name):
		self.create_log_dir()
		self.logger = logging.getLogger('{}'.format(name))
		format = "%(asctime)s - %(name)s [%(levelname)s]:  %(message)s"
		logging.basicConfig(format=format, level=logging.DEBUG)
		file_handler = logging.FileHandler('logs/log.log')
		file_handler.setLevel(logging.DEBUG)
		formatter = logging.Formatter(format)
		file_handler.setFormatter(formatter)
		self.logger.addHandler(file_handler)

	def create_log_dir(self):
		root = os.path.dirname(os.path.realpath(__file__))
		logs_dir = os.path.join(root, 'logs')
		if not os.path.isdir(logs_dir):
			os.mkdir(logs_dir)

	def info(self, message):
		self.logger.info(message)

	def warning(self, message):
		self.logger.warning(message)

	def debug(self, message):
		self.logger.debug(message)

	def error(self, message):
		self.logger.error(message)

	def get_logs(self, level):
		# add more specific exceptions, absolute url
		logs = ''
		weight = log_weights[level] if level else 4
		with open('logs/log.log') as log:
			for line in log:
				log_type = line[line.index('[') + 1:line.index(']')]
				if log_weights[log_type.lower()] <= weight:
					logs += line
		return logs











		
