import wikipedia

stop_words = set(["my", "is", "your", "name"])
happy_responce = set(["happy"])
sad_responce = set(["sad"])

def remove_stop_words(wordlist, stopwords=stop_words):
    if not wordlist: 
        sentence = raw_input("hello whats your name? ")
        wordlist = sentence.split()
    intro = []
        
    for t in wordlist:
        if t.lower() in stopwords:
            intro.append
            ("")
        else:
            intro.append(t)
    return intro

wordlist = []
intro_list = remove_stop_words(wordlist)

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