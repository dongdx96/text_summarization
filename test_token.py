#!/usr/bin/env python
# -*- coding: utf8 -*-

import nltk
import io
import re
import sys
from nltk.tokenize import RegexpTokenizer
from pyvi.pyvi import ViTokenizer as ViTok
from sumy.nlp.tokenizers import Tokenizer
import sentences_proccess




# tokenizer = Tokenizer('japanese')
# expected = (
#             '１つ目の文章です。',
#             'その次は何が来ますか？',
#             '「２つ目の文章」です。'
#         )
# paragraph = '１つ目の文章です。その次は何が来ますか？　「２つ目の文章」です。'
# # print tokenizer.to_sentences(paragraph)
# for t in tokenizer.to_sentences(paragraph):
# 	print t 


# tokenizer = Tokenizer("vietnamese")
tokenizer = Tokenizer("english")
sentences = tokenizer.to_words("""he walked to the store yesterday""")
# words = "Anh_ấy xin chào mọi người... Ha ha vui quá? Một con mèo tên shi."
# words = tokenizer.to_words("Anh_ấy xin chào mọi người. Ha ha vui quá.")
# sentences = tokenizer.to_sentences(words)
# print words
for t in sentences:
	print t
# filename = "doc/document.txt"

# file = io.open(filename, "r", encoding="utf-8")
# text = file.read()

# tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
# test = tokenizer.tokenize(text)

# for t in words:
# 	print t
# text = nltk.word_tokenize(ViTok.tokenize(text))

