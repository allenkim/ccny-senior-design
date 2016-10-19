from newspaper import Article
from random import randint

with open("links.txt","r") as infile:
    links = infile.readlines()

with open("links_with_query.txt","a") as outfile:
    count = 1
    for url in links:
        a = Article(url.strip(), language='en')
        a.download()
        try:
            a.parse()
        except Exception as e:
            continue
        a.nlp()
        outfile.write(url)
        outfile.write(a.title + "\n")
        summary = a.summary.splitlines()
        if len(summary) == 0:
            outfile.write("\n")
        else:
            outfile.write(summary[randint(0,len(summary)-1)] + "\n")
        outfile.write(str(a.keywords) + "\n\n")
        print("Processed " + str(count) + " articles")
        count += 1
