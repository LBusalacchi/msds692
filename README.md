# MSDS692 Practicum 1 - Australian Bushfire Sentiment Analysis


In the second half of the year, the massive scope of the Australian Bushfire captured climate news headlines worldwide, and eventually reached the front page of most major news outlets. Climate change has long been a hot button issue, but the rhetoric around it certainly seemed to reach new heights with this latest crisis. However, did the event really change how people felt about climate change? This project takes an initial look at the sentiment of tweets using key climate phrases, in relation to the key dates of the Australian Bushfire crisis.
For high level technical details, please continue to read below. For an executive summary, please see the video posted [here](https://youtu.be/XOjmVZ7xUg4).

## Data Gathering
The first step in our process to understanding the potential changes in sentiment are gather data. For this analysis we will be using tweets that contain the key phrases “climate change”, “climate crisis”, and “global warming”. These phrases are often used interchangeably, though those familiar with the subject but say “global warming” is a misnomer for the predicted changes. However, it is still widely used and is certain to be used with numerous tweets related to bushfires or wildfires in general. 
In order to pull this information, we will use the Python package ‘GetOldTweets3’ by Jefferson Henrique, which acts as a webscraper to pull key phrases within the indicated parameters (Mottl, 2019). While the initial instinct may be to use the Twitter API instead of webscraping, that service only provides the last couple weeks of tweets and our analysis will need tweets from much further back. 
Given the vast number of tweets on this subject in even just a single day, we will limit this data pull to 10 tweets per day, per phrase. At this point I would like to note that we will not be limiting location to Australia. Not only does doing so severely limit the results of the data pull (often to less than 10 per day), but climate change is a global issue, and the Australian Bushfires were extensively covered in global news. The resulting code for this data pull gives us a series of loops like this: 

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/getOldTweetsLoop.png)

For the complete query, please see the file [GetTweets_Year.](https://github.com/LBusalacchi/msds692/blob/master/GetTweets_Year.py)

## EDA & Data Cleansing
Our first look at the data shows a few changes needed right off the bat, dropping an extraneous column, adding descriptive column headers, and ensuring each field is the correct data type.  

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/og.png)

We also want to ensure there are no duplicates:

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/duplicates.png)

Let’s look by date now since that will be a key field in our later analysis:

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/spikebymonth.png)

January is much higher than the other months, and some digging reveals that while our initial data pull was for 2019, the nature of the date function used with Twitter allows for a few dates on either end of the limit. This can be remedied with a quick filter: 

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/newbymonth.png)

We can now start adding the groups we want to use to analyze the data later, by both data as well key phrase. 

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/date_groups.png)

Our resultant dataset now looks like this: 

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/withgroups.png)

## Sentiment Analysis Preparation
We are now ready to specifically prepare our text for the sentiment analysis.  We will be using the tweet_cleaner function written by Kim (2018), with a few minor changes. This function will remove tags which should be treated as proper nouns, the first part of website addresses, and decode some characters. 
![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/cleaner.png)

## Sentiment Analysis
Now that EDA and cleansing is complete, let's get some sentiment scores! We will use the NLTK Vader package, which is specifically designed for sentiment analysis of social media, and actually takes into account the way capitalization, punctuation, and emojis are used with language to provide a more accurate score of the overall sentiment than traditional sentiment analysis (Pandey, 2018). While many other sentiment analysis packages require tokenization of the text, cleaning of cases, converting to root words, and so on, this nifty little package does a lot of that for you!
With another loop we can get the below details to append back onto our Tweets3 dataset:
![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/sentiment.png)

## Comparing Scores

With the sentiment scores, we can now begin to analyze how the different groups we’ve previously defined differ from each other in sentiment. In order to compare and understand if these differences are statistically significant, we must first assess the normality of our data to ensure we perform the correct statistical test. 

Overall our data is not showing a nice bell curve, and given the scale of negative to positive numbers, we are unable to perform any power transformations as a result. Our mean also confirms that the overall sentiment where climate change is involved is negative.

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/all.png)

At the group levels we continue to see skewed distributions and can start to see the differences between the phrases. While the means are all different, tweets with the phrase “global warming” have a positive mean sentiment, which turns out the be the only analyzed group with a positive mean!

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/change.png)

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/cc.png)

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/gw.png)

Within our date groups we begin to see more of the same, non-normal distributions, but perhaps not as much variation in the mean sentiment. 

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/pre_season.png)

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/na_only.png)

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/national.png)

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/soe.png)

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/rlyhot.png)

Since our data is not normal (or non-parametric) we will use a Mann-Whitney U test. With the standard alpha of 95% confidence, we can perform a test as follows to test for significant differences. 

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/MAnnWhitney.png)

For our key word groups, the sentiment is significantly different for all three. 

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/keyword_diff.png)

For the date groups, the results were more varied. While everything was different from our last group, the hottest day of the year until the end of 2019, there was slower change in sentiment as the bushfires began. 

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/dg_differences.png)

Further visualization of the data confirms that this isn’t entirely unexpected, as several very large dips occur in a short amount of time. This includes the lowest average sentiment day of the year, which could be correlated with the evacuations of thousands of residents in efforts to reduce fatalities. 

![alt text](https://github.com/LBusalacchi/msds692/blob/master/images/dashboard.png)

To further explore the data, please view the dashboard posted on [Tableau Public]( https://public.tableau.com/profile/lauren.busalacchi#!/vizhome/AustralianBushfireSentimentAnalysis/Dashboard1).

