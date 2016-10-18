from newspaper import Article

with open("links.txt","r") as infile:
    links = infile.readlines()

with open("links_with_query.txt","a") as outfile:
    count = 1
    for url in links:
        outfile.write(url)
        a = Article(url.strip(), language='en')
        a.download()
        a.parse()
        a.nlp()
        outfile.write(a.title)
        outfile.write(a.summary + "\n")
        outfile.write(str(a.keywords) + "\n\n")
        print("Processed " + str(count) + " articles")
        count += 1
