# The ML Podcaster's Secret: Leveraging Finetuned GPT-2 for Audio Productions

## Abstract
In recent times, audio generation has gained significant popularity and relevance due to its ability to deliver engaging and immersive content experiences. With the advancement of technology, including the application of finetuned GPT models, audio generation has become an effective tool for creating text-based content specifically tailored for podcasts. By leveraging these models, content creators can generate podcast scripts, dialogues, and narratives that are optimized for spoken delivery, enhancing the overall quality and appeal of their audio productions. This allows for efficient and streamlined podcast creation, enabling creators to focus on crafting compelling stories and discussions while maximizing the potential of their audio platforms.
## Dataset 

This dataset is created by applying whisper to the videos of the Youtube channel Lex Fridman Podcast. The dataset was created a medium size whisper model.


Data Fields

The dataset is composed by:

id: Id of the youtube video.

channel: Name of the channel.

channel_id: Id of the youtube channel.

title: Title given to the video.

categories: Category of the video.

description: Description added by the author.

text: Whole transcript of the video.

segments: A list with the time and transcription of the video.

start: When started the trancription.

end: When the transcription ends.

text: The text of the transcription.

Source Hugging Face : https://huggingface.co/datasets/Whispering-GPT/lex-fridman-podcast

## Models

GPT2-Simple - Foundational Model

GPT2 Finetuned - We have Fine-tuned the Foundational Model using the Dataset of Lex Fridman Podcast. We have experimented with models 124M and 774M of GPT2.

**Finetuned Model Link:** https://drive.google.com/file/d/1oxuiNOPsU4XT286Jlpl-ZypkI_pwc9WQ/view?usp=share_link

GPT 3.5 Turbo -  is used to provide a character summary with names and attributes, as well as the text in a manuscript format. The character attributes are then compared with the attributes from a set of ElevenLabs voices

ElevanLabs TTS - The most appropriate voice is chosen for each character. The transcribed text is then read line by line using Text-to-Speech(TTS) by either the narrator or the character who is speaking.

## Metrics Used

Bleu Score : 0.03

## Experiments
We Have experimented with two datasets:

Hugging Face - 

Source: https://huggingface.co/datasets/Whispering-GPT/lex-fridman-podcast

Colab Link: 

We opted for this dataset as it was podcast data. Using this Dataset, Our models output was in conversational style which is suitable for podcast.

Harry Potter Book Series - 

Source: http://www.glozman.com/textpages.html

Colab Link: https://colab.research.google.com/drive/15w08HXqfl1gBof6GJbTk5BSfQNWrxQVJ?usp=sharing

As we both are Harry Potter fans, We initially tried this dataset. Our model results where in book style.

## Usage


Put the text you want to transcribe in input.txt, and run

python main.py --transcribe --play

You need to have both an OpenAI API key and an ElevenLabs API key. You will also need to create voices with labels used in the code such that they can be matched with the characters.

export OPENAI_API_KEY="your_openai_api_key_here"

export ELEVENLABS_API_KEY="your_elevenlabs_api_key_here"

The labels used in this project are {'sex': 'male/female', 'age': 'young/old', 'accent': 'british/american/irish/scottish/indian'}, but you can change these as you like.


You can set the narrator voice in main.py to any voice you like by giving it the voice_id.

## Options


The following options are available when running main.py:

--transcribe: Transcribes the input text and saves it to transcript.txt.


--play: Reads the transcribed text line by line using TTS.


--introduce: Provides a brief introduction of the characters using TTS.

## DeepLearningProject
Team Members:

Chaitra Bengaluru Vishweshwaraiah


Krishna Pranathi Mokshagundam
