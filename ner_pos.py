import spacy
import os
from reader import get_data

nlp = spacy.load('en')

def get_named_entites(text):        # Takes a string as an input
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.start_char, ent.end_char, ent.label_))

    return entities                 # Returns name, start character, end character, entity


def get_postags(text):              # Takes a string as an input
    doc = nlp(text)
    postags = []
    for token in doc:
        postags.append((token, token.pos_))

    return postags                  # Returns part of speech tags
