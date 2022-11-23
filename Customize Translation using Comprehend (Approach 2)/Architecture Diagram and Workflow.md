# Approach 2 - Using Custom Terminology to customize and improve translation

In this approach, [Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html) is used to customize and improve Translation. Using [DetectEntities](https://docs.aws.amazon.com/comprehend/latest/dg/using-api-sync.html#get-started-api-entities-python) API call, we will be retrieving the named entities such as brand name, organisation name, person name and so on from the transcription and embed them in angular braces or tags.

What's the effect of angular braces on translation ?

> In case of HTML tags, the following are the effects on translation :

![image](https://user-images.githubusercontent.com/32926625/203531879-c1e20b1a-aaf9-428a-9ade-13feb37f82d9.png)

* Text within the angular braces are not translated. ("b" -> tag , "How are you" -> text)
* Text spanning between the 'Translate="No"' tags do not get translated.
* However, text between the opening and closing of tags get translated unless you use 'translate = "no"' attribute with the HTML tags.


<br>

## Architecture Diagram

<br>

![image](https://user-images.githubusercontent.com/32926625/203530588-4001b0e6-cbe3-48b4-81be-9abf4c937d40.png)

<br>

## Workflow 

1. Lambda function makes DetectEntities API call to Comprehend to detect the entities in the transcript. 

Detecting entities detected in the transcript :

```

{
    'Entities': [{
        'Score': 0.9977008700370789,
        'Type': 'PERSON',
        'Text': 'Nana',
        'BeginOffset': 100,
        'EndOffset': 104
    }, {
        'Score': 0.9982559084892273,
        'Type': 'PERSON',
        'Text': 'Rose',
        'BeginOffset': 137,
        'EndOffset': 141
    }, {
        'Score': 0.9994229078292847,
        'Type': 'PERSON',
        'Text': 'Rose',
        'BeginOffset': 144,
        'EndOffset': 148
    }, {
        'Score': 0.9935682415962219,
        'Type': 'QUANTITY',
        'Text': '84 years',
        'BeginOffset': 160,
        'EndOffset': 168
    }, {
        'Score': 0.9993612170219421,
        'Type': 'PERSON',
        'Text': 'Rose',
        'BeginOffset': 230,
        'EndOffset': 234
    }, {
        'Score': 0.9975423812866211,
        'Type': 'PERSON',
        'Text': 'Lovett',
        'BeginOffset': 273,
        'EndOffset': 279
    }, {
        'Score': 0.9943063259124756,
        'Type': 'QUANTITY',
        'Text': '84 years',
        'BeginOffset': 291,
        'EndOffset': 299
    }, {
        'Score': 0.7720921039581299,
        'Type': 'LOCATION',
        'Text': 'china',
        'BeginOffset': 346,
        'EndOffset': 351
    }, {
        'Score': 0.8280236124992371,
        'Type': 'COMMERCIAL_ITEM',
        'Text': 'Titanic',
        'BeginOffset': 409,
        'EndOffset': 416
    }, {
        'Score': 0.8022783994674683,
        'Type': 'TITLE',
        'Text': 'The Ship of Dreams',
        'BeginOffset': 429,
        'EndOffset': 447
    }, {
        'Score': 0.5594068169593811,
        'Type': 'QUANTITY',
        'Text': 'third-class',
        'BeginOffset': 486,
        'EndOffset': 497
    }],
    'ResponseMetadata': {
        'RequestId': 'fecd0127-3572-4f05-8ca8-4ad5b6be4e17',
        'HTTPStatusCode': 200,
        'HTTPHeaders': {
            'x-amzn-requestid': 'fecd0127-3572-4f05-8ca8-4ad5b6be4e17',
            'content-type': 'application/x-amz-json-1.1',
            'content-length': '1088',
            'date': 'Wed, 10 Aug 2022 08:55:27 GMT'
        },
        'RetryAttempts': 0
    }
}
```

2. Modify input before translation :

_Code snippet to parse out list of “PERSON” entities from the above json and mask them with <> to avoid translation:_

```code
person = list(set(person))
person = [i["Text"] for i in response["Entities"] if i["Type"]=="PERSON"]

for i in person :
    target_string = '<'+i+'>'
    text = text.replace(i,target_string)
```    




## Obervations and Results

Input Text :
```
Will you share it with us? 
(Music Playing) 
(Crying) 
-  I'm taking her to rest. 
- No. - Come on, Nana. 
- No! Tape recorder. Tell us, Rose. 
Rose: It's been 84 years. It's okay.Just try to remember anything-- anything at all. 
Rose: Do you want to hear this or not, Mr. Lovett? It's been 84 years... and I can still smell the fresh paint. The china had never been used. The sheets had never been slept in. Titanic was called "The Ship of Dreams" and it was, it really was. 
Man: All third-class passengers with a forward berth this way, please, this queue
```

Output - Translated text (The below only showcases maintaining context for “PERSON” entities, this can be achieved for PII data, other entities and even for custom entities if CER - Comprehend Custom entity recognition is in use.)
```
क्या आप इसे हमारे साथ साझा करेंगे?
(संगीत बजाना)
(रोना)
मैं उसे आराम करने के लिए ले जा रहा हूं। 
नहीं. - चलो,Nana। 
नहीं! टेप रिकॉर्डर। हमें बताइए,Rose। 
Rose: 84 साल हो गए हैं। यह ठीक है। बस कुछ भी याद रखने की कोशिश करो - कुछ भी।
Rose: क्या आप यह सुनना चाहते हैं या नहीं, श्रीमानLovett? 84 साल हो गए हैं... और मैं अभी भी ताजा पेंट सूंघ सकता हूं। चीन का इस्तेमाल कभी नहीं किया गया था। चादरें कभी सोई नहीं गई थीं। टाइटैनिक को “द शिप ऑफ ड्रीम्स” कहा जाता था और यह था, यह वास्तव में था।
मैन: फॉरवर्ड बर्थ वाले सभी तीसरे श्रेणी के यात्री इस तरह से, कृपया, यह कतार
```
We can notice how the context as a person is maintained in the end result for the characters in the transcript.


