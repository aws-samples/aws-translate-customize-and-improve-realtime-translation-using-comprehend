## Overview

Audio dubbing is the process of replacing the original dialogue from your video or film with new audio. Unlike Voiceover, which plays over your videos but is separate from your content, audio dubbing aims to replace the dialogue as precisely and organically as possible.

Traditional dubbing is an expensive and time-consuming process, and AI voices provide a cheap and scalable alternative to them. A typical AI workflow to dub audio/video is as mentioned below :

<br>


## Workflow and Architecture

<br>

![image](https://user-images.githubusercontent.com/32926625/203485943-7cc84c9b-2b1f-4480-85b8-f026918d49bd.png)

<br>


1. End users/clients fire requests to dub a audio/video file from Soruce language (abc) to a Target language (xyz) where (abc,xyz) is known as the language pair.
2. [Amazon Transcribe](https://aws.amazon.com/transcribe/) is used to convert the audio to text. Amazon Transcribe is an automatic speech recognition (ASR) service that makes it easy for developers to add speech to text capability to their applications.
3. [Amazon Translate](https://aws.amazon.com/translate/) is a text translation service that uses advanced machine learning technologies to provide high-quality translation on demand. Amazon Translate is used to translate the transcription from step 2 from source language "abc" to target language "xyz".
4. [Amazon Polly](https://aws.amazon.com/polly/) converts the translated text into life-like speech.


<br>

## Scenario

We often encounter inconsistencies in translations where the context gets lost during the course of translation.

For instance, lets consider the language pair (en-US,hi) where we are translating the input from English (US) to Hindi. The input considered here a transcript from a scene from Titanic.

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
क्या आप इसे हमारे साथ साझा करेंगे? 
(संगीत बजाना) 
(रोना) 
- मैं उसे आराम करने के लिए ले जा रहा हूं। 
- नहीं। - आओ, नाना। 
- नहीं! टेप रिकॉर्डर। हमें बताइए, गुलाब। 
रोज: 84 साल हो गए हैं। यह ठीक है। बस कुछ भी याद रखने की कोशिश करो - कुछ भी। 
गुलाब: क्या आप यह सुनना चाहते हैं या नहीं, श्री लवेट? 84 साल हो गए हैं... और मैं अभी भी ताजा पेंट सूंघ सकता हूं। चीन का इस्तेमाल कभी नहीं किया गया था। चादरें कभी सोई नहीं गई थीं। टाइटैनिक को “द शिप ऑफ ड्रीम्स” कहा जाता था और यह था, यह वास्तव में था। 
मैन: फॉरवर्ड बर्थ वाले सभी तीसरे श्रेणी के यात्री इस तरह से, कृपया, यह कतार।चीन का इस्तेमाल कभी नहीं किया गया था। चादरें कभी सोई नहीं गई थीं। टाइटैनिक को “द शिप ऑफ ड्रीम्स” कहा जाता था और यह था, यह वास्तव में था। 
```

Here, the movie character :"Rose" was translated to "Gulaab" in hindi. While it means the same (Gulaab tranlsated to Rose flower), the context as a person is lost here.


## Solution

This sample addresses the above concerns using custom workflow where the translation is customized to improve accuracy. The below 2 approaches are discussed in this solution :

1. Use [Custom Terminology](https://docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html) to ensure brand names, character names, model names, and other unique content is translated exactly the way you need it, regardless of its context and the Amazon Translate algorithm’s decision. This requires the user to maintain and update the custom terminology file
2. Use Comprehend to detect entities/PII data and apply tags/angular braces to avoid translation of specific terms.



## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

