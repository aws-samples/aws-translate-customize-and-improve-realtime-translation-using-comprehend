import json
import boto3

comprehend_client = boto3.client('comprehend')
translate_client = boto3.client('translate')


def lambda_handler(event, context):
    
    with open('transcript.txt') as f:
        text = f.read()
    
    print(text)
    
    # response = client.detect_pii_entities( 
    #     Text=text, 
    #     LanguageCode='en')
        
    # print(response)
    
    response = comprehend_client.detect_entities(
        Text= text,
        LanguageCode='en')
    print(response)
    
    person = [i["Text"] for i in response["Entities"] if i["Type"]=="PERSON"]
    print(person)
    
    person = list(set(person))
    print(person)
    
    for i in person :
        target_string = '<'+i+'>'
        text = text.replace(i,target_string)
        
    response = translate_client.translate_text(
        Text=text,
        SourceLanguageCode='en',
        TargetLanguageCode='hi')
    print(response)
    
    print(response["TranslatedText"])
    
    final_text = response["TranslatedText"].replace("<","")
    final_text = final_text.replace(">","")

    print(final_text)
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
