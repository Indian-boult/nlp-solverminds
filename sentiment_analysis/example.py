from get_sentiment import SentimentIntensityAnalyzer
sentences = ['I really like the new design of your website!',
             'I’m not sure if I like the new design',
             'The new design is awful!',
             ]

sid = SentimentIntensityAnalyzer()
for sentence in sentences:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()
