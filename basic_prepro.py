import re
import pickle
import nltk
from nltk.corpus import stopwords
import spacy

def process(text):                                                                      # Input type: str
    processed = text.replace('\n', ' ').replace('\r', '')                               # New line and carriage return removal
    processed = re.sub('\d\.\s+|[a-z]\)\s+|•\s+|[A-Z]\.\s+|[IVX]+\.\s+', ' ', text)     # Bullets & numbering removal
    processed = re.sub(r'\s+', ' ', processed)                                          # Continuous sapce removal
    processed = re.sub(r'[^\w\s]','',processed)                                         # Punctuation & special chars removal
    processed = re.sub("\d+", " ", processed)                                           # Numbers removal
    processed = processed.lower()                                                       # Case conversion
    processed = processed.strip()
    return processed                                                                    # Output type: str

def do_tokeinze(text, tool):                                                                  # Tokenization
    if tool == 'spacy':
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(text)
        tokens = []
        for token in doc:
            tokens.append(token.text)
        return tokens
    elif tool == 'nltk':
        return nltk.tokenize.word_tokenize(text)

def rm_stopwords(text):                                                                 # Input type: str
    eng_stopwords = set(stopwords.words('english'))                                     # Reading english stopwords
    data = process(text)                                                                # Basic data preprocessing
    data_tokenized = do_tokeinze(data)                                                  # Tokenization
    data_wo_stpwrds = []
    for token in data_tokenized:                                                        # Stopwords removal
        if token not in(eng_stopwords):
            data_wo_stpwrds.append(token)

    return data_wo_stpwrds                                                              # Returns tokenized data without stopwords
                                                                                            # Output type: list
