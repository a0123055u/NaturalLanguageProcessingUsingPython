from textblob import TextBlob
import re
import pycountry
#replace symbols with empty string for easy NLP processing
original_text = open('test1.txt').read()
new_string = re.sub('[^a-zA-Z0-9\n\.]', ' ', original_text)
open('temp.txt', 'w').write(new_string)

#read line by line to aviod memory intense working of RAM
filepath = 'temp.txt'

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}".format(cnt))
       line = fp.readline()
       cnt += 1
       blob = TextBlob(line)
       print '##############################################'
       print 'length of noun phrases', len(blob.noun_phrases)
       print '##############################################'
       noun = blob.noun_phrases
       #write noun to file noun
       open('noun.txt','a+').write(str(noun))
       #need to process the above to take persons, organisation from the noun
       for country in pycountry.countries:
           if country.name in line:
               #write the country to seperate file
               line = line.replace(country.name,"<country> {} </country>".format(country.name))               
               open('country.txt', 'a+').write(line)
                         
fp.close()



