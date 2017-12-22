# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import io

LANGUAGE = "vietnamese"
SENTENCES_COUNT = 1


if __name__ == "__main__":
    # url = "http://www.24h.com.vn/an-ninh-hinh-su/tiet-lo-dau-vet-tay-xoa-sua-chua-trong-ho-so-vu-1-cu-damdoat-mang-dong-nghiep-c51a918451.html"
    # parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    file = io.open("doc/result.txt", "w")
    parser = PlaintextParser.from_file("doc/test.txt", Tokenizer(LANGUAGE))
    # stemmer = Stemmer(LANGUAGE)

    # summarizer = TextRankSummarizer()
    summarizer = LexRankSummarizer()
    summary = summarizer(parser.document, SENTENCES_COUNT)
    # for sentence in summary:
    file.write('\n'.join('%s' % x for x in summary))
    file.close()
