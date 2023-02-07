# Module: Text Simplifier
# Simplifies paragraph into list of list of simplified sentences of paragraphs.

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
stop = set(stopwords.words("english"))
stop.remove("not")
stop.remove("no")
posIgnore = ["$","''","(",")",",","--",".",":","CD","FW","LS","NNP","NNPS","NNS","PRP","PRP$","SYM","TO","WDT","WP","WP$","WRB","``"]
exStr = "There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level."

def getWnetPos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def simplify(parag = exStr):
    stns = sent_tokenize(parag)
    wrds = []
    for a in stns:
        wrds.append(word_tokenize(a))
    wrdsFilt = []
    for i in wrds:
        temp = []
        for j in i:
            if j.casefold() not in stop:
                temp.append(j)
        wrdsFilt.append(temp)

    tagged = []
    for words in wrdsFilt:
        tagged.append(nltk.pos_tag(words))

    wrdsLem = []
    for words in tagged:
        for word in words:
            if word[1] in posIgnore:
                wrdsLem.append(word[0])    
            elif getWnetPos(word[1]) != None:
                wrdsLem.append([lemmatizer.lemmatize(word[0],pos=getWnetPos(word[1]))])
            else:
                wrdsLem.append([lemmatizer.lemmatize(word[0])])

    for words in wrdsLem:
        for word in words:
            synons = []
            for ss in wordnet.synsets(word):
                synons.append(ss)
            synons.sort()
            if(synons):
                word = synons[0]
            synons.clear()
    return wrdsLem