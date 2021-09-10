from flask import Flask,request,redirect,url_for,jsonify,render_template
import pandas as pd
from firebase_admin import credentials, firestore, initialize_app,storage
import json
import requests
from firebase import firebase
import datetime
import urllib
 

#AUDIO
import glob  
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import librosa  
import numpy as np  
# from keras.models import load_model 

#TEXT
import speech_recognition as s
import gensim
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300-SLIM.bin', binary=True) 
# print(model.most_similar('hello'))#Create model from word2vec file 
import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize

#MAP
import gmplot

#IMAGE
import shutil

# Warnings



app = Flask(__name__)
# db = firestore.client()
config = {
  "apiKey": "AIzaSyAT6S-AHV2t23r2spbgxSHZ-9T0moDAdMM",    #Gcloud-apikey
  "authDomain": "unisys-a75c1.firebaseapp.com",           #firestore-auth-Domain
  "databaseURL": "https://unisys-a75c1.firebaseio.com",   #firestore-database-url
  "projectId": "unisys-a75c1",                            #gcloud / firestore
  "storageBucket": "unisys-a75c1.appspot.com",            #gcloud
  "messagingSenderId": "919856881921",                    #firestore
  "appId": "1:919856881921:web:1c02fb82f68fce0d147b00"    #firestore
}

cred = credentials.Certificate("unisys-key.json")
default_app = initialize_app(cred)
bucket = storage.bucket(name="unisys-a75c1.appspot.com")
db = firestore.client()

