import re
import pickle
import nltk
from nltk.corpus import stopwords
import spacy

def process(text):
    """
    Clean a string for newlines, bullets, numbering, chunk of spaces,
    punctuation and, convert the string to lowercase

    :param str text: The string to be processed, passed a an python string
    :return str processed: processed text.
    """
    processed = text.replace('\n', ' ').replace('\r', '')
    processed = re.sub('\d\.\s+|[a-z]\)\s+|•\s+|[A-Z]\.\s+|[IVX]+\.\s+', ' ', text)
    processed = re.sub(r'\s+', ' ', processed)
    processed = re.sub(r'[^\w\s]','',processed)
    processed = re.sub("\d+", " ", processed)
    processed = processed.lower()
    processed = processed.strip()
    return processed

def do_tokeinze(text, tool='nltk'):
    """
    The native nltk string tokenizer with support for spacy.

    :param str text: The string to be tokenized, passed a as python string
    :param str tool: Tool to be used for tokenization. (default 'nltk')
    :return list processed: tokenized text
    """
    if tool == 'spacy':
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(text)
        tokens = []
        for token in doc:
            tokens.append(token.text)
        return tokens
    elif tool == 'nltk':
        return nltk.tokenize.word_tokenize(text)

def rm_stopwords(token_list):
    """
    function to remove stopwords as specified in nltk english stopwords from a
    list of tokens.

    :param list token_list: list of tokens to be filtered
    :return list clean_token_list: filtered list of tokens (no stopwords)
    """
    eng_stopwords = set(stopwords.words('english'))
    clean_token_list = []
    for token in token_list:
        if token not in(eng_stopwords):
            clean_token_list.append(token)

    return clean_token_list
