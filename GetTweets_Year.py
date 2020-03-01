# -*- coding: utf-8 -*-
"""
Created on Thu Jan 2020

@author: jelin
"""

import GetOldTweets3 as got
import pandas as pd
import time
from os import chdir
import calendar


cal = calendar.Calendar()

chdir('D://Practicum1') #set filepath directory for this script


#Code developed from sources Giordano (2017a, 2017b).
data = pd.DataFrame(columns=[]) #create an empty Pandas dataframe
info = {} #create an empty dictionary



#begin pulling by each month, 3 sections for each key phrase as otherwise the query really just pulls the first phrase

#pull January 2019
then = time.time()

for date in cal.itermonthdates(2019, 1): #iterate through the dates including 2 days on either end
    tweetdate=date #set the date argument for the actual twitter pull command
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate change').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode") #set parameters for twitter search
    #purposefully not setting location... results are extremely limited and location seems unreliable
    tweets = got.manager.TweetManager.getTweets(tweetCriteria) #set arguement for twitter pull
    for idx, tweet in enumerate(tweets): #create the loop that will go through each day 
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date #pull 10 tweets from each day into a dictionary
        df=pd.DataFrame.from_dict(info,orient='index') #convert results into a dataframe
        data=data.append(df) #append results to the existing dataframe now that they are formatted
        
for date in cal.itermonthdates(2019, 1):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate crisis').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        
for date in cal.itermonthdates(2019, 1):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('global warming').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        data.drop_duplicates(keep='first',inplace=True)#periodically drop duplicates 
            
now = time.time()    
print("It took: ", (now-then), " seconds for January data")  #time calc to see how the script is progressing 

time.sleep(60) #sleep to stop 429 errors

#pull February 2019
then = time.time()

for date in cal.itermonthdates(2019, 2): #iterate through the dates including 2 days on either end
    tweetdate=date #set the date argument for the actual twitter pull command
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate change').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode") #set parameters for twitter search
    tweets = got.manager.TweetManager.getTweets(tweetCriteria) #set arguement for twitter pull
    for idx, tweet in enumerate(tweets): #create the loop that will go through each day 
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date #pull 10 tweets from each day into a dictionary
        df=pd.DataFrame.from_dict(info,orient='index') #convert results into a dataframe
        data=data.append(df) #append results to the existing dataframe now that they are formatted
        
for date in cal.itermonthdates(2019, 2):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate crisis').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        
for date in cal.itermonthdates(2019, 2):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('global warming').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        data.drop_duplicates(keep='first',inplace=True)#periodically drop duplicates 
            
now = time.time()    
print("It took: ", (now-then), " seconds for February data")  #time calc to see how the script is progressing 

time.sleep(60)

#pull March 2019
then = time.time()

for date in cal.itermonthdates(2019, 3): #iterate through the dates including 2 days on either end
    tweetdate=date #set the date argument for the actual twitter pull command
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate change').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode") #set parameters for twitter search
    tweets = got.manager.TweetManager.getTweets(tweetCriteria) #set arguement for twitter pull
    for idx, tweet in enumerate(tweets): #create the loop that will go through each day 
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date #pull 10 tweets from each day into a dictionary
        df=pd.DataFrame.from_dict(info,orient='index') #convert results into a dataframe
        data=data.append(df) #append results to the existing dataframe now that they are formatted
        
for date in cal.itermonthdates(2019, 3):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate crisis').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        
for date in cal.itermonthdates(2019, 3):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('global warming').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        data.drop_duplicates(keep='first',inplace=True)#periodically drop duplicates 
            
now = time.time()    
print("It took: ", (now-then), " seconds for March data")  #time calc to see how the script is progressing

time.sleep(60)

#pull April 2019
then = time.time()

for date in cal.itermonthdates(2019, 4): #iterate through the dates including 2 days on either end
    tweetdate=date #set the date argument for the actual twitter pull command
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate change').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode") #set parameters for twitter search
    tweets = got.manager.TweetManager.getTweets(tweetCriteria) #set arguement for twitter pull
    for idx, tweet in enumerate(tweets): #create the loop that will go through each day 
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date #pull 10 tweets from each day into a dictionary
        df=pd.DataFrame.from_dict(info,orient='index') #convert results into a dataframe
        data=data.append(df) #append results to the existing dataframe now that they are formatted
        