# @title keywords
keywords = [
'UNCONSCIOUS',
'NUMBNESS',
'PARALYSIS',
'health',
 'government',
 'exigency',
 'natural',
 'disaster',
 'life',
 'rescue',
 'property',
 'pinch',
 'flood',
 'parking',
 'brake',
 'emergency',
 'brake',
 'hand',
 'brake',
 'crisis',
 'relief',
 'evacuation',
 'aid',
 'assistance',
 'alert',
 'disaster',
 'medical',
 'personnel',
 'standby',
 'shelter',
 'emergency',
 'service',
 'hospital',
 'dispatch',
 'coronavirus',
 'fever',

 'power',
 'outage',
 'ambulance',
 'brake',
 'human',
 'stroke',
 'mumps',
 'ocd',
 'vd',
 'anthrax',
 'malaria',
 'overdose',
 'tornado',
 'scabies',
 'hurricane',
 'monitoring',
 'mal',
 'security',
 'temporary',
 'hiv',
 'provide',
 'catastrophe',
 'calamity',
 'tragedy',
 'tsunami',
 'famine',
 'devastation',
 'earthquake',
 'hardship',
 'cataclysm',
 'hurricane',
 'destruction',
 'damage',
 'accident',
 'misfortune',
 'flood',
 'adversity',
 'drought',
 'meltdown',
 'apocalypse',
 'plague',
 'visitation',
 'catastrophic',
 'bad',
 'luck',
 'power',
 'outage',
 'spill',
 'emergency',
 'tidal',
 'wave',
 'aftermath',
 'quake',
 'rescue',
 'relief',
 'katrina',
 'emergencies',
 'crisis',
 'floods',
 'danger',
 'crash',
 'RELATED',
 'WORDS',
 'CONTINUE',
 'AFTER',
 'ADVERTISEMENT',
 'wreck',
 'explosion',
 'preparedness',
 'storm',
 'cleanup',
 'failures',
 'collapse',
 'rebuilding',
 'nightmare',
 'haiti',
 'havoc',
 'flooding',
 'evacuation',
 'aid',
 'outbreak',
 'landslide',
 'mishap',
 'trauma',
 'mudslide',
 'tornado',
 'avalanche',
 'cold',
 'disease',
 'gdp',
 'fire',
 'disasters',
 'devastating',
 'hail',
 'worst',
 'impact',
 'heat',
 'massive',
 'deluge',
 'flash',
 'flood',
 'tsunami',
 'river',
 'water',
 'inundate',
 'stream',
 'swamp',
 'tide',
 'torrent',
 'inundation',
 'levee',
 'floodplain',
 'overflow',
 'flow',
 'lake',
 'erosion',
 'monsoon',
 'dam',
 'drainage',
 'earthquake',
 'hydrograph',
 'fill',
 'landslide',
 'flowage',
 'reservoir',
 'torrential',
 'fill',
 'up',
 'drainage',
 'basin',
 'debacle',
 'outpouring',
 'oversupply',
 'floodlight',
 'photoflood',
 'irrigation',
 'wind',
 'flood',
 'lamp',
 'evacuation',
 'fertility',
 '100-year',
 'flood',
 'flashflood',
 'freshet',
 'ice',
 'dam',
 'downpour',
 'rains',
 'storm',
 'seepage',
 'thunderstorm',
 'disaster',
 'arroyo',
 'landslides',
 'hurricane',
 'floodwaters',
 'rivers',
 'floodwater',
 'devastation',
 'watercourse',
 'comfort',
 'assistance',
 'aid',
 'help',
 'respite',
 'alleviation',
 'succor',
 'ease',
 'assist',
 'succour',
 'solace',
 'reprieve',
 'sculpture',
 'stucco',
 'consolation',
 'monumental',
 'sculpture',
 'rock',
 'relief',
 'easement',
 'social',
 'welfare',
 'moderation',
 'backup',
 'rest',
 'ministration',
 'easing',
 'substitute',
 'reliever',
 'stand-in',
 'fill-in',
 'assuagement',
 'relievo',
 'embossment',
 'rilievo',
 'backup',
 'man',
 'rest',
 'period',
 'bronze',
 'casting',
 'liberalization',
 'comfortableness',
 'benefit',
 'emergency',
 'reconstruction',
 'disaster',
 'rescue',
 'protection',
 'rebuilding',
 'shelter',
 'ancient',
 'near',
 'east',
 'recovery',
 'support',
 'rehabilitation',
 'response',
 'italian',
 'language',
 'victims',
 'suicide',
 'life',
 'end',
 'afterlife',
 'dying',
 'funeral',
 'demise',
 'decease',
 'disease',
 'murder',
 'burial',
 'brain',
 'death',
 'heart',
 'state',
 'fatality',
 'grim',
 'reaper',
 'extinction',
 'killing',
 'autopsy',
 'homicide',
 'martyrdom',
 'accident',
 'reincarnation',
 'destruction',
 'cremation',
 'senescence',
 'organism',
 'cardiac',
 'arrest',
 'ending',
 'ritual',
 'megadeath',
 'reaper',
 'necrosis',
 'necrobiosis',
 'dead',
 'necrophobia',
 'medicine',
 'fatal',
 'last',
 'organic',
 'phenomenon',
 'cell',
 'death',
 'starvation',
 'malnutrition',
 'grave',
 'azrael',
 'decomposition',
 'mortality',
 'commit',
 'suicide',
 'death',
 'hurt',
 'maim',
 'harm',
 'traumatize',
 'humiliate',
 'bruise',
 'wound',
 'concuss',
 'incapacitate',
 'mutilate',
 'injury',
 'damage',
 'blunt',
 'trauma',
 'corona',
 'symptoms',
 'diss',
 'lacerate',
 'offend',
 'insult',
 'spite',
 'shock',
 'stab',
 'calk',
 'provoke',
 'trample',
 'falling',
 'traumatise',
 'penetrating',
 'trauma',
 'trauma',
 'center',
 'terrorize',
 'kill',
 'sicken',
 'frighten',
 'inflict',
 'immobilize',
 'demoralize',
 'decapitate',
 'intimidate',
 'punish',
 'retaliate',
 'terrify',
 'endanger',
 'harass',
 'deprive',
 'suffocate',
 'drown',
 'electrocute',
 'disfigure',
 'victimize',
 'impair',
 'empty',
 'void',
 'eliminate',
 'expel',
 'withdraw',
 'relocate',
 'move',
 'evacuation',
 'displace',
 'stranded',
 'flee',
 'arrive',
 'resettle',
 'rescue',
 'airlifted',
 'displaced',
 'marooned',
 'vacate',
 'trapped',
 'leave',
 'flooded',
 'disembark',
 'evict',
 'panicked',
 'alert',
 'redeploy',
 'eject',
 'emigrate',
 'excrete',
 'pass',
 'suction',
 'evacuated',
 'evacuating',
 'vacant',
 'egest',
 'removal',
 'evacuees',
 'remove',
 'shelters',
 'remover',
 'refugees',
 'shelter',
 'evacuations',
 'survivors',
 'residents',
 'reinforcements',
 'peacekeepers',
 'vehicle',
 'hospital',
 'helicopter',
 'automobile',
 'paramedic',
 'bus',
 'van',
 'taxi',
 'medevac',
 'cab',
 'car',
 'motorcar',
 'auto',
 'paramedics',
 'medic',
 'emergency',
 'rescue',
 'toyota',
 'siren',
 'dispatcher',
 'stretcher',
 'firemen',
 'firefighters',
 'escort',
 'ferry',
 'evacuation',
 'minibus',
 'nurse',
 'medics',
 'morgue',
 'police',
 'rescuers',
 'sirens',
 'motorcycle',
 'ambulance',
 'limousine',
 'triage',
 'hospital',
 'ship',
 'truck',
 'firefighter',
 'ford',
 'police',
 'car',
 'emergency',
 'vehicle',
 'equipment',
 'illness',
 'injury',
 'latin',
 'machine',
 'military',
 'cart',
 'disaster',
 'car',
 'accident',
 'portugal',
 'industrialization',
 'fuel',
 'ambulances',
 'fly-car',
 'dispatch',
 'electronics',
 'nissan']
