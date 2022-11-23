In this approach, we will be using [Custom terminology](https://docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html) to customize Tranlsation. Using custom terminology with your translation requests enables you to make sure that your brand names, character names, model names, and other unique content is translated exactly the way you need it, regardless of its context and the Amazon Translate algorithm’s decision.

When a translation request comes in, Amazon Translate reads the source sentence, creates a semantic representation of the content (in other words, it understands it), and generates a translation into the target language.

In scenarios where a custom terminology is used as part of the translation request, the engine scans the terminology file before returning the final result. When the engine identifies an exact match between a terminology entry and a string in the source text, it locates the appropriate string in the proposed translation and replaces it with the terminology entry.

<br>

## Architecture Diagram

![image](https://user-images.githubusercontent.com/32926625/203523514-0d035852-18c0-4955-8ad8-db76f02add96.png)

<br>

## Workflow 

1. [Create a Custom terminology file](https://docs.aws.amazon.com/translate/latest/dg/creating-custom-terminology.html) for the words/phrases which are to be customized for translation. 
2. Amazon Transcribe converts in input video/audio to transcript
3. Amazon Translate integrates uses custom terminology to customize the translation at runtime. In our example (for the Titanic transcription), we have created a custom terminology called "custom_terminology.csv" in this folder. The same can be imported to Amazon Translate. 
4. Amazon Polly converts custom translated text to speech.

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

Output - Translated text
```
मैन: फॉरवर्ड बर्थ वाले सभी तीसरे श्रेणी के यात्री इस तरह से, कृपया, यह कतार। 
क्या आप इसे हमारे साथ साझा करेंगे? 
(संगीत बजाना) 
(रोना) 
मैं उसे आराम करने के लिए ले जा रहा हूं। 
नहीं। - आओ, Nana। 
नहीं! टेप रिकॉर्डर। हमें बताइए, रोज। 
रोज: 84 साल हो गए हैं। यह ठीक है। बस कुछ भी याद रखने की कोशिश करो - कुछ भी। 
रोज: क्या आप यह सुनना चाहते हैं या नहीं, Mr. Lovett? 84 साल हो गए हैं... और मैं अभी भी ताजा पेंट सूंघ सकता हूं। चीन का इस्तेमाल कभी नहीं किया गया था। चादरें कभी सोई नहीं गई थीं। टाइटैनिक को “द शिप ऑफ ड्रीम्स” कहा जाता था और यह था, यह वास्तव में था। 
```
_*Improvements seen in end result :*_

* Rose is always translated to “रोज” and not “गुलाब” anymore. Output translation is consistent
* Context of addressing Mr. Lovett as “Mr” is maintained.

## Drawbacks

In scenarios where a movie or a huge file is being dubbed which involves a lot of entities/characters/brand names/proper nouns in general, a static list needs to be maintained which is not a scalable solution.

This is being addressed in the 2nd approach where the solution uses Comprehend to detect entities and PII data dynamically and translate the text while maintaining the context using a custom workflow.