for date in cal.itermonthdates(2019, 4):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate crisis').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        
for date in cal.itermonthdates(2019, 4):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('global warming').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        data.drop_duplicates(keep='first',inplace=True)#periodically drop duplicates 
            
now = time.time()    
print("It took: ", (now-then), " seconds for April data")  #time calc to see how the script is progressing

time.sleep(60)

#pull May 2019
then = time.time()

for date in cal.itermonthdates(2019, 5): #iterate through the dates including 2 days on either end
    tweetdate=date #set the date argument for the actual twitter pull command
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate change').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode") #set parameters for twitter search
    tweets = got.manager.TweetManager.getTweets(tweetCriteria) #set arguement for twitter pull
    for idx, tweet in enumerate(tweets): #create the loop that will go through each day 
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date #pull 10 tweets from each day into a dictionary
        df=pd.DataFrame.from_dict(info,orient='index') #convert results into a dataframe
        data=data.append(df) #append results to the existing dataframe now that they are formatted
        
for date in cal.itermonthdates(2019, 5):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate crisis').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        
for date in cal.itermonthdates(2019, 5):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('global warming').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        data.drop_duplicates(keep='first',inplace=True)#periodically drop duplicates 
            
now = time.time()    
print("It took: ", (now-then), " seconds for May data")  #time calc to see how the script is progressing


time.sleep(60)

#pull June 2019
then = time.time()

for date in cal.itermonthdates(2019, 6): #iterate through the dates including 2 days on either end
    tweetdate=date #set the date argument for the actual twitter pull command
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate change').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode") #set parameters for twitter search
    tweets = got.manager.TweetManager.getTweets(tweetCriteria) #set arguement for twitter pull
    for idx, tweet in enumerate(tweets): #create the loop that will go through each day 
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date #pull 10 tweets from each day into a dictionary
        df=pd.DataFrame.from_dict(info,orient='index') #convert results into a dataframe
        data=data.append(df) #append results to the existing dataframe now that they are formatted
        
for date in cal.itermonthdates(2019, 6):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate crisis').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        
for date in cal.itermonthdates(2019, 6):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('global warming').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        data.drop_duplicates(keep='first',inplace=True)#periodically drop duplicates 
            
now = time.time()    
print("It took: ", (now-then), " seconds for June data")  #time calc to see how the script is progressing

time.sleep(60)

#pull July 2019
then = time.time()

for date in cal.itermonthdates(2019, 7): #iterate through the dates including 2 days on either end
    tweetdate=date #set the date argument for the actual twitter pull command
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate change').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode") #set parameters for twitter search
    tweets = got.manager.TweetManager.getTweets(tweetCriteria) #set arguement for twitter pull
    for idx, tweet in enumerate(tweets): #create the loop that will go through each day 
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date #pull 10 tweets from each day into a dictionary
        df=pd.DataFrame.from_dict(info,orient='index') #convert results into a dataframe
        data=data.append(df) #append results to the existing dataframe now that they are formatted
        
for date in cal.itermonthdates(2019, 7):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate crisis').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        
for date in cal.itermonthdates(2019, 7):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('global warming').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        data.drop_duplicates(keep='first',inplace=True)#periodically drop duplicates 
            
now = time.time()    
print("It took: ", (now-then), " seconds for July data")  #time calc to see how the script is progressing

time.sleep(60)

#pull August 2019
then = time.time()

for date in cal.itermonthdates(2019, 8): #iterate through the dates including 2 days on either end
    tweetdate=date #set the date argument for the actual twitter pull command
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate change').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode") #set parameters for twitter search
    tweets = got.manager.TweetManager.getTweets(tweetCriteria) #set arguement for twitter pull
    for idx, tweet in enumerate(tweets): #create the loop that will go through each day 
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date #pull 10 tweets from each day into a dictionary
        df=pd.DataFrame.from_dict(info,orient='index') #convert results into a dataframe
        data=data.append(df) #append results to the existing dataframe now that they are formatted
        
for date in cal.itermonthdates(2019, 8):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate crisis').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        
for date in cal.itermonthdates(2019, 8):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('global warming').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        data.drop_duplicates(keep='first',inplace=True)#periodically drop duplicates 
            
now = time.time()    
print("It took: ", (now-then), " seconds for August data")  #time calc to see how the script is progressing

time.sleep(60)

#pull September 2019
then = time.time()

