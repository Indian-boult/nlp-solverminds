# import these modules
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import spacy

def do_stemming(tokens):
    ps = PorterStemmer()
    stemms = {}
    for w in tokens:
        stemms[w] = ps.stem(w)

    return stemms

def do_lemmatization(text):
    # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = spacy.load("en_core_web_sm")
    lemmas = {}
    # Process whole documents
    doc = nlp(text)

    for token in doc:
        lemmas[token] = token.lemma_

    return lemmas

def rm_custom_sw(tokens, custom_sw):
    filtered_tokens = []
    for token in tokens:
        if token not in custom_sw:
            filtered_tokens.append(token)

    return filtered_tokens
