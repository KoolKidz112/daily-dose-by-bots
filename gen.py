import random
import urllib.request
import json
import yake

from gtts import gTTS as t
from random_word import RandomWords
from serpapi import GoogleSearch
from randfacts import get_fact as fact
from joke_generator import generate as jokegen
word = RandomWords().get_random_word()
print("Getting word. If it gets in a loop, try restarting!")
if not word:
    exit("Couldn't get word. Try restarting!")

print("Init completed. Starting yake...")
extractor = yake.KeywordExtractor(lan="en",numOfKeywords=50)

introSt = random.choice(
    [
        "Welcome to wonderful news. These news will tell you all you need to know about the world around you. It is simply excellent and you will love it. We will cover many things on wonderful news videos. New video of a news every day. It will be excellent. This might be the one hundredth time you have heard this intro statement. If so, excellent. Congratulations. Let's get into the wonderful news.",
        "Welcome to the excellent news, every often. These news are human curated and not made by bots, which will help you be sure it is real and factual. Let us begin.",
        "Do you like to learn? If so, welcome to excellency news, sponsored by Google. Google sponsors. It sponsors because they have created me. Wow. Simply excellent. We begin in just a few seconds.",
        "Good morning and welcome to the Black Mesa Transit System. This automated train is provided for the security and convenience of employees of the Black Mesa Research Facility personnel. Please feel free to move about the train or simply sit back and enjoy the ride.",
    ]
    )
searchSt = random.choice(
    ['Let us begin by giving you the wonderful search of the day.',
     'Let\'s begin with an excellent search of Google.',
     'Here is a Google Search, sponsored by Google. Fun fact, my voice is made by Google. Excellent. Here is the search.']
    )
searchQ = random.choice(
    [
        'latest '+word+' game',
        'how to get free '+word+' no virus no malware 2021 working free',
        word,
        'top 10 '+word+'s',
        'why '+word+' is important'
    ]
)
print("Loading weather data")
weatherURL = "https://www.7timer.info/bin/civil.php?lon=-82.6&lat=30.1&ac=0&unit=metric&output=json&tzshift=0"
weatherIMG = "https://www.7timer.info/bin/civil.php?lon=-82.602&lat=30.058&lang=en&ac=0&unit=metric&tzshift=0"
with urllib.request.urlopen(weatherURL) as url:
    weatherParse = json.loads(url.read().decode())
    print(weatherParse)
weatherSt = random.choice(
    [
        "Wow, excellency. The excellency has been refined. Now onto the weather for Hell, Michigan.",
        "Go to hell. Hell, Michigan, of course. Weather there is quite oddly. Let's have a look.",
        "I love weather, but I hate hell, so here is the weather for Hell, Michigan."
    ]
)
factSt = random.choice(
    [
        "Now we can begin the facts. The factual facts, along with the jokes. I love both of these things. Happy happy, joy joy.",
        "There is nothing I love more than the knowledge of the stuff and the humor of the life. Excellent. Refinery has been achieved."
    ]
)
print("Finished initial search and intro variables. Random word is "+word+".")
# USE WHEN CODE IS READY
#searchCall = GoogleSearch({
#    "q": searchQ,
#    "hl": "en",
#    "api_key": "ede3f634c071dfbd7073f17ffcbed70f4e0b7671cc5bc0af6892c7d4f39522e7"
#})
#searchRes = searchCall.get_dict()
#print("Search completed!")
#print(searchRes['search_metadata'])
#if searchRes['search_metadata']['status'] != "Success":
#    print("Search failure")
#else:
#    searchFinalTop = searchRes['organic_results'][0]['title']
#    searchFinalDesc = searchRes['organic_results'][0]['snippet']
#    searchFinalSec = searchRes['organic_results'][1]['title']
#    searchFinalLast = searchRes['organic_results'][2]['title']
#    if 'inline_videos' in searchRes:
#        searchFinalVideo = searchRes['inline_videos']['title']+" on "+searchRes['inline_videos']['platform']
print("Search results sucessfully scraped. Starting export...")
scriptArr=[
        introSt,
        searchSt,
        #"Today's search is "+searchQ+". The results are "+searchFinalTop+". The description for this result is this: "+searchFinalDesc+". Wow. What an excellent search. Just so we can be sure of how factual our search is, let us see the other results.",
        #"The next result's title is "+searchFinalSec+", and the final result's title is "+searchFinalLast+". ",
        weatherSt,
        "Today in Hell, Michigan you can expect "+str(weatherParse['dataseries'][0]['prec_amount'])+" preciptation. ",
        "The wind will be going "+str(weatherParse['dataseries'][0]['wind10m']['speed'])+"MPH at direction ",
        weatherParse['dataseries'][0]['wind10m']['direction'],
        ". As for weather I don't know how to parse it. Owned. Here is fast version. Weather is ",
        weatherParse['dataseries'][0]['weather']+". ",
        factSt+" Did you know? ",
        fact()+". Here is a very silly and humorous joke. It will give you a laugh. ",
        jokegen(),]
script = "".join(scriptArr)
print('Extracting important keywords using YAKE...')
keywords = extractor.extract_keywords(script)
for kw in keywords:
    print(kw)
audio = t(text=script,lang="en",tld="com")
audio.save('audio.mp3')
print("Done! Saved to audio.mp3")
