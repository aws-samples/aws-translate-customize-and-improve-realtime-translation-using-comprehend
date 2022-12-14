import json
import boto3

client = boto3.client('translate')

def lambda_handler(event, context):
    
    input_text = '''Will you share it with us? 
    (Music Playing) 
    (Crying) 
    -  I'm taking her to rest. 
    - No. - Come on, Nana. 
    - No! Tape recorder. Tell us, Rose. 
    Rose: It's been 84 years. It's okay.Just try to remember anything-- anything at all. 
    Rose: Do you want to hear this or not, Mr. Lovett? It's been 84 years... and I can still smell the fresh paint. The china had never been used. The sheets had never been slept in. Titanic was called "The Ship of Dreams" and it was, it really was. 
    Man: All third-class passengers with a forward berth this way, please, this queue.'''
    
    response = client.translate_text(
    Text=input_text,
    TerminologyNames=[
        'titanic',
    ],
    SourceLanguageCode='en',
    TargetLanguageCode='hi')
    
    print(response) 
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
