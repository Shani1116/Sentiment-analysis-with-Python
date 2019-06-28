import nltk

text = "I would have gotten the promotion, but my attendance wasn't good enough."

tokenizer = nltk.tokenize.WhitespaceTokenizer()
print(tokenizer.tokenize(text))
