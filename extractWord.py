from textblob import TextBlob
txt = """Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the inter
actions between computers and human (natural) languages."""
f = open("test.txt", "r")
print f.read()
with open('test.txt', 'r') as file:
    data = file.read().replace('\n', '')
    blob = TextBlob(data)
    print '########'
    print 'length of noun phrases', len(blob.noun_phrases)
    print 'length of blob' , len(blob)
    print 'length of data', len(data)
    print blob.noun_phrases

