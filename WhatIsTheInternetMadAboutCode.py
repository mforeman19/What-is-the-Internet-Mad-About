# Hailey Ross, Matthew Foreman, and Charlie Trochlil
# What is the Internet Mad About?
# STAT 1559 Final Project

##FROM THE AUTHOR##
# Hello! This code is open source, and I hope it helps in some way towards what you are doing.
# This is most certainly code from beginners in Python, and this happens to be one of the first projects
# I posted on Github. Let it be known that I am not responsible for anything bad that occurs as a
# result of your actions. 

##BACKGROUND##
# This is part of a 2018 statistics project done to analyze tweets from a dataset retrieved from Twitter.
# This portion of the project was done by me, Matthew Foreman, and is on the tweets that
# contain "love" or "loving" as well as the proportion of tweets that were quotes/retweets
# and the proportion of tweets that contain profanity.
# The full report can be found on the GitHub repository. It includes figures for tweets that contain 'hate'
# as well.

import pandas as pd
import json

#################################################
# Following code opens tweet data and places into list

tweetlist = []
for line in open('ultimate.txt', 'r'): # Open the file of tweets
    if line.count('[') > 0:
        tweetlist.append(json.loads(line))

shorties = []
for tweet in tweetlist:
    if tweet['text'].endswith('…'): #ignores tweets that end with ... in the data set
        pass
    else:
        shorties.append(tweet)
        
#################################################
# Following code gets tweets from short list that contain 'love' or 'loving' and appends into a list
emptyboi = []
for tweet in shorties:
    if 'love' in tweet['text']:
        emptyboi.append(tweet['text'])
    elif 'loving' in tweet['text']:
        emptyboi.append(tweet['text'])
        

a1 = emptyboi #gets love tweets
a2 = shorties
phat = (len(a1)/(len(a2))) #phat gets the proportion of true values 
n = len(a2) #n gets length of sheet
lcl = phat - 1.96*(phat*(1-phat)/n)**0.5
ucl = phat + 1.96*(phat*(1-phat)/n)**0.5
print('(lcl and ucl): love w/ short list:', [lcl, ucl])

# Following code that gets tweets from long list that contain 'love' or 'loving' and appends into a list
emptyboi = []
for tweet in tweetlist:
    if 'love' in tweet['text']:
        emptyboi.append(tweet['text'])
    elif 'loving' in tweet['text']:
        emptyboi.append(tweet['text'])
        

a1 = emptyboi #gets love tweets
a2 = tweetlist
phat = (len(a1)/(len(a2))) #phat gets the proportion of true values 
n = len(a2) #n gets length of sheet
lcl = phat - 1.96*(phat*(1-phat)/n)**0.5
ucl = phat + 1.96*(phat*(1-phat)/n)**0.5
print('(lcl and ucl): Love & Hate w/ full list:', [lcl, ucl]) 

#################################################
#Following gets quotes or retweets from short list
emptyboi = []
for tweet in shorties:
    if (tweet['is_quote_status'] == True) or ('retweeted_status' in tweet):
        emptyboi.append(tweet['text'])

#Following finds proportion of quotes/retweets in short list set
a1 = emptyboi
a2 = shorties
phat = (len(a1)/(len(a2))) #phat gets the proportion of true values 
n = len(a2) #n gets length of sheet
lcl = phat - 1.96*(phat*(1-phat)/n)**0.5
ucl = phat + 1.96*(phat*(1-phat)/n)**0.5
print('(lcl and ucl): Retweets/Quotes w/ short list:', [lcl, ucl])   

#Following gets quotes or retweets from long list
emptyboi = []
for tweet in tweetlist:
    if (tweet['is_quote_status'] == True) or ('retweeted_status' in tweet):
        emptyboi.append(tweet['text'])

#Following finds proportion of quotes/retweets in long list set
a1 = emptyboi #gets love retweets % quotes
a2 = tweetlist
phat = (len(a1)/(len(a2))) #phat gets the proportion of true values 
n = len(a2) #n gets length of sheet
lcl = phat - 1.96*(phat*(1-phat)/n)**0.5
ucl = phat + 1.96*(phat*(1-phat)/n)**0.5
print('(lcl and ucl): Retweets/Quotes w/ full list:', [lcl, ucl])    

#################################################
#Following returns tweets that had sensitive material in short list

emptyboi = []
for tweet in shorties:
    if 'possibly_sensitive' in tweet:
        if tweet['possibly_sensitive'] == True:
            emptyboi.append(tweet['text'])


a1 = emptyboi
a2 = shorties
phat = (len(a1)/(len(a2))) #phat gets the proportion of true values 
n = len(a2) #n gets length of sheet
lcl = phat - 1.96*(phat*(1-phat)/n)**0.5
ucl = phat + 1.96*(phat*(1-phat)/n)**0.5
print('(lcl and ucl): Sensitive Material w/ short list:', [lcl, ucl])

#Following returns tweets that had sensitive material in long list
emptyboi = []
for tweet in tweetlist:
    if 'possibly_sensitive' in tweet:
        if tweet['possibly_sensitive'] == True:
            emptyboi.append(tweet['text'])


a1 = emptyboi
a2 = tweetlist
phat = (len(a1)/(len(a2))) #phat gets the proportion of true values 
n = len(a2) #n gets length of sheet
lcl = phat - 1.96*(phat*(1-phat)/n)**0.5
ucl = phat + 1.96*(phat*(1-phat)/n)**0.5
print('(lcl and ucl): Sensitive Material w/ full list:', [lcl, ucl]) 

#################################################
# Following code was experimental for the project. It ultimately did not get used.
emptyboi2 = []
for tweet in tweetlist:
    emptyboi2.append(tweet['text'])


emptyboi2 = pd.Series(emptyboi2) 
emptyboi2 = emptyboi2.str.split("hate")

emptyboi2 = emptyboi2.str[1]
emptyboi2 = emptyboi2.dropna(how='all')
emptyboi2 = emptyboi2.str.replace(":", "") #removes :
emptyboi2 = emptyboi2.str.replace(",", "")
emptyboi2 = emptyboi2.str.replace(".", "")
emptyboi2 = emptyboi2.str.split(" ")
emptyboi2 = emptyboi2.str[1:3]

emptynoob = emptyboi2.str[0:1]
emptynoob2 = emptyboi2.str[1:2]

emptyboi2 = emptyboi2.sort_index()
bb = ['First Word', 'Second Word']


n = len(emptyboi2)
for x in emptyboi2.index:
    sentence = emptyboi2[x]
    sentence = " ".join(sentence)
    sentence = sentence.replace(":", "") #removes :
    sentence = sentence.replace(",", "")
    sentence = sentence.replace(".", "")
    sentence = sentence.replace("'", "")
    emptyboi2[x] = sentence
    
emptyboi2 = emptyboi2.value_counts()


for x in emptynoob.index:
    sentence = emptynoob[x]
    sentence = "".join(sentence)
    emptynoob[x] = sentence

for x in emptynoob2.index:
    sentence = emptynoob2[x]
    sentence = "".join(sentence)
    emptynoob2[x] = sentence
    
emptynoob = emptynoob.value_counts()
emptynoob2 = emptynoob2.value_counts()

print(emptyboi2[0:12])
emptyboi2.to_csv('twowords.csv')
print(emptyboi2[emptyboi2 > 10])

print(emptynoob[0:13])
emptynoob.to_csv('firstword.csv')
print(emptynoob2[0:20])
emptynoob2.to_csv('secondword.csv')

        
            
