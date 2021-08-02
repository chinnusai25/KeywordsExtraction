import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='us-west-2')
                
textfile = open("text.txt","r+") 
text = textfile.read()

print('Calling DetectKeyPhrases')
print(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectKeyPhrases\n')