#end region

# text priority
def textPriority(text1):
  text=list(text1.values())
  inde=list(text1.keys())
  data=text
  pos = nltk.pos_tag(text)
  #print(pos)
  wanted_tags = ['NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
  pos_tags = [item for item in pos if item[1] in wanted_tags]
  nv_words = []
  for item in pos_tags:
    nv_words.append(item[0])
  # print(nv_words)

  #declaring variables
  max_avg = 0
  max_label = ''
  sum_cos = 0 
  dict={}
  count = 0
  labelswords = []
  word_call_list = []
  labelswords2 = []
  exit = 'false'
  ind=0
  for call in data:  #for each call in the dataset
    
    call_tokens = word_tokenize(call)  #
    call_pos = nltk.pos_tag(call_tokens) #finds the pos and stores it in a list
    call_words = [item[0].lower() for item in call_pos if item[1] in wanted_tags]
    #print(call_words)
    sum_cos = 0
    count = 0
    exit = 'false'
    max_label = ''
    max_avg = 0
    max_avg_1 = 0
    kc = 0
    for word_call in call_words:
      word_call_list = []
      for labels in keywords:
        labels = word_tokenize(labels)
        labelswords = []
        count = 0
        sum_cos = 0
        for word_mpds in labels:
          if word_mpds.isalpha() and word_mpds != '>' and word_mpds != 'of' and word_mpds != 'and' and word_mpds != 'a'and word_mpds != 'monixide':
            labelswords.append(word_mpds.lower())
        word_call_list.append(word_call)
        common = set(labelswords).intersection(set(word_call_list))
        if len(common) > 0:
          max_label = labels 
          kc+=1
          exit = 'true'
        else:
          for word_mpds in labels:
            try:
              callcorrelation = model.similarity(word_call, word_mpds.lower())
              if callcorrelation > 0.2 or callcorrelation < -0.2: 
                sum_cos += callcorrelation
                count += 1
            except KeyError:
              continue  
        if count == 0:
          count = 1
        avg = sum_cos/count
        
        if avg >= max_avg:
          max_avg = avg
          max_label = labels
        if exit == 'true':
          break
    #print('Matching label for ', call, 'is ', max_label)
    # print (max_avg)
    if (kc==0):
          kc=0.5
    max_avg_1 = max_avg*kc
    # print(kc)
    dict[inde[ind]]=max_avg_1
    ind =ind+1
    #print(dict)
  return dict

#NEW TEXT PRIORITY

def extPriority(text1):
  text=list(text1.values())
  inde = list(text1.keys())
  data=text
  pos = nltk.pos_tag(text)
  #print(pos)
  wanted_tags = ['NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
  pos_tags = [item for item in pos if item[1] in wanted_tags]
  nv_words = []
  for item in pos_tags:
    nv_words.append(item[0])
  # print(nv_words)

  #declaring variables
  max_avg = 0
  max_label = ''
  sum_cos = 0 
  dict={}
  count = 0
  labelswords = []
  word_call_list = []
  labelswords2 = []
  exit = 'false'
  ind=0
  for call in data:  #for each call in the dataset
    
    call_tokens = word_tokenize(call)  #
    call_pos = nltk.pos_tag(call_tokens) #finds the pos and stores it in a list
    call_words = [item[0].lower() for item in call_pos if item[1] in wanted_tags]
    # print(call_words)
    sum_cos = 0
    count = 0
    exit = 'false'
    max_label = ''
    labelswords = []
    max_avg = 0
    max_avg1 = 0
    kcount=0
    for word_call in call_words:
      
      word_call_list = []
      for labels in keywords:
        #print("Hey")
        labels = word_tokenize(labels)
        
        count = 0
        sum_cos = 0
        #print(labels)
        for word_mpds in labels:
          if word_mpds.isalpha() and word_mpds != '>' and word_mpds != 'of' and word_mpds != 'and' and word_mpds != 'a'and word_mpds != 'monixide':
            labelswords.append(word_mpds.lower())
        word_call_list.append(word_call)
        

        common = set(labelswords).intersection(set(word_call_list))
        
        if len(common) > 0:
          max_label = labels
          kcount+=1 
          exit = 'true'
        else:
          for word_mpds in labels:
            try:
              callcorrelation = model.similarity(word_call, word_mpds.lower())
              if callcorrelation > 0.2 or callcorrelation < -0.2: 
                sum_cos += callcorrelation
                count += 1
            except KeyError:
              continue  
        if count == 0:
          count = 1
        avg = sum_cos/count
        
        if avg >= max_avg:
          max_avg = avg
          
          max_label = labels
        if exit == 'true':
          break
      #print('Matching label for ', call, 'is ', max_label)
    
        
    # print(labelswords)
    # print(common)
    if(kcount==0):
      kcount=0.5
    max_avg1=max_avg*kcount
    
    # print(max_avg,kcount,max_avg*kcount)
          
    dict[inde[ind]]=max_avg1
    ind =ind+1
    #print(dict)
  return dict

#text1={1:"There is an emergency near me, people are stranded, please provide relief and rescue us.",2:"There is a crash between 2 cars"}






emotions=['neutral', 'calm', 'happy', 'sad', 'angry', 'fearful', 'disgust', 'surprised']
pred_list = {}
document = {}
#Audio features
def extract_feature(file_name): 
    X, sample_rate = librosa.load(file_name)
    stft = np.abs(librosa.stft(X))
    mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T,axis=0)
    chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
    mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
    contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T,axis=0)
    tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X),
    sr=sample_rate).T,axis=0)
    return mfccs,chroma,mel,contrast,tonnetz


