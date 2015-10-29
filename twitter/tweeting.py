import twitter, datetime #importing the libaries
import urllib2

file = open("keys.txt") #reading in the twitter credentials and splitting them up
creds = file.readline().strip().split(',')

currentSession = open("/Users/tobystimpson/Library/Application Support/Google/Chrome/Default/Current Session") #finding the current session in google chrome and getting all the information
twit = currentSession.read()
lines = twit.splitlines()

webaddress = " "
for line in lines:
    if (line.find("//") != -1):
        startIndex = line.rfind("//") + 2 #loops throught the lines and finds the web url
        endIndex = line.rfind("/")
        webaddress = line[startIndex:endIndex]

api = twitter.Api(creds[0], creds[1], creds[2], creds[3])

timestamp = datetime.datetime.utcnow()

#response = api.PostUpdate("Tweeted at " + str(timestamp))
response = api.PostUpdate("I like " + webaddress) #posts the web address to twitter

print("Status update to: " + response.text)