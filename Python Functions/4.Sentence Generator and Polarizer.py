import os
import nltk
from nltk.tokenize import sent_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


os.chdir(r"C:\Users\Pratik\Desktop\Project\ExtractedData\FetchedData")



with open("Extracted_Reviews.txt",encoding="utf-8") as f:
	text=f.read()

if not os.path.exists(r"C:\Users\Pratik\Desktop\Project\ExtractedData\GeneratedData"):
    os.makedirs(r"C:\Users\Pratik\Desktop\Project\ExtractedData\GeneratedData")
                      

set_path=r"C:\Users\Pratik\Desktop\Project\ExtractedData\GeneratedData"
os.chdir(set_path)

sentences=sent_tokenize(text)
lower_sentences= [sentence.lower() for sentence in sentences]
          
with open("sentences.txt","w+",encoding="utf-8") as f1:
	f1.write('\n'.join(lower_sentences))



with open("sentencespolarlist.txt","w+",encoding="utf-8") as f:
       for sentence in lower_sentences:
           vs=analyzer.polarity_scores(sentence)
           f.write("{:-<65} {}\n".format(sentence, str(vs)))



	
	
