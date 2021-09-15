[
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
        jokegen(),
]
#import?
