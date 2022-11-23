## Scenario

Audio dubbing is the process of replacing the original dialogue from your video or film with new audio. Unlike Voiceover, which plays over your videos but is separate from your content, audio dubbing aims to replace the dialogue as precisely and organically as possible.

Traditional dubbing is an expensive and time-consuming process, and AI voices provide a cheap and scalable alternative to them. A typical AI workflow to dub audio/video is as mentioned below :

<br>


## Workflow

<br>

![image](https://user-images.githubusercontent.com/32926625/203485943-7cc84c9b-2b1f-4480-85b8-f026918d49bd.png)

<br>


1. End users/clients fire requests to dub a audio/video file from Soruce language (abc) to a Target language (xyz) where (abc,xyz) is known as the language pair.
2. [Amazon Transcribe](https://aws.amazon.com/transcribe/) is used to convert the audio to text. Amazon Transcribe is an automatic speech recognition (ASR) service that makes it easy for developers to add speech to text capability to their applications.
3. [Amazon Translate](https://aws.amazon.com/translate/) is a text translation service that uses advanced machine learning technologies to provide high-quality translation on demand. Amazon Translate is used to translate the transcription from step 2 from source language "abc" to target language "xyz".
4. [Amazon Polly](https://aws.amazon.com/polly/) converts the translated text into life-like speech.





## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

