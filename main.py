# -*- coding: utf-8 -*-

import nltk, re, json
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer

from ArticlePreprocessor import ArticlePreprocessor
from ArticleAnalyzer import ArticleAnalyzer

with open('test_data/arctic_article.txt', 'r') as myfile:
	arctic_article = myfile.read().replace('\n', '')

with open('test_data/arctic_article2.txt', 'r') as myfile:
	arctic_article2 = myfile.read().replace('\n', '')

with open('test_data/regular_article.txt', 'r') as myfile:
	regular_article = myfile.read().replace('\n', '')

with open('test_data/forest_article.txt', 'r') as myfile:
	forest_article = myfile.read().replace('\n', '')

with open('test_data/oceans_article.txt', 'r') as myfile:
	oceans_article = myfile.read().replace('\n', '')

with open('test_data/oceans_article2.txt', 'r') as myfile:
	oceans_article2 = myfile.read().replace('\n', '')

with open('test_data/air_article.txt', 'r') as myfile:
	air_article = myfile.read().replace('\n', '')


article_preprocessor = ArticlePreprocessor(oceans_article2)
tagged_words = article_preprocessor.tagged_article
chunked_words = article_preprocessor.chuck_words(tagged_words)

aa = ArticleAnalyzer(chunked_words)
print(aa.classify())