for date in cal.itermonthdates(2019, 9): #iterate through the dates including 2 days on either end
    tweetdate=date #set the date argument for the actual twitter pull command
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate change').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode") #set parameters for twitter search
    tweets = got.manager.TweetManager.getTweets(tweetCriteria) #set arguement for twitter pull
    for idx, tweet in enumerate(tweets): #create the loop that will go through each day 
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date #pull 10 tweets from each day into a dictionary
        df=pd.DataFrame.from_dict(info,orient='index') #convert results into a dataframe
        data=data.append(df) #append results to the existing dataframe now that they are formatted
        
for date in cal.itermonthdates(2019, 9):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate crisis').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        
for date in cal.itermonthdates(2019, 9):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('global warming').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        data.drop_duplicates(keep='first',inplace=True)#periodically drop duplicates 
            
now = time.time()    
print("It took: ", (now-then), " seconds for September data")  #time calc to see how the script is progressing

time.sleep(60)

#pull October 2019
then = time.time()

for date in cal.itermonthdates(2019, 10): #iterate through the dates including 2 days on either end
    tweetdate=date #set the date argument for the actual twitter pull command
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate change').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode") #set parameters for twitter search
    tweets = got.manager.TweetManager.getTweets(tweetCriteria) #set arguement for twitter pull
    for idx, tweet in enumerate(tweets): #create the loop that will go through each day 
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date #pull 10 tweets from each day into a dictionary
        df=pd.DataFrame.from_dict(info,orient='index') #convert results into a dataframe
        data=data.append(df) #append results to the existing dataframe now that they are formatted
        
for date in cal.itermonthdates(2019, 10):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate crisis').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        
for date in cal.itermonthdates(2019, 10):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('global warming').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        data.drop_duplicates(keep='first',inplace=True)#periodically drop duplicates 
            
now = time.time()    
print("It took: ", (now-then), " seconds for October data")  #time calc to see how the script is progressing

time.sleep(60)

#pull November 2019
then = time.time()

for date in cal.itermonthdates(2019, 11): #iterate through the dates including 2 days on either end
    tweetdate=date #set the date argument for the actual twitter pull command
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate change').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode") #set parameters for twitter search
    tweets = got.manager.TweetManager.getTweets(tweetCriteria) #set arguement for twitter pull
    for idx, tweet in enumerate(tweets): #create the loop that will go through each day 
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date #pull 10 tweets from each day into a dictionary
        df=pd.DataFrame.from_dict(info,orient='index') #convert results into a dataframe
        data=data.append(df) #append results to the existing dataframe now that they are formatted
        
for date in cal.itermonthdates(2019, 11):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate crisis').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        
for date in cal.itermonthdates(2019, 11):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('global warming').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        data.drop_duplicates(keep='first',inplace=True)#periodically drop duplicates 
            
now = time.time()    
print("It took: ", (now-then), " seconds for November data")  #time calc to see how the script is progressing

time.sleep(60)

#pull December 2019
then = time.time()

for date in cal.itermonthdates(2019, 12): #iterate through the dates including 2 days on either end
    tweetdate=date #set the date argument for the actual twitter pull command
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate change').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode") #set parameters for twitter search
    tweets = got.manager.TweetManager.getTweets(tweetCriteria) #set arguement for twitter pull
    for idx, tweet in enumerate(tweets): #create the loop that will go through each day 
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date #pull 10 tweets from each day into a dictionary
        df=pd.DataFrame.from_dict(info,orient='index') #convert results into a dataframe
        data=data.append(df) #append results to the existing dataframe now that they are formatted
        
for date in cal.itermonthdates(2019, 12):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('climate crisis').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        
for date in cal.itermonthdates(2019, 12):
    tweetdate=date
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('global warming').setUntil(str(tweetdate)).setMaxTweets(10).setEmoji("unicode")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    for idx, tweet in enumerate(tweets):
        info[idx] = tweet.id, tweet.username, tweet.text, tweet.date
        df=pd.DataFrame.from_dict(info,orient='index')
        data=data.append(df)
        data.drop_duplicates(keep='first',inplace=True)#periodically drop duplicates 
            
now = time.time()    
print("It took: ", (now-then), " seconds for December data")  #time calc to see how the script is progressing

data.to_csv('D:/Practicum1/tweets.csv')

print('Complete!')
          
