import json
from nltk import Tree as Tree
from nltk.corpus import treebank_chunk

class ArticleAnalyzer:

	def __init__(self,chunked_words):
		# load and store the keywords from json file
		self.keywords = self.json_loader("json_data/classifier_keywords.json")
		# store the tagged words
		self.chunked_words = chunked_words
		self.classifications = ['polar','forests','oceans','air','none']

	def json_loader(self,filename):
		with open(filename) as data_file:
			data = json.load(data_file)
		return data

	def convert_chucked_to_str_list(self,chunked_words):
		words = []
		for chunk in chunked_words:
			word = ""
			if isinstance(chunk, Tree):
				word = chunk[0][0] + " " + chunk[1][0]
			else:
				word = chunk[0]
			words.append(word)
		return words

	def classify(self):
		if self.calculate_polar_score() > .15:
			return self.classifications[0]
		elif self.calculate_forests_score() > .15:
			return self.classifications[1]
		elif self.calculate_oceans_score() > .15:
			return self.classifications[2]
		elif self.calculate_air_score() > .15:
			return self.classifications[3]
		else:
			return self.classifications[4]
		# just in case
		return self.classifications[4]


	def calculate_polar_score(self):
		words = self.convert_chucked_to_str_list(self.chunked_words)
		score = 0
		for word in words:
			if word in self.keywords['polarKeywords']:
				score += 5
			if word in self.keywords['sharedKeywords']:
				score += 1
		return score / len(words)

	def calculate_forests_score(self):
		words = self.convert_chucked_to_str_list(self.chunked_words)
		score = 0
		for word in words:
			if word in self.keywords['forestsKeywords']:
				score += 5
			if word in self.keywords['sharedKeywords']:
				score += 1
		return score / len(words)

	def calculate_oceans_score(self):
		words = self.convert_chucked_to_str_list(self.chunked_words)
		score = 0
		for word in words:
			if word in self.keywords['oceansKeywords']:
				score += 5
			if word in self.keywords['sharedKeywords']:
				score += 1
		return score / len(words)

	def calculate_air_score(self):
		words = self.convert_chucked_to_str_list(self.chunked_words)
		score = 0
		for word in words:
			if word in self.keywords['airKeywords']:
				score += 5
			if word in self.keywords['sharedKeywords']:
				score += 1
		return score / len(words)