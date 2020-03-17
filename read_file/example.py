from reader import get_data
from basic_prepro import process, do_tokeinze
text, title = get_data('001.pdf')

processed = process(text)
print(len(do_tokeinze(processed)))
