import os
import re     
import json


os.chdir(r"C:\Users\Pratik\Desktop\Project\ExtractedData\GeneratedData")
with open("sentencespolarlist.txt","r",encoding="utf-8") as f:
	contents=f.read()

	
      


positive_reviews = []    

negative_reviews = []    

neutral_reviews = []    


data = re.findall(r'(.*?)(\{.*?\})', contents, re.M)        


for line in data:
	sentence = line[0].rstrip(' ').rstrip('-')
	json_string = line[1].replace("'", '"')
	review_data = json.loads(json_string)
	if review_data['pos'] > 0 :
		positive_reviews.append(sentence)
	if review_data['neg'] > 0 :    
		negative_reviews.append(sentence)
	if review_data['neu'] > 0 :    
		neutral_reviews.append(sentence)

		
with open("PositiveSentences.txt","w+",encoding="utf-8") as f:
	f.write('\n'.join(positive_reviews))


with open("NegativeSentences.txt","w+",encoding="utf-8") as f:
	f.write('\n'.join(negative_reviews))

	
with open("NeutralSentences.txt","w+",encoding="utf-8") as f:
        f.write('\n'.join(neutral_reviews))


	


