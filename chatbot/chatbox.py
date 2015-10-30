import wikipedia

stop_words = set(["my", "is", "your", "name", "the", "I", "won", "i", "a", "game", "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't" "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd" "i'll," "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's" "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this" "those", "through", "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]) #setting all my stopwords
happy_responce = set(["happy", "good", "joy"])
sad_responce = set(["sad", "unhappy", "upset"])

def remove_stop_words(wordlist, stopwords=stop_words): #calling the stopwords and creating the function 
    if not wordlist: 
        sentence = raw_input("hello whats your name? ") #splitting up the responce and putting it into an array
        wordlist = sentence.split()
    intro = []
        
    for t in wordlist: #looping through what was entered and taking out anything thats in the stopwords
        if t.lower() in stopwords:
            intro.append
            ("")
        else:
            intro.append(t)
    return intro

wordlist = []
intro_list = remove_stop_words(wordlist)
sentence = raw_input("Nice to meet you " + intro_list[0] + ", how are you today? ") #the responce to the previous question and also prints the name that was entered

def happyResponce(happyword, happyresponce=happy_responce):
    if not happyword:
        responce = raw_input("Nice to meet you " + intro_list[0] + ", how are you today? ")
        happyword = responce.split()
    happy = []
    
    for h in happyword:
        if h.lower() in happyresponce:
            happy.append
            ("")
        else:
            happy.append(t)
    return happy

happyword = []
happy_list = happyResponce(happyword)
print("thats good to hear")

def sadResponce(sadword,sadresponce=sad_responce):
    if not sadword:
        responcesad = raw_input("Nice to meet you " + intro_list[0] + ", how are you today? ")
        sadword = responcesad.split()
    sad = []
    
    for s in sadword:
        if s.lower() in sadresponce:
            sad.append
            ("")
        else:
            sad.append(t)
    return sad
    
sadword = []
sad_list = sadResponce(sadword)
print("Oh why is that")

def wikiSearch(wordlist, stopwords=stop_words):
    if not wordlist: 
        search = raw_input("why is that? ")
        wordlist = search.split()
    thing = []
    
    for w in wordlist:
        if w.lower() in stopwords:
            thing.append
            ("")
        else:
            thing.append(w)
    return thing

wordlist = []
thing_list = wikiSearch(wordlist) 
wikipedia.search(thing_list[0])
wikipedia.set_lang("en")
print(wikipedia.summary(thing_list[0], sentences=1))
search = raw_input("anything else? ")
wikiSearch(wordlist)