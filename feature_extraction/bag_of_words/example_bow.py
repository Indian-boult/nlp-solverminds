from BagOfWords import get_bow
import numpy as np
cat_in_the_hat_docs=[
       "One Cent, Two Cents, Old Cent, New Cent: All About Money (Cat in the Hat's Learning Library",
       "Inside Your Outside: All About the Human Body (Cat in the Hat's Learning Library)",
       "Oh, The Things You Can Do That Are Good for You: All About Staying Healthy (Cat in the Hat's Learning Library)",
       "On Beyond Bugs: All About Insects (Cat in the Hat's Learning Library)",
       "There's No Place Like Space: All About Our Solar System (Cat in the Hat's Learning Library)"
      ]

vector = get_bow(cat_in_the_hat_docs, max, stop_words=['all', 'in', 'the', 'is', 'and'])
print(vector.shape)
print(vector.toarray())
