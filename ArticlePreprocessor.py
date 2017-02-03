import nltk, re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import PunktSentenceTokenizer

class ArticlePreprocessor:

	def __init__(self,article):
		# store the article
		self.article = article
		# store the article without stopwords
		self.article_no_stopwords = self.remove_stop_words(article)
		# tag all words
		self.tagged_article = self.tag_words(self.article_no_stopwords)

	def article_to_list(self,article):
		# get all the words
		words = re.compile('\w+').findall(article)
		# convert all words to lower case
		return [word.lower() for word in words]

	def remove_stop_words(self, article):
		# convert to list to work with easier
		list_of_words = self.article_to_list(article)
		stop_words = set(stopwords.words('english'))
		# lemmatize words (long processing)
		# list_of_words = [self.lemmatize(word) for word in list_of_words]
		output = [word for word in list_of_words if word not in stop_words]
		# convert back to a string
		return ' '.join(output)

	def lemmatize(self,word):
		wordnet_lemmatizer = WordNetLemmatizer()
		return wordnet_lemmatizer.lemmatize(word)

	def tag_words(self, article):
		custom_sentence_tokenizer = PunktSentenceTokenizer(article)
		tokenized = custom_sentence_tokenizer.tokenize(article)
		try:
			for i in tokenized:
				words = nltk.word_tokenize(i)
				tagged = nltk.pos_tag(words)
				return tagged
		except Exception as e:
			pass
			# print(str(e))

	def chuck_words(self,tagged_words):
		'''
		Examples:
		climate(noun) change(verb)
		global(adjective) warming(adjective)
		sea(noun) ice(noun)
		greenhouse(noun) gas(noun)
		fossil(noun) fuels(noun)
		carbon(noun) dioxide(noun)
		'''
		chunk_gram = '''Chunk: {<JJ.?><NN.?> | <NN.?><NN.?> | <JJ.?><JJ.?>}'''
		chunkParser = nltk.RegexpParser(chunk_gram)
		chunked = chunkParser.parse(tagged_words)
		return chunked