from newspaper import Article
url = 'http://bangordailynews.com/2012/10/12/news/bangor/bangor-police-detectives-blood-alcohol-content-was-0-13-da-says/'

a = Article(url, language='en')

a.download()
a.parse()
a.nlp()

print(a.text)
print(a.title)
print(a.summary)
print(a.keywords)
