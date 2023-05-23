# The ML Podcaster's Secret: Leveraging Finetuned GPT-2 for Audio Productions

## Abstract
In recent times, audio generation has gained significant popularity and relevance due to its ability to deliver engaging and immersive content experiences. With the advancement of technology, including the application of finetuned GPT models, audio generation has become an effective tool for creating text-based content specifically tailored for podcasts. By leveraging these models, content creators can generate podcast scripts, dialogues, and narratives that are optimized for spoken delivery, enhancing the overall quality and appeal of their audio productions. This allows for efficient and streamlined podcast creation, enabling creators to focus on crafting compelling stories and discussions while maximizing the potential of their audio platforms.

data:image/png;base64,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

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

Demo Link: https://drive.google.com/file/d/1K2OzUlGg5MaJq_mvXKl-xQdXzp4k7Ye6/view?usp=sharing
