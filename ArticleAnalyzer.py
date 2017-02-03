import json

class ArticleAnalyzer:

	def __init__(self,article):
		# load and store the keywords from json file
		self.keywords = self.json_loader("json_data/classifier_keywords.json")

	def json_loader(self,filename):
		with open(filename) as data_file:
			data = json.load(data_file)
		return data