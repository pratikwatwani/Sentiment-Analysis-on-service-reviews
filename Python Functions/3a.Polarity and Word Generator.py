import nltk
import os
import re
os.chdir(r"C:\Users\Pratik\Desktop\Project\ExtractedData\FetchedData")

with open("Extracted_Reviews.txt","r",encoding="utf-8") as f:
    text=f.read()

low_text=text.lower()

from nltk import RegexpTokenizer
tokenizer=RegexpTokenizer(r'\w+')
holder=tokenizer.tokenize(low_text)

from nltk.corpus import stopwords
stops=set(stopwords.words('english'))
new_holder=[word for word in holder if word not in stops]

tags=nltk.pos_tag(new_holder)


lists=[]
for tag in tags:
    if((tag[1]=='NN') or (tag[1]=='RB')):
        lists.append(tag[0])





newlists=[]
for element in lists:
    if len(element)>2:
        newlists.append(element)

'''
with open("adjective_adverblist.txt","a") as f2:
    for element in newlists:
        f2.write("%s\n"%element)
'''
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

os.chdir(r"C:\Users\Pratik\Desktop\Project\ExtractedData\GeneratedData")
#OUTPUT 
with open("polarlist.txt","w+",encoding="utf-8") as f3:
    for element in newlists:
        vs = analyzer.polarity_scores(element)
        f3.write("{:-<65} {}\n".format(element, str(vs)))
    
    
####
#to get positive words

from ast import literal_eval


with open("polarlist.txt","r") as f4:
    contents=f4.read()
    
items = re.findall(r"([^\s-]+)-+\s*(\{.*?\})", contents)
d = {i[0]: literal_eval(i[1]) for i in items}
positive_list=[k for k in d if d[k]['pos'] > 0]

negative_list=[k for k in d if d[k]['neg'] > 0]

neutral_list=[k for k in d if d[k]['neu']>0]




from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()




from nltk import pos_tag

poslemmlist=[]
for word in positive_list:
    ll=wordnet_lemmatizer.lemmatize(word,'a')
    poslemmlist.append(ll)



neglemmlist=[]
for word in negative_list:
    ll=wordnet_lemmatizer.lemmatize(word,'a')
    neglemmlist.append(ll)

neulemmlist=[]
for word in neutral_list:
    ll=wordnet_lemmatizer.lemmatize(word,'a')
    neulemmlist.append(ll)
    
with open("positivewords.txt","w+",encoding="utf-8") as f5:
    for word in poslemmlist:
        f5.write("%s\n"%word)

with open("negativewords.txt","w+",encoding="utf-8") as f6:
    for word in neglemmlist:
        f6.write("%s\n"%word)

with open("neutralwords.txt","w+",encoding="utf-8") as f7:
    for word in neulemmlist:
        f7.write("%s\n"%word)

        
    

