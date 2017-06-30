from flask import current_app
from web import app
import unittest
import json

class ContentEngineTestCase(unittest.TestCase):
	"""docstring for ContentEngineTestCase"""
	def test_similar(self):
		context = app.test_request_context()
		context.push()

		from engine import content_engine

		content_engine.train('dummy-data.csv')
		
		data = {'item': 1, 'num':10}
		headers = [('Conent-Type', 'application/json'), ('X-API-TOKEN', current_app.config['API_TOKEN'])]
		json_data = json.dumps(data)
		json_data_length = len(json_data)
		headers.append(('Content-Length', str(json_data_length)))

		response = app.test_client().post('/predict', headers = headers, data = json_data)	
		response = json.loads(response.data)
		self.assertEqual(len(response), 10)
		self.assertEqual(response[0][0], "19")

	if __name__ == '__main__':
	unittest.main()		
		