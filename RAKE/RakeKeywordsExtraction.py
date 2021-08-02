from rake_nltk import Rake
# import nltk
# nltk.download('stopwords')
# nltk.download('punkt')
Rake = Rake()
textfile = open("./Articles/Article3.txt","r+") 
text = textfile.read()
Rake.extract_keywords_from_text(text)
keywords = Rake.get_ranked_phrases()
print(keywords)