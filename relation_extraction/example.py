from get_relation import get_relation
from get_entities import get_entities

sentence ="Language model pretraining has advanced the sate of the art in many nlp tasks."

entites = get_entities(sentence)
relation = get_relation(sentence)

relation_dict = {
    'subject': entites[0],
    'relation': relation,
    'object': entites[1]
}

print(relation_dict)
