import json
from google.cloud import language_v1
from google.cloud.language_v1 import enums
import os

credentials = {
  "type": "service_account",
  "project_id": "XXXXXXX",
  "private_key_id": "XXXXXXX",
  "private_key": "-----BEGIN PRIVATE KEY-----\nXXXXXXX\n-----END PRIVATE KEY-----\n",
  "client_email": "XXXXXXX",
  "client_id": "XXXXXXX",
  "auth_uri": "XXXXXXX",
  "token_uri": "XXXXXXX",
  "auth_provider_x509_cert_url": "XXXXXXX",
  "client_x509_cert_url": "XXXXXXX"
}

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials

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

