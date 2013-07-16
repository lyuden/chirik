import os
import json
import demjson
import sys

def removefield(s, f):
  s = s.replace(f, '')
  return s

def removefields(s, fs):
  for f in fs:
    s = removefield(s, f)
  return s
  
def replaceEq(s, f):
  s = s.replace(", " + f + '=', ', "'+f+'"'+':')
  s = s.replace("{" + f + '=', '{"'+f+'"'+':')
  return s

def replaceEqs(s, fs):
  for f in fs:
    s = replaceEq(s, f)
  return s

def removefields(s, fs):
  for f in fs:
    s = removefield(s, f)
  return s

def surroundbyQuotes(s, f):
  fm = f.split('=')[0]
  while (f in s):
    which = ","
    if (s.split(f)[1].find("}") < s.split(f)[1].find(",")):
      which = "}"
    #s = s.split(f)[0] + '"' + fm + '":"' + s.split(f)[1].split(which)[0] + '"' + which + which.join(s.split(f)[1].split(which)[1:])
    start = s.find(f)
    end = s.find(which, start)
    s = s[:start] + fm + ':' + '"' + s[start + len(f):end] + '"' + s[end:]
  return s

def fixJSON(s):
  #s = s.split("createdAt=")[0] + "createdAt='" + s.split("createdAt=")[1].split("2012")[0] + "2012'" + s.split("createdAt=")[1].split("2012")[1]
  sorig = s
  s = surroundbyQuotes(s, "createdAt=")
  s = surroundbyQuotes(s, "url=")
  #s = surroundbyQuotes(s, "expandedURL=")
  s = surroundbyQuotes(s, "displayURL=")
  s = surroundbyQuotes(s, "mediaURL=")
  s = surroundbyQuotes(s, "mediaURLHttps=")
  
  #if ("name=" in s):
    #namestart = s.find("name=") + 5
    #nameend = s.find("screenName", namestart) - 4
    #s = s[:namestart] + s[namestart:nameend].replace("'", "\\'") + s[nameend:]
  
  s = removefields(s, ["GeoLocation", "TweetJSONImpl", "UserMentionEntityJSONImpl", "URLEntityJSONImpl", "HashtagEntityJSONImpl", "MediaEntityJSONImpl"])
  s = replaceEqs(s, ["name", "latitude", "longitude", "resize", "width", "height", "sizes", "text", "toUserId", "toUser", "fromUser", "id", "fromUserId", "isoLanguageCode", "source", "profileImageUrl", "createdAt", "location", "place", "geoLocation", "annotations", "userMentionEntities", "start", "end", "screenName", "urlEntities", "hashtagEntities", "mediaEntities", "url", "displayURL"])
  
  textStart = 9
  textEnd = s.find("toUserId") - 4
  s = s[:textStart] + s[textStart:textEnd].replace("'", "\\'") + s[textEnd:]
  
  while ("expandedURL=" in s):
    expURLstart = s.find("expandedURL=") + 11
    expURLend = s.find("displayURL", expURLstart) - 2
    s = s[:expURLstart] + ":'" + s[expURLstart + 1:expURLend] + "'" + s[expURLend:]
    #print s
  
  s = s.replace("0=Size", "0:")
  s = s.replace("1=Size", "1:")
  s = s.replace("2=Size", "2:")
  s = s.replace("3=Size", "3:")
  s = s.replace('\n', ' ')
  
  #s = s.replace(' rel="nofollow"', 'rel="nofollow"')
  #s = s.replace('\"\'', '"')
  #s = s.replace('\'\"', '"')
  #s = s.replace("'null'", '"null"')
  #s = s.replace("None", '"None"')
  #s = s.replace("null", '"None"')
  #s = s.replace("'", '"')
  #s = s.replace("=", ":")
  #print sorig
  #print s
  return s

def loadBadJSON(f):
  a = open(f, 'r')
  s = a.read()
  a.close()
  try:
    #print fixJSON(s)
    #print s
    return demjson.decode(fixJSON(s))
  except Exception as e:
    #s
    #print s
    print fixJSON(s)
    print e
    #sys.exit(1)
  #a.close()
