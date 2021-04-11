import pandas as pd

def sentimental(x):
    d = str(x)
    d = d.lower()
    dt = d.split()
    dt = [item.replace(".", "").replace("/", " ").replace("!", " ").replace("(", " ").replace(")", " ").replace('?', ' ').replace('"', ' ').replace('name', ' ').replace('dtype', ' ').replace('\\n', ' ').replace('float64', ' ').replace('!', ' ').replace('[', ' ').replace(']', ' ').replace(',', ' ').replace(':', ' ').replace('series', ' ')for item in dt]
    d = " "
    d = d.join(dt)
    dt = d.split()
    score = {'very':1, 'fantastic': 2, 'nature': 1, 'great': 3, 'enjoy': 1, 'thank': 1, 'cozy':1, 'superb':3, 'wonderful':4,'comfortable':1, 'best':2, 'nice':3, 'beautiful':2, 'gorgeous':4, 'surprising':3,'relaxing': 3, ' impressed': 3, ' extraordinary': 5, 'excellent':4}
    cums = {'very':0, 'fantastic': 0, 'nature': 0, 'great': 0, 'enjoy': 0, 'thank': 0, 'cozy':0, 'superb':0, 'wonderful':0, 'comfortable':0, 'best':0, 'nice':0,'beautiful':0, 'gorgeous':0, 'surprising':0,'relaxing': 0, ' impressed': 0, ' extraordinary': 0, 'excellent':0}
    count = 0
    points = 0
    for d in dt:
        for key in list(score.keys()):
            if d.startswith(key):
                cums[key] += 1
                points = score[key] + points
        count = count + 1
    display=" "
    display = display.join(dt)
    SentimentalScore = int((points/count)*5)
    
    return SentimentalScore