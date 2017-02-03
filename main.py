# -*- coding: utf-8 -*-

import nltk, re, json
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer

from ArticlePreprocessor import ArticlePreprocessor
from ArticleAnalyzer import ArticleAnalyzer

with open('test_data/arctic_article.txt', 'r') as myfile:
	arctic_article = myfile.read().replace('\n', '')

with open('test_data/regular_article.txt', 'r') as myfile:
	regular_article = myfile.read().replace('\n', '')

article_preprocessor = ArticlePreprocessor(regular_article)
tagged_words = article_preprocessor.tagged_article
chunked_words = article_preprocessor.chuck_words(tagged_words)

aa = ArticleAnalyzer(chunked_words)
print(aa.classify())