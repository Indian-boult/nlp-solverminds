import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import os
import pickle
import re
import spacy
import string

nlp = spacy.load('en_core_web_sm')

def process(text):
    """
    Clean a string for newlines, bullets & numbering, punctuation,
    uppercase chars chunk of spaces.

    :param str text: The string to be processed, passed a an python string
    :return str processed: processed text.
    """
    # replace newlines with spaces and deleting carriage returns
    newl_mod = text.replace("\n", " ").replace("\r", "")
    # Removing bullets and numbering
    bulnum_mod = re.sub("\d\.\s+|[a-z]\)\s+|•\s+|[A-Z]\.\s+|[IVX]+\.\s+", "", newl_mod)
    # Punctuation removal
    punc_mod = bulnum_mod.translate(str.maketrans("", "", string.punctuation))
    # Case conversion
    case_mod = punc_mod.lower()
    # special chars removal
    schar_mod = re.sub("[^A-Za-z0-9]+", " ", case_mod)
    # Space chunks removal
    space_mod = re.sub("\s+", " ", schar_mod)
    # Strip the text
    processed = space_mod.strip()
    # Return processed text
    return processed

def do_tokeinze(text):
    """
    The native nltk string tokenizer.

    :param str text: The string to be tokenized, passed a as python string
    :return list processed: tokenized text
    """
    return nltk.tokenize.word_tokenize(text)

def rm_stopwords(token_list):
    """
    function to remove stopwords as specified in nltk english stopwords from a
    list of tokens.

    :param token_list: list of tokens to be filtered
    :type list: iterable of strings
    :return clean_token_list: list of tokens (no stopwords)
    :type list: iterable of strings
    """
    eng_stopwords = set(stopwords.words('english'))
    clean_token_list = []
    for token in token_list:
        if token not in(eng_stopwords):
            clean_token_list.append(token)

    return clean_token_list

def do_stemming(text):
    """
    :param text: string to be stemmed
    :type str: python string
    :return stemms: iterable of strings
    :type list: python list
    """
    tokens = word_tokenize(text)
    ps = PorterStemmer()
    stemms = []
    for w in tokens:
        stemms.append(ps.stem(w))

    return stemms

def do_lemmatization(text):
    """
    :param text: sting to be lemmatized
    :type str: python string
    :return lemmas: iterable of strings
    :type list: python list
    """
    # Load English tokenizer, tagger, parser, NER and word vectors
    lemmas = []
    # Process whole documents
    doc = nlp(text)

    for token in doc:
        lemmas.append(token.lemma_)

    return lemmas

def rm_custom_sw(text, custom_sw):
    """
    :param text: text from which the custom stopwords to be removed
    :type string: python string
    :param custom_sw: iterable of stopwords to be removed
    :type list: python list

    :return filtered_tokens: Tokenized text with custom stopwords removed
    :type list: python list
    """
    filtered_tokens = []
    for token in tokens:
        if token not in custom_sw:
            filtered_tokens.append(token)

    return filtered_tokens

def get_named_entites(text):
    """
    :param text: text from which the named entities to be fetched
    :type string: python string

    :return entities: List of tuples, each tuple is having entity name, its
                        start char and end char, entity type
    :type list: python list of tuples
    """
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.start_char, ent.end_char, ent.label_))

    return entities


def get_postags(text):
    """
    :param text: text from which the part-of-speech tags to be identified
    :type string: python string

    :return postags: List of tuples, each tuple is having token and  it's predicted
                        part-of-speech tag
    :type list: python list of tuples
    """
    doc = nlp(text)
    postags = []
    for token in doc:
        postags.append((token, token.pos_))

    return postags