@app.route('/pred',methods=['POST','GET'])
def pred():
        d ={}
        url_d = {}
        # df = {}
        ref = db.collection('users')
        docs = ref.stream()
        for doc in docs:
              img = 'images/'+doc.id
              b = bucket.blob(img)
              # print(b)
              url =  b.generate_signed_url(datetime.timedelta(seconds=300),method='GET')
              url_d[doc.id] = url
              # img = 'images/'+'corona.jpg'
              # print(url)
            # r = requests.get(url,stream=True)
            # local = open(doc.id+'.jpg', 'wb')
            # r.raw.decode_content = True
            # shutil.copyfileobj(r.raw,local)


        d = extPriority(document)
        # print(d);
        # a = bucket.blob('text')
        # url =  a.generate_signed_url(datetime.timedelta(seconds=300),method='GET')
        # +0.2*pred_list[id]
        for id in d.keys():
              d[id] = d[id]
        # print(d)
        # print(sorted(d.items(), key= lambda x:x[1],reverse=True))
        df = sorted(d.items(), key= lambda x:x[1],reverse=True)
        
        
        return render_template('a.html',df=df,document=document,url_d=url_d)

@app.route('/audio',methods=['POST','GET'])
def audio():
    
    ref = db.collection('users')
    docs = ref.stream()
    
    for doc in docs:
        # print('{}=>{}'.format(doc.id,doc.to_dict()))
        aud = 'audio/'+doc.id+'.wav'
        b = bucket.blob(aud)
        url =  b.generate_signed_url(datetime.timedelta(seconds=300),method='GET')
        r = requests.get(url,allow_redirects=True)
        open('new.wav', 'wb').write(r.content)
    # generating text
        sr = s.Recognizer()
        fn = 'new.wav'
        with s.AudioFile(fn) as src:
            audio = sr.listen(src)
            try:
                text = sr.recognize_google(audio)
            except s.UnknownValueError:
                # l = ['I am stuck in a building and it is about to collapse','There is fire in my home']
                text = 'I am stuck in a building and it is about to collapse'
            # print(text)
        document[doc.id] = text;
        # print(document)

