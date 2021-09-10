# IDA-README

---------------------------------------------------------------------------------------------------

# Natural Language Processing for Text Analysis of Call Transcript and Tweet.


The text is prioritized using TF-IDF, Page Ranking, Cosine Similarity using steps:

### Pre-Processing-> TF-IDF Matrix -> Similarity Semantics -> Page ranking.

The tweets are prioritized using Integer Linear Programming methods like Primal and Dual, and using library such as 
### Textacy, Spacy, NLTK, PyMathProg. 
Tweet Summarization is Achieved in 3 steps:

#### 1.I want the total length of all the selected tweets to be less than some value L

#### 2.If I pick some content word (out of my possible content words) , then I want to have at least
#### one tweet from the set of tweets which contain that content word, .

#### 3.If I pick some tweet i (out of my possible tweets) , then all the content words in that tweet are also selected.

---------------------------------------------------------------------------------------------------

Audio is sent to DEEP-LEARNING 7-LAYERED DNN Model , which considers spectrogram of the
audio and uses the Librosa library for classifying the particular emotions Angry, Sad, Disgust,
Surprised, and a testing accuracy of 75%.

The calls are classified based on following features in our DL Model:

### MelSpectrogram, MFCC, Spectral-Contrast, Chroma,Tonnetz

The text is prioritized using TF-IDF, Page Ranking, Cosine Similarity using steps:

---------------------------------------------------------------------------------------------------

# IDA Mobile Cross Platform Application

## Project Theme

#### Domain: Data Analytics Using Machine Learning and AI/Cognitive Solutions Using Deep Learning

A B2C AI model, which can tackle large volumes of information during calamities, assist the relief committee and prioritize the information accurately, reducing the response time and damages. 

Enhanced multi-level precedence and pre-emption based priority relief routing should be implemented in India along with the option to pre-empt ongoing services, if needed in order to ensure efficacy.

### Screenshots

![image](https://user-images.githubusercontent.com/43045825/82894026-9187be00-9f6f-11ea-87bf-228a856f37fb.png)
------------------------------------------------------------------------------------------------------
![Workflow (1)](https://user-images.githubusercontent.com/43045825/82894103-aa906f00-9f6f-11ea-9bf8-0b435c491c94.png)
------------------------------------------------------------------------------------------------------
![WhatsApp Image 2020-04-23 at 10 21 34 PM](https://user-images.githubusercontent.com/43045825/82894142-bbd97b80-9f6f-11ea-8492-405f3c867dda.jpeg)
------------------------------------------------------------------------------------------------------
![WhatsApp Image 2020-04-23 at 10 21 32 PM](https://user-images.githubusercontent.com/43045825/82894145-bd0aa880-9f6f-11ea-9f21-239454595b3e.jpeg)
------------------------------------------------------------------------------------------------------

## Benefits and Business Use-case

#### USER SELLING POINTS : 

No existing solution provides this:
B2C AI solution involving multiple-sources, i.e. Call, Text, Image, Location, Tweets.
Obtaining Information from NO/ LOW-NETWORK AREAS.
Multilingual call recording facilitation for non-English speakers.
Inclusion of Prioritized Tweets from RealTime data from Twitter.
Minimalistic, Easy-To-Use Interface in just 3 steps to avoid panic.

#### Business scalability:

Can be adopted by Govt. and Helpline committee for ease in services.
Will help to reproduce the loss of revenue faced by helpline by pre-empting less important calls.
Can be scaled to all the disasters and also to fire emergencies, blasts, accidents, pandemics.
It can be adopted by hospitals, ambulances for effective routing and addressing during time of serious mishaps.

---------------------------------------------------------------------------------------------------

## Details to run the project

#### TO RUN THE FLUTTER MOBILE APP

Step 1 − Go to URL, https://flutter.dev/docs/get-started/install/windows and download the latest Flutter SDK. As of April 2019, the version is 1.2.1 and the file is flutter_windows_v1.2.1-stable.zip.

Step 2 − Unzip the zip archive in a folder, say C:\flutter\

Step 3 − Update the system path to include flutter bin directory.

Step 4 − Flutter provides a tool, flutter doctor to check that all the requirement of flutter development is met.

Step 5 - flutter run (command to run the app)

#### TO RUN THE WEB APP
Step 1 - Go to URL, https://github.com/IDA-Caffeine-Overflow/IDA-Website.git and download the repository.

Step 2 - Make sure Python 3.7.* is installed and path is mentioned in the environment variables.

Step 3 - Please install all the required packages present in Requirements.txt using pip.

          #For example 
              pip install librosa

Step 4 - To start the server use the below command.
              
              ##python3 server.py
