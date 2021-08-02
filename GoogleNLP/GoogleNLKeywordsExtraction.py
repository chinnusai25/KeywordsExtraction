import json
from google.cloud import language_v1
from google.cloud.language_v1 import enums
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './gnp/nlp-test-ad8ad9f5347e.json'

client = language_v1.LanguageServiceClient()
type_ = enums.Document.Type.PLAIN_TEXT

keywords=[]
language = "en"
document = {"content": text_content, "type": type_, "language": language}

encoding_type = enums.EncodingType.UTF8

response = client.analyze_entities(document, encoding_type=encoding_type)
for entity in response.entities:
    if entity.salience > 0.0005 and enums.Entity.Type(entity.type).name != "OTHER":
        keywords.append(entity.name)

print(keywords)