# Extracting features
    #     model = load_model('aud.h5')
    #     features, labels = np.empty((0,193)), np.empty(0)
        
    #     mfccs, chroma, mel, contrast,tonnetz = extract_feature(fn)
    #     ext_features = np.hstack([mfccs,chroma,mel,contrast,tonnetz])
    #     features = np.vstack([features,ext_features])
    #     labels = np.append(labels, fn)
        
    #     prob = model.predict_proba(features)
    #     print(prob)
    #     prediction = (prob[0][5]*3+prob[0][3]*2+prob[0][-1])/(6)
        
    #     pred_list[doc.id] =prediction
    # print(pred_list)
    # print(document)
    return render_template('a.html',document=document)

@app.route('/plot',methods=['POST','GET'])
def plot():
      gd = {}
      lat = [13.080384,13.080384,13.080384]
      lon = [77.5319506,77.5319506,77.5319506]
      ref = db.collection('users')
      docs = ref.stream()
      for doc in docs:
            lat.append(doc.to_dict()['location']['latitude'])
            lon.append(doc.to_dict()['location']['longitude'])
      gmap1 = gmplot.GoogleMapPlotter(13.0319627,77.5642704, 13 )
      # print(lat)
      # print(lon)
      gmap1.heatmap(lat, lon)
      gmap1.draw("templates\map.html")
      
      return render_template("map.html")
      
@app.route('/tweet',methods=['GET'])
def tweet():
      ref = db.collection('users')
      docs = ref.stream()
      for doc in docs:
        img = 'images/'+doc.id
        b = bucket.blob(img)
        url =  b.generate_signed_url(datetime.timedelta(seconds=300),method='GET')
        print(url)
        r = requests.get(url,stream=True)
        local = open(doc.id+'.jpg', 'wb')
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw,local)
      return url

if __name__=='__main__':
    app.run(debug=True)
