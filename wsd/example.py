from wsd import lesk

sentence1 = ['I', 'went', 'to', 'the', 'bank', 'to', 'deposit', 'money', '.']
sentence2 = ['I', 'went', 'to', 'the', 'bank', 'of', 'river', 'on', 'weekend', '.']
sense1 = lesk(sentence1, 'bank', 'n')
sense2 = lesk(sentence2, 'bank', 'n')
print(sense1)
print(sense2)
