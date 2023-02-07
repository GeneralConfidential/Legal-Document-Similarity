from itertools import product
import nltk
from nltk import wordnet

def wordSimilarity(wrd1,wrd2):
    syns1 = wordnet.synsets(wrd1)
    syns2 = wordnet.synsets(wrd2)
    for sn1, sn2 in product(syns1, syns2):
        if syns1 == syns2:
            return 1.0
        else:
            return wordnet.wup_similarity(sn1, sn2)


def comp(txt1,txt2):
    assert len(txt1) == len(txt2), "Different number of lines in samples."
    sim = []
    a=txt1.copy()
    b=txt2.copy()
    for i in txt1:
        tmp=[]
        for j in txt2:
            tmp.append(False)
        sim.append(tmp)
    
    for i,j in a,b:
        for w1 in i:
            if i == []:
                break
            for w2 in j:
                if j == []:
                    break
                if w1 == w2:
                    sim[a.index(i)][b.index(w1)]
                    i.discard(w1)
                    j.discard(w2)

    score = [0]*len(txt1)
    total = score.copy()
    for i in range(txt1):
        for j in range(sim[i]):
            total[i][j] += 1
            if sim[i][j]:
                score[i][j] += 1
    
    return (sum(score)/sum(total))*100