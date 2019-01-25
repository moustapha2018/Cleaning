def Cleaning(liste):
    import re 
    import nltk 
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    ps = PorterStemmer()
    stopwords = list(set(stopwords.words('english')))
    Liste = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(0,len(Liste)):
        stopwords.append(Liste[i])
    corpus = []
    for i in range(0,len(liste),1):
        review = re.sub('[^a-zA-Z]',' ',liste[i])
        review = review.lower()
        review = review.split()
        review = [ps.stem(i) for i in review if i not in stopwords]
        review = ' '.join(review)
        corpus.append(review)
    return corpus