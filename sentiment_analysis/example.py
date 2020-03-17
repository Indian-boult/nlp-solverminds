from get_sentiment import SentimentIntensityAnalyzer
sentences = ['Coronet has the best lines of all day cruisers!',
             'Bertram has a deep V hull and runs easily through seas.',
             'Pastel-colored 1980s day cruisers from Florida are ugly.',
             ]

sid = SentimentIntensityAnalyzer()
for sentence in sentences:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print("\n")
