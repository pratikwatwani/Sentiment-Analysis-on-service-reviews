from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os


os.chdir(r"C:\Users\Pratik\Desktop\Project\ExtractedData\GeneratedData")
with open("positivewords.txt","r",encoding="utf-8") as f:
	postext=f.read()

with open("negativewords.txt","r",encoding="utf-8") as f1:
	negtext=f1.read()

font_path=r'C:\Users\Pratik\Desktop\Project\font\Archivio-900.otf'
poswordcloud = WordCloud(font_path=font_path,
                          background_color='white',
                          width=1920,
                          height=1080
                         ).generate(postext)

plt.imshow(poswordcloud)

plt.axis('off')

os.chdir(r"C:\Users\Pratik\Desktop\Project\ExtractedData\Visualization")
plt.savefig('positivecloud.png', dpi=600,orientation='landscape',
            papertype=None, format=None,transparent=True)


negwordcloud = WordCloud(font_path=font_path,
                          background_color='white',
                          width=1920,
                          height=1080
                         ).generate(negtext)


plt.imshow(negwordcloud)
plt.axis('off')
plt.savefig('negativecloud.png', dpi=600,orientation='landscape',
            papertype=None, format=None,transparent=True)

