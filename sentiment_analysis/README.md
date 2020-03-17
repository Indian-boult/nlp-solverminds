# Sentiment analysis
## Installation
1. Install nltk
```bash
pip install nltk
```
2. Launch python prompt on terminal.
3. Run following in a python prompt.
```bash
import nltk
nltk.download('vader_lexicon')
```

## Usage
```bash
>>> from get_sentiment import SentimentIntensityAnalyzer
>>> sentences = ['I really like the new design of your website!',
...              'I’m not sure if I like the new design',
...              'The new design is awful!',
...              ]
>>> sid = SentimentIntensityAnalyzer()
>>> for sentence in sentences:
...     print(sentence)
...     ss = sid.polarity_scores(sentence)
...     for k in sorted(ss):
...         print('{0}: {1}, '.format(k, ss[k]), end='')
...     print()
...
I really like the new design of your website!
compound: 0.474, neg: 0.0, neu: 0.694, pos: 0.306,
I’m not sure if I like the new design
compound: -0.4717, neg: 0.404, neu: 0.596, pos: 0.0,
The new design is awful!
compound: -0.5093, neg: 0.451, neu: 0.549, pos: 0.0,
```
