# use the py code from https://developer.linkedin.com/documents/quick-start-guide

#!/usr/local/bin/python
# -*- coding: ascii -*-

import oauth2 as oauth
import httplib2
import time, os, simplejson
import xml.etree.ElementTree as ET

#########################
#Import secrets
from secrets import secret

#######################
#Load auth keys
CONSUMER_KEY = secret['API_KEY']
CONSUMER_SECRET = secret['Secret_Key']
USER_TOKEN = secret['OAUT']
USER_SECRET = secret['OAUS']
RETURN_URL = 'http://localhost:8000'
GROUP_ID = secret['Group_ID']

def linkedin_group_read():
    # Use your API key and secret to instantiate consumer object
    consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
 
    # Use the consumer object to initialize the client object
    client = oauth.Client(consumer)
     
    # Use your developer token and secret to instantiate access token object
    access_token = oauth.Token(
                key=USER_TOKEN,
                secret=USER_SECRET)
     
    client = oauth.Client(consumer, access_token)
     
    # Make call to LinkedIn to retrieve your own profile in json
    # resp,content = client.request("http://api.linkedin.com/v1/people/~?format=json", "GET", "")
    
    # cannot output json, by adding "?format=json". why?
    #resp,content = client.request("http://api.linkedin.com/v1/groups/"+str(GROUP_ID)+"/posts:(creation-timestamp,title,summary,creator:(first-name,last-name,picture-url,headline),likes,attachment:(image-url,content-domain,content-url,title,summary),relation-to-viewer)?category=discussion&order=recency&modified-since=1302727083000&count=1")
    
    #resp,content = client.request("http://api.linkedin.com/v1/groups/"+str(GROUP_ID)+"/posts:(title,summary,creator:(first-name,last-name,picture-url,headline),likes,attachment:(image-url,content-domain,content-url,title,summary),relation-to-viewer)?category=discussion&order=popularity")
    
    resp,content = client.request("http://api.linkedin.com/v1/groups/"+str(GROUP_ID)+"/posts:(title,summary,attachment:(title,summary))?category=discussion&order=recency&count=2")
    
    # print "resp"
    # print resp
    
    # print "content"
    # print content
    
    root = ET.fromstring(content)
    #print root
    
    title_list = []
    summary_list = []
    
    for post in root.findall('post'):
        title = post.find('title').text
        title_list.append(title)
        summary = post.find('summary').text
        summary_list.append(summary)
        print title+'\n'
        print summary+'\n'
    
    print "lists\n"
    for title in title_list:
        print title+'\n'
    
    for summary in summary_list:
        print summary+'\n'


    
  
