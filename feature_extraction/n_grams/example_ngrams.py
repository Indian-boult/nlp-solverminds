from Ngrams import ngrams

n = 2
n_gen = ngrams('Better problem definitions often lead to better solutions.'.split(), n)

n_gram_list = list(n_gen)
print(n_gram_list)